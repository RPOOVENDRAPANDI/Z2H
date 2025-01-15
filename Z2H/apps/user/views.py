from rest_framework import generics, authentication, permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from apps.user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    RegisterUserSerializer,
    UserPasswordUpdateSerializer,
    UserListSerializer,
    WebAuthTokenSerializer,
    CustomerSerializer,
    UpdateRegisterUserDetailsSerializer,
    Z2HCommissionSerializer,
    RegisterUserDetailsSerializer,
    CustomerNotGotDownlineSerializer,
)
from apps.user.permissions import ReferrerLimitPermission
from apps.user.models import Z2HUser, Z2HCustomers, Z2HUserRoles, Role, RegisterUser
from apps.app.models import Z2HWebPages, Z2HWebPageRoles, Z2HOrders
from apps.utils.tasks import send_email
import random
import string
from rest_framework.decorators import action
from django.db.models import Q
from django.utils import timezone
from django.utils.dateparse import parse_date
from datetime import timedelta
from django.core.paginator import Paginator

LOOKUP_REGEX = '[0-9a-f-]{36}'

def generate_password(length=8):
    required_password_char_length = length - 2
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    password = ''.join(random.choices(letters, k=required_password_char_length))
    password += random.choice(letters.upper())
    password += random.choice(digits)
    password += random.choice(special_chars)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    password = password.replace("\\", "$").replace("\"", "*")

    if len(password) < required_password_char_length:
        password += generate_password(required_password_char_length - len(password))

    return password

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrive and return the authenticated user."""
        return self.request.user

class ListUsersView(generics.ListAPIView):
    """List all the users in the system."""
    serializer_class = UserListSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        """Return all the users."""
        return Z2HCustomers.objects.all()

class UserLoginView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def handle_web_login(self, request_data):
        data = {
            'status': 'success',
            'message': 'Login Successful',
            'token': None,
        }

        serializer = WebAuthTokenSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        request_data = request.data

        accessed_from = request_data.get('accessed_from', None)

        if accessed_from == 'web':
            return self.handle_web_login(request_data)

        data = {
            'status': 'success',
            'message': 'Login Successful',
        }

        mobile_number = request_data.get('mobile_number')

        user_email = str(mobile_number) + "@z2h.com"
        z2h_user = Z2HUser.objects.filter(email=user_email).first()

        if z2h_user and z2h_user.is_first_login:
            z2h_user.is_first_login = False

        z2h_customer_uids = []
        z2h_customer = Z2HCustomers.objects.filter(user=z2h_user)
        if z2h_customer:
            z2h_customer_uids = [customer.uid for customer in z2h_customer]
        
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        data['is_first_login'] = user.is_first_login
        data["customer_uids"] = z2h_customer_uids

        z2h_user.save()
        return Response(data, status=status.HTTP_200_OK)
    
class GetUserInfoView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_user_info(self, user):
        user_role = Z2HUserRoles.objects.filter(user_uid=str(user.uid)).first()
        role = Role.objects.filter(uid=user_role.role_uid).first()
        web_page_roles = Z2HWebPageRoles.objects.filter(role_uid=role.uid, is_active=True)
        web_pages = Z2HWebPages.objects.filter(uid__in=[web_page_role.web_page_uid for web_page_role in web_page_roles])

        user_info = {
            'uid': user.uid,
            'name': user.name,
            'email': user.email,
            'role': role.name,
            'web_pages': [web_page.name for web_page in web_pages],
        }

        return user_info
    
    def get_check_user(self, request):
        enable_payment = False
        is_existing_user = False
        customer = Z2HCustomers.objects.filter(user=request.user).first()

        if not customer:
            enable_payment = True

        if customer:
            is_existing_user = True
        
        if customer and customer.is_level_one_completed and customer.is_level_two_completed \
            and customer.is_level_three_completed and customer.is_level_four_completed:
            enable_payment = True

        return enable_payment, is_existing_user
    
    def get_registered_users_under_user(self, request):
        registered_users_under_user_all = RegisterUser.objects.filter(
            referred_by__user=request.user, is_referrer_got_notified_for_joining=False
        ).all()

        # Remove registered users present in Z2hCustomers
        registered_users_under_user = []
        for registered_user in registered_users_under_user_all:
            customer = Z2HCustomers.objects.filter(user=registered_user.user).first()
            if not customer:
                registered_users_under_user.append({
                    "name": registered_user.name,
                    "mobile_number": registered_user.mobile_number,
                    "id": registered_user.id,
                    "uid": registered_user.uid,
                })

        return registered_users_under_user
    
    def get_product_purchased_users_under_user(self, request):
        referrer = Z2HCustomers.objects.filter(user=request.user).first()

        customers_under_referrer = Z2HCustomers.objects.filter(
            referrer=referrer, is_referrer_got_notified_for_joined_level_one=False,
        ).all()

        product_purchased_users_under_user = []
        for customer in customers_under_referrer:
            register_user = RegisterUser.objects.filter(user=customer.user).first()
            if register_user:
                product_purchased_users_under_user.append({
                    "name": register_user.name,
                    "mobile_number": register_user.mobile_number,
                    "customer_number": customer.customer_number,
                    "customer_uid": customer.uid,
                })


        return product_purchased_users_under_user

    def get_level_completed_status_of_user(self, request):
        level_one_completed_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_one_completed=True, is_user_got_notified_for_level_four_completion=False
        )
        level_two_completed_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_two_completed=True, is_user_got_notified_for_level_four_completion=False
        )
        level_three_completed_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_three_completed=True, is_user_got_notified_for_level_four_completion=False
        )
        level_four_completed_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_four_completed=True, is_user_got_notified_for_level_four_completion=False
        )

        level_completed_status_of_user = {
            "level_one_completed": level_one_completed_status.exists(),
            "level_two_completed": level_two_completed_status.exists(),
            "level_three_completed": level_three_completed_status.exists(),
            "level_four_completed": level_four_completed_status.exists(),
        }

        return level_completed_status_of_user
    

    def get_commission_paid_status_of_user(self, request):
        level_one_commission_paid_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_one_commission_paid=True, is_user_got_notified_for_level_one_commission_paid=False
        )
        level_two_commission_paid_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_two_commission_paid=True, is_user_got_notified_for_level_two_commission_paid=False
        )
        level_three_commission_paid_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_three_commission_paid=True, is_user_got_notified_for_level_three_commission_paid=False
        )
        level_four_commission_paid_status = Z2HCustomers.objects.filter(
            user=request.user, is_level_four_commission_paid=True, is_user_got_notified_for_level_four_commission_paid=False
        )

        commission_paid_status_of_user = {
            "level_one_commission_paid": level_one_commission_paid_status.exists(),
            "level_two_commission_paid": level_two_commission_paid_status.exists(),
            "level_three_commission_paid": level_three_commission_paid_status.exists(),
            "level_four_commission_paid": level_four_commission_paid_status.exists(),
        }

        return commission_paid_status_of_user

    
    def get_user_info_for_mobile(self, request):
        data = {
            'status': 'success',
            'message': 'User Infomation!!!',
        }
        
        user = RegisterUser.objects.filter(user=request.user).first()

        if not user:
            data['status'] = 'error'
            data['message'] = 'User Not Found'
            return Response(data, status=status.HTTP_200_OK)

        customer = Z2HCustomers.objects.filter(id=user.referred_by.id).first()

        referrer = RegisterUser.objects.filter(user=customer.user).first()

        user_customer = Z2HCustomers.objects.filter(user=request.user).first()

        enable_payment, is_existing_user = self.get_check_user(request)

        registered_users_under_user = self.get_registered_users_under_user(request)

        product_purchased_users_under_user = self.get_product_purchased_users_under_user(request)

        level_completed_status_of_user = self.get_level_completed_status_of_user(request)

        commission_paid_status_of_user = self.get_commission_paid_status_of_user(request)
        
        user_info = {
            'registered_date': user.created,
            'name': user.name,
            'nominee_name': user.nominee_name,
            'date_of_birth': user.date_of_birth,
            'marital_status': user.marital_status,
            'gender': user.gender,
            'aadhar_number': user.aadhar_number,
            'pan': user.pan,
            'mobile_number': user.mobile_number,
            'city': user.city,
            'town': user.town,
            'address': user.address,
            'pin_code': user.pin_code,
            'name_of_bank': user.name_of_bank,
            'name_as_in_bank': user.name_as_in_bank,
            'ifsc_code': user.ifsc_code,
            'bank_branch': user.bank_branch,
            'account_number': user.account_number,
            'email_address': user.email_address,
            'district': user.district.name,
            'state': user.district.state.name,
            'referrer_uid': customer.customer_number,
            'referrer_name': referrer.name,
            'referrer_city': referrer.city,
            'referrer_town': referrer.town,
            'referrer_mobile_number': referrer.mobile_number,
            'profile_photo_path': user.profile_photo_path,
            'enable_payment': enable_payment,
            "is_existing_user": is_existing_user,
            "user_customer_uid": user_customer.uid if user_customer else None,
            "user_customer_number": user_customer.customer_number if user_customer else None,
            "is_user_under_no_plan": True if not user_customer else False,
            "is_first_login": request.user.is_first_login,
            "registered_users_under_user": registered_users_under_user,
            "product_purchased_users_under_user": product_purchased_users_under_user,
            "level_completed_status_of_user": level_completed_status_of_user,
            "commission_paid_status_of_user": commission_paid_status_of_user,
        }

        data['user_info'] = user_info

        return Response(data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        accessed_from = request.GET.get('accessed_from', None)

        if not accessed_from:
            return Response({'status': 'error', 'message': 'Accessed From is required'}, status=status.HTTP_400_BAD_REQUEST)

        if accessed_from == 'mobile':
            return self.get_user_info_for_mobile(request)

        data = {
            'status': 'success',
            'message': 'User Infomation!!!',
        }
        user = request.user
        user_info = self.get_user_info(user)
        data['user_info'] = user_info
        return Response(data, status=status.HTTP_200_OK)
    
class UserLogoutView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            'status': 'success',
            'message': 'Logout Successful',
        }
        request.user.auth_token.delete()
        return Response(data, status=status.HTTP_200_OK)
    
class UpdatePasswordView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        data = {
            'status': 'success',
            'message': 'Password Updated Successfully',
        }
        user = request.user
        password = request.data.get('password')

        serialier = UserPasswordUpdateSerializer(data=request.data)

        if serialier.is_valid():
            user.set_password(password)
            user.is_password_updated = True
            user.save()
            return Response(data, status=status.HTTP_200_OK)

        data['message'] = serialier.errors
        data['status'] = 'error'
        return Response(data, status=status.HTTP_200_OK)
    
class RegisterUserView(APIView):
    authentication_classes = []
    permission_classes = [ReferrerLimitPermission, ]

    def get_create_new_user(self, request_data):
        mobile_number = request_data.get('mobile_number')
        name = request_data.get('name')

        email = str(mobile_number) + "@z2h.com"

        check_user_exists = Z2HUser.objects.filter(email=email).exists()
        if check_user_exists:
            return "user_exists"

        password = generate_password()

        data = {
            'email': email,
            'password': password,
            'name': name,
        }

        user_serializer = UserSerializer(data=data)

        if user_serializer.is_valid():
            user_serializer.save()
            data = user_serializer.data
            data['password'] = password
            return data
        
        return None
    
    def post(self, request, *args, **kwargs):
        request_data = request.data

        referred_by = Z2HCustomers.objects.filter(customer_number=request_data.get('referred_by')).first()

        if not referred_by:
            data = {
                "status": "Error",
                "message": "No Referrer Found!!!"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        referred_by_id = referred_by.id
        request_data['referred_by'] = referred_by_id

        serializer = RegisterUserSerializer(data=request_data)

        if serializer.is_valid():
            new_user_password = self.get_create_new_user(request_data)

            if not new_user_password:
                data = {
                    "status": "Error",
                    "message": "Something went wrong!!!"
                }
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
            
            if new_user_password == "user_exists":
                data = {
                    "status": "Error",
                    "message": "User Already Exists!!!"
                }
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            user_uid = Z2HUser.objects.get(email=new_user_password['email']).uid

            password = new_user_password['password']

            data = {
                "status": "Success",
                "message": "User Created Successfully!!!",
                "uid": user_uid,
            }

            subject = "Zero To Hero Login Credentials"
            body = f"The System Generated Password for Zero To Hero Login of User '{request_data['name']}' is {password}"
            
            try:
                send_email(to_email=request_data['email_address'], body=body, subject=subject)
            except Exception as e:
                return Response(data={"error:failed on sending the email to the user,check on your smtp username and password"}, status=status.HTTP_201_CREATED)
            
            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        
        data = {
            "status": "success",
            "message": "User Details Updated Successfully!!!",
        }
        
        request_data = request.data

        bank_name = request_data['bankName']
        bank_account_number = request_data['bankAccountNumber']
        name_as_in_bank = request_data['nameAsInBank']
        bank_branch = request_data['bankBranch']
        ifsc_code = request_data['ifscCode']
        city = request_data['city']
        town = request_data['town']
        district = request_data['district']
        address = request_data['address']
        user_status = request_data['userStatus']
        pin_code = request_data['pinCode']
        customer_uid = request_data['customerUid']

        user = Z2HCustomers.objects.filter(uid=customer_uid).first().user

        RegisterUser.objects.filter(user=user).update(
            name_of_bank=bank_name,
            account_number=bank_account_number,
            name_as_in_bank=name_as_in_bank,
            bank_branch=bank_branch,
            ifsc_code=ifsc_code,
            city=city,
            town=town,
            district=district,
            address=address,
            pin_code=pin_code,
        )

        if user_status == 'Active':
            user.is_active = True
            user.save()

        if user_status == 'Inactive':
            user.is_active = False
            user.save()

        return Response(data, status=status.HTTP_200_OK)
    
class UpdateRegisterUderDetailsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request_data = request.data

        register_user = RegisterUser.objects.filter(user=request.user).first()

        serializer = UpdateRegisterUserDetailsSerializer(register_user, data=request_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "Success",
                "message": "User Details Updated Successfully!!!",
                "data": serializer.data,
            }
            return Response(data=data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ValidateReferrerView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        referrer_uid = request.query_params.get('referrer_uid', None)

        if not referrer_uid:
            data = {
                "status": "Error",
                "message": "Referrer UID is required!!!"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        referred_by = Z2HCustomers.objects.filter(customer_number=referrer_uid).first()
        if not referred_by:
            data = {
                "status": "Error",
                "message": "No Referrer Found!!!"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            "status": "Success",
            "message": "Referrer Found!!!"
        }

        register_user = RegisterUser.objects.filter(user=referred_by.user).first()

        referrer_name = referred_by.user.name
        referrer_city = register_user.city

        data["referrer_name"] = referrer_name
        data["referrer_city"] = referrer_city
        
        return Response(data=data, status=status.HTTP_200_OK)
    
class ForgotPasswordView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        email_address = request.query_params.get('email_address', None)
        mobile_number = request.query_params.get('mobile_number', None)

        data = {
            'status': 'success',
            'message': 'Email Sent Successfully!!!',
        }

        if not email_address:
            data['status'] = 'error'
            data ['message'] = 'Email Address is required!!!'
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        if not mobile_number:
            data['status'] = 'error'
            data ['message'] = 'Mobile Number is required!!!'
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        register_user = RegisterUser.objects.filter(email_address=email_address, mobile_number=mobile_number)
        if not register_user.exists():
            data['status'] = 'error'
            data['message'] = 'User Not Found!!!'
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        
        user = register_user.first().user
        new_password = generate_password()

        data = {
            'password': new_password
        }

        serialier = UserPasswordUpdateSerializer(data=data)

        if serialier.is_valid():
            user.set_password(new_password)
            user.save()
        
        subject = "Zero To Hero Reset Password"

        body = f"The Updated Password for Zero To Hero Login of User '{register_user.first().name}' is {new_password}"
            
        send_email(to_email=email_address, body=body, subject=subject)

        return Response(data=data, status=status.HTTP_200_OK)

class WebUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RegisterUserSerializer
    queryset = RegisterUser.objects.all()
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        return self.queryset.filter(is_active=True, role__login_mode='web')

    def get_create_user(self, email, password, name):
        data = {
            'email': email,
            'password': password,
            'name': name,
        }

        user_serializer = UserSerializer(data=data)

        if user_serializer.is_valid():
            user_serializer.save()
            return True
        
        return False

    def generate_new_password(self, name, dob):
        dob_replace = str(dob).replace('-', '')
        return name.replace(" ", "").lower()[:4] + dob_replace
    
    def get_update_user_role(self, email):
        user = Z2HUser.objects.filter(email=email).first()
        register_user = RegisterUser.objects.filter(user=user).first()
        role = Role.objects.filter(id=register_user.role.id).first()

        Z2HUserRoles.objects.create(user_uid=user.uid, role_uid=role.uid)

        return True

    def create(self, request, *args, **kwargs):
        data = {
            'status': 'success',
            'message': 'User Created Successfully!!!',
        }

        request_data = request.data

        check_user_exists = Z2HUser.objects.filter(email=request_data['user_email']).exists()
        if check_user_exists:
            data['status'] = "user_exists"
            data['message'] = "User Already Exists!!!"
            return Response(data=data, status=status.HTTP_200_OK)

        serializer = RegisterUserSerializer(data=request_data, context={'request': request})

        if serializer.is_valid():
            password = self.generate_new_password(request_data['name'], request_data['date_of_birth'])
            create_user = self.get_create_user(request_data['user_email'], password, request_data['name'])
            if create_user:
                serializer.save()
                self.get_update_user_role(request_data['user_email'])
                return Response(data=data, status=status.HTTP_201_CREATED)

        data['status'] = "error"
        data['message'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['GET', ], url_path='registered_users', url_name='registered-users')
    def get_registered_users(self, request, *args, **kwargs):
        customers = Z2HCustomers.objects.all().values_list('user', flat=True)

        register_user = RegisterUser.objects.exclude(
            Q(user__id__in=list(customers))
        ).filter(is_active=True, is_admin_user=False).order_by('id')

        data = {
            "status": "success",
            "message": "Registered Users Fetched Successfully!!!",
            "data": RegisterUserDetailsSerializer(register_user, many=True).data,
        }

        return Response(data=data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['DELETE', ], url_path='delete_registered_user', url_name='delete-registered-user')
    def delete_registered_user(self, request, *args, **kwargs):
        registered_user_uid = request.data['registerUserUid']
        registered_user = RegisterUser.objects.filter(uid=registered_user_uid).first()
        if registered_user:
            registered_user.delete()

        user = registered_user.user
        user.delete()

        return Response(data={"status": "success"}, status=status.HTTP_200_OK)

class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Z2HCustomers.objects.all()
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_paginationData(self, queryset, page="1", rowsPerPage="10"):
        paginator = Paginator(queryset, rowsPerPage)
        page_obj = paginator.get_page(page)
        data = {
            "data": page_obj.object_list,
            "total_page_count":round(queryset.count()/int(rowsPerPage)),
        }
        return data
    
    def get_queryset(self):
        queryset = self.queryset.filter(is_active=True).order_by('id')
        
        first_record = queryset.first()
        if first_record:
            queryset = queryset.exclude(id=first_record.id)

        return queryset
    
    def list(self, request, *args, **kwargs): 
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        page = self.request.query_params.get('page', None)
        rowsPerPage = self.request.query_params.get('rowsPerPage', None)

        pagination_data = self.get_paginationData(queryset, page=page, rowsPerPage=rowsPerPage)
        pagination_data['data'] = self.get_serializer(pagination_data['data'], many=True).data
        return Response(pagination_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET', ], url_path='customer_details', url_name='customer-details')
    def get_customer_details(self, request, *args, **kwargs):
        customer_uid = request.query_params.get('customer_uid', None)
        page = request.query_params.get('page', None)
        row_per_page = request.query_params.get('rowPerPage', None)
        
        if not customer_uid:
            data = {
                "status": "Error",
                "message": "Customer UID is required!!!"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        customer = Z2HCustomers.objects.filter(uid=customer_uid).first()

        first_level_customers = Z2HCustomers.objects.filter(referrer=customer)
        first_level_customers_data = CustomerSerializer(first_level_customers, many=True).data

        second_level_customers = Z2HCustomers.objects.filter(referrer__in=first_level_customers)
        second_level_customers_data = CustomerSerializer(second_level_customers, many=True).data

        third_level_customers = Z2HCustomers.objects.filter(referrer__in=second_level_customers)
        third_level_customers_data = CustomerSerializer(third_level_customers, many=True).data

        fourth_level_customers = Z2HCustomers.objects.filter(referrer__in=third_level_customers)
        fourth_level_customers_data = CustomerSerializer(fourth_level_customers, many=True).data

        data = {
            "customer": CustomerSerializer(customer).data,
            "first_level_customers": first_level_customers_data,
            "second_level_customers": second_level_customers_data,
            "third_level_customers": third_level_customers_data,
            "fourth_level_customers": fourth_level_customers_data,
        }

        return Response(data=data, status=status.HTTP_200_OK)
    
    def get_level_one_customers_not_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_not_got_paid_for_level_one_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_one_completed_date__gte=commission_from_date) & Q(level_one_completed_date__lte=commission_to_date)
        )

        customers_not_got_paid_for_level_one_completion = customers_not_got_paid_for_level_one_completion_within_dates.filter(
            Q(is_level_one_completed=True) & Q(is_level_one_commission_paid=False)
        )

        return customers_not_got_paid_for_level_one_completion
    
    def get_level_one_customers_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_got_paid_for_level_one_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_one_completed_date__gte=commission_from_date) & Q(level_one_completed_date__lte=commission_to_date)
        )

        customers_got_paid_for_level_one_completion = customers_got_paid_for_level_one_completion_within_dates.filter(
            Q(is_level_one_completed=True) & Q(is_level_one_commission_paid=True)
        )

        return customers_got_paid_for_level_one_completion
    
    def get_level_one_customers_commission(self, commission_from_date, commission_to_date):
        customers_for_level_one_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_one_completed_date__gte=commission_from_date) & Q(level_one_completed_date__lte=commission_to_date)
        )

        customers_for_level_one_completion = customers_for_level_one_completion_within_dates.filter(
            Q(is_level_one_completed=True)
        )

        return customers_for_level_one_completion
    
    def get_level_one_customers_with_issue_in_payments(self, commission_from_date, commission_to_date):
        customers_for_level_one_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_one_completed_date__gte=commission_from_date) & Q(level_one_completed_date__lte=commission_to_date)
        )

        customers_for_level_one_completion = customers_for_level_one_completion_within_dates.filter(
            Q(is_level_one_completed=True) & Q(is_level_one_payment_issue=True)
        )

        return customers_for_level_one_completion
    
    def get_level_two_customers_not_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_not_got_paid_for_level_two_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_two_completed_date__gte=commission_from_date) & Q(level_two_completed_date__lte=commission_to_date)
        )

        customers_not_got_paid_for_level_two_completion = customers_not_got_paid_for_level_two_completion_within_dates.filter(
            Q(is_level_two_completed=True) & Q(is_level_two_commission_paid=False)
        )

        return customers_not_got_paid_for_level_two_completion
    
    def get_level_two_customers_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_got_paid_for_level_two_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_two_completed_date__gte=commission_from_date) & Q(level_two_completed_date__lte=commission_to_date)
        )

        customers_got_paid_for_level_two_completion = customers_got_paid_for_level_two_completion_within_dates.filter(
            Q(is_level_two_completed=True) & Q(is_level_two_commission_paid=True)
        )

        return customers_got_paid_for_level_two_completion
    
    def get_level_two_customers_commission(self, commission_from_date, commission_to_date):
        customers_for_level_two_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_two_completed_date__gte=commission_from_date) & Q(level_two_completed_date__lte=commission_to_date)
        )

        customers_for_level_two_completion = customers_for_level_two_completion_within_dates.filter(
            Q(is_level_two_completed=True)
        )

        return customers_for_level_two_completion
    
    def get_level_two_customers_with_issue_in_payments(self, commission_from_date, commission_to_date):
        customers_for_level_two_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_two_completed_date__gte=commission_from_date) & Q(level_two_completed_date__lte=commission_to_date)
        )

        customers_for_level_two_completion = customers_for_level_two_completion_within_dates.filter(
            Q(is_level_two_completed=True) & Q(is_level_two_payment_issue=True)
        )

        return customers_for_level_two_completion
    
    def get_level_three_customers_not_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_not_got_paid_for_level_three_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_three_completed_date__gte=commission_from_date) & Q(level_three_completed_date__lte=commission_to_date)
        )

        customers_not_got_paid_for_level_three_completion = customers_not_got_paid_for_level_three_completion_within_dates.filter(
            Q(is_level_three_completed=True) & Q(is_level_three_commission_paid=False)
        )

        return customers_not_got_paid_for_level_three_completion
    
    def get_level_three_customers_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_got_paid_for_level_three_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_three_completed_date__gte=commission_from_date) & Q(level_three_completed_date__lte=commission_to_date)
        )

        customers_got_paid_for_level_three_completion = customers_got_paid_for_level_three_completion_within_dates.filter(
            Q(is_level_three_completed=True) & Q(is_level_three_commission_paid=True)
        )

        return customers_got_paid_for_level_three_completion
    
    def get_level_three_customers_commission(self, commission_from_date, commission_to_date):
        customers_for_level_three_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_three_completed_date__gte=commission_from_date) & Q(level_three_completed_date__lte=commission_to_date)
        )

        customers_for_level_three_completion = customers_for_level_three_completion_within_dates.filter(
            Q(is_level_three_completed=True)
        )

        return customers_for_level_three_completion
    
    def get_level_three_customers_with_issue_in_payments(self, commission_from_date, commission_to_date):
        customers_for_level_three_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_three_completed_date__gte=commission_from_date) & Q(level_three_completed_date__lte=commission_to_date)
        )

        customers_for_level_three_completion = customers_for_level_three_completion_within_dates.filter(
            Q(is_level_three_completed=True) & Q(is_level_three_payment_issue=True)
        )

        return customers_for_level_three_completion
    
    def get_level_four_customers_not_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_not_got_paid_for_level_four_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_four_completed_date__gte=commission_from_date) & Q(level_four_completed_date__lte=commission_to_date)
        )

        customers_not_got_paid_for_level_four_completion = customers_not_got_paid_for_level_four_completion_within_dates.filter(
            Q(is_level_four_completed=True) & Q(is_level_four_commission_paid=False)
        )

        return customers_not_got_paid_for_level_four_completion
    
    def get_level_four_customers_got_paid_commission(self, commission_from_date, commission_to_date):
        customers_got_paid_for_level_four_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_four_completed_date__gte=commission_from_date) & Q(level_four_completed_date__lte=commission_to_date)
        )

        customers_got_paid_for_level_four_completion = customers_got_paid_for_level_four_completion_within_dates.filter(
            Q(is_level_four_completed=True) & Q(is_level_four_commission_paid=True)
        )

        return customers_got_paid_for_level_four_completion
    
    def get_level_four_customers_commission(self, commission_from_date, commission_to_date):
        customers_for_level_four_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_four_completed_date__gte=commission_from_date) & Q(level_four_completed_date__lte=commission_to_date)
        )

        customers_for_level_four_completion = customers_for_level_four_completion_within_dates.filter(
            Q(is_level_four_completed=True)
        )

        return customers_for_level_four_completion
    
    def get_level_four_customers_with_issue_in_payments(self, commission_from_date, commission_to_date):
        customers_for_level_four_completion_within_dates = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(level_four_completed_date__gte=commission_from_date) & Q(level_four_completed_date__lte=commission_to_date)
        )

        customers_for_level_four_completion = customers_for_level_four_completion_within_dates.filter(
            Q(is_level_four_completed=True) & Q(is_level_four_payment_issue=True)
        )

        return customers_for_level_four_completion
    
    def get_all_customers_not_got_paid_commission(self, commission_from_date, commission_to_date):
        first_level = self.get_level_one_customers_not_got_paid_commission(
            commission_from_date, commission_to_date
        )

        second_level = self.get_level_two_customers_not_got_paid_commission(
            commission_from_date, commission_to_date
        )

        third_level = self.get_level_three_customers_not_got_paid_commission(
            commission_from_date, commission_to_date
        )

        fourth_level = self.get_level_four_customers_not_got_paid_commission(
            commission_from_date, commission_to_date
        )

        commission_queryset = first_level | second_level | third_level | fourth_level
        
        return commission_queryset
    
    def get_all_customers_got_paid_commission(self, commission_from_date, commission_to_date):
        first_level = self.get_level_one_customers_got_paid_commission(
            commission_from_date, commission_to_date
        )

        second_level = self.get_level_two_customers_got_paid_commission(
            commission_from_date, commission_to_date
        )

        third_level = self.get_level_three_customers_got_paid_commission(
            commission_from_date, commission_to_date
        )

        fourth_level = self.get_level_four_customers_got_paid_commission(
            commission_from_date, commission_to_date
        )

        commission_queryset = first_level | second_level | third_level | fourth_level

        return commission_queryset
    
    def get_all_level_customers_commission(self, commission_from_date, commission_to_date):
        first_level = self.get_level_one_customers_commission(
            commission_from_date, commission_to_date
        )

        second_level = self.get_level_two_customers_commission(
            commission_from_date, commission_to_date
        )

        third_level = self.get_level_three_customers_commission(
            commission_from_date, commission_to_date
        )

        fourth_level = self.get_level_four_customers_commission(
            commission_from_date, commission_to_date
        )

        commission_queryset = first_level | second_level | third_level | fourth_level

        return commission_queryset
    
    def get_all_customers_with_issue_in_payments(self, commission_from_date, commission_to_date):
        first_level = self.get_level_one_customers_with_issue_in_payments(
            commission_from_date, commission_to_date
        )

        second_level = self.get_level_two_customers_with_issue_in_payments(
            commission_from_date, commission_to_date
        )

        third_level = self.get_level_three_customers_with_issue_in_payments(
            commission_from_date, commission_to_date
        )

        fourth_level = self.get_level_four_customers_with_issue_in_payments(
            commission_from_date, commission_to_date
        )

        commission_queryset = first_level | second_level | third_level | fourth_level

        return commission_queryset
    
    def get_queryset_for_unpaid_commission_status(self, commission_level, commission_from_date, commission_to_date):
        if commission_level == 'One':
            commission_queryset = self.get_level_one_customers_not_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Two':
            commission_queryset = self.get_level_two_customers_not_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Three':
            commission_queryset = self.get_level_three_customers_not_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Four':
            commission_queryset = self.get_level_four_customers_not_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'All':
            commission_queryset = self.get_all_customers_not_got_paid_commission(
                commission_from_date, commission_to_date
            )

        return commission_queryset
    
    def get_queryset_for_paid_commission_status(self, commission_level, commission_from_date, commission_to_date):
        if commission_level == 'One':
            commission_queryset = self.get_level_one_customers_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Two':
            commission_queryset = self.get_level_two_customers_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Three':
            commission_queryset = self.get_level_three_customers_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Four':
            commission_queryset = self.get_level_four_customers_got_paid_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'All':
            commission_queryset = self.get_all_customers_got_paid_commission(
                commission_from_date, commission_to_date
            )

        return commission_queryset
    
    def get_queryset_for_all_commission_status(self, commission_level, commission_from_date, commission_to_date):
        if commission_level == 'One':
            commission_queryset = self.get_level_one_customers_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Two':
            commission_queryset = self.get_level_two_customers_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Three':
            commission_queryset = self.get_level_three_customers_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Four':
            commission_queryset = self.get_level_four_customers_commission(
                commission_from_date, commission_to_date
            )

        if commission_level == 'All':
            commission_queryset = self.get_all_level_customers_commission(
                commission_from_date, commission_to_date
            )

        return commission_queryset
    
    def get_queryset_for_issue_with_payments(self, commission_level, commission_from_date, commission_to_date):
        if commission_level == 'One':
            commission_queryset = self.get_level_one_customers_with_issue_in_payments(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Two':
            commission_queryset = self.get_level_two_customers_with_issue_in_payments(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Three':
            commission_queryset = self.get_level_three_customers_with_issue_in_payments(
                commission_from_date, commission_to_date
            )

        if commission_level == 'Four':
            commission_queryset = self.get_level_four_customers_with_issue_in_payments(
                commission_from_date, commission_to_date
            )

        if commission_level == 'All':
            commission_queryset = self.get_all_customers_with_issue_in_payments(
                commission_from_date, commission_to_date
            )

        return commission_queryset
    
    @action(detail=False, methods=['GET', ], url_path="commission_details", url_name="commission-details")
    def get_commission_details(self, request, *args, **kwargs):
        commission_from_date = request.query_params.get('commission_from_date', None)
        commission_to_date = request.query_params.get('commission_to_date', None)
        commission_status = request.query_params.get('commission_status', None)
        commission_level = request.query_params.get('commission_level', None)
        
        unpaid_status = 'Yet to be paid'
        paid_status = 'Paid'
        payment_issue = 'Issue with payments'
        all_status = 'All'

        if commission_from_date:
            commission_from_date = timezone.make_aware(
                timezone.datetime.combine(parse_date(commission_from_date), timezone.datetime.min.time())
            )
        if commission_to_date:
            commission_to_date = timezone.make_aware(
                timezone.datetime.combine(parse_date(commission_to_date), timezone.datetime.max.time())
            )

        if commission_status == unpaid_status:
            commission_queryset = self.get_queryset_for_unpaid_commission_status(
                commission_level, commission_from_date, commission_to_date
            )

        if commission_status == paid_status:
            commission_queryset = self.get_queryset_for_paid_commission_status(
                commission_level, commission_from_date, commission_to_date
            )

        if commission_status == all_status:
            commission_queryset = self.get_queryset_for_all_commission_status(
                commission_level, commission_from_date, commission_to_date
            )

        if commission_status == payment_issue:
            commission_queryset = self.get_queryset_for_issue_with_payments(
                commission_level, commission_from_date, commission_to_date
            )

        commission_queryset_ordered = commission_queryset.order_by('id')

        commission_data = Z2HCommissionSerializer(commission_queryset_ordered, many=True, context={'request': request}).data

        data = {
            "status": "success",
            "message": "Commission Details Fetched Successfully!!!",
            "commissions": commission_data,
        }

        return Response(data=data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['PATCH', ], url_path="update_commission_details", url_name="update-commission-details")
    def update_commission_details(self, request, *args, **kwargs):
        commission_level = request.data["commissionLevel"]
        commission_pay_date = request.data["commissionPayDate"]
        commission_status = request.data["commissionStatus"]
        comments = request.data["comments"]
        customer_number = request.data["customerNumber"]

        customer = Z2HCustomers.objects.get(customer_number=customer_number)

        if commission_level == "One":
            customer.level_one_commission_paid_date = commission_pay_date
            customer.level_one_commission_details["comments"] = comments
        elif commission_level == "Two":
            customer.level_two_commission_paid_date = commission_pay_date
            customer.level_two_commission_details["comments"] = comments
        elif commission_level == "Three":
            customer.level_three_commission_paid_date = commission_pay_date
            customer.level_three_commission_details["comments"] = comments
        elif commission_level == "Four":
            customer.level_four_commission_paid_date = commission_pay_date
            customer.level_four_commission_details["comments"] = comments

        if commission_status == "paymentIssue":
            if commission_level == "One":
                customer.is_level_one_payment_issue = True
            elif commission_level == "Two":
                customer.is_level_two_payment_issue = True
            elif commission_level == "Three":
                customer.is_level_three_payment_issue = True
            elif commission_level == "Four":
                customer.is_level_four_payment_issue = True
        elif commission_status == "paid":
            if commission_level == "One":
                customer.is_level_one_commission_paid = True
                customer.is_level_one_payment_issue = False
            elif commission_level == "Two":
                customer.is_level_two_commission_paid = True
                customer.is_level_two_payment_issue = False
            elif commission_level == "Three":
                customer.is_level_three_commission_paid = True
                customer.is_level_three_payment_issue = False
            elif commission_level == "Four":
                customer.is_level_four_commission_paid = True
                customer.is_level_four_payment_issue = False
            
        customer.save()

        data = {
            "status": "success",
            "message": "Commission Details Updated Successfully!!!",
        }

        return Response(data=data, status=status.HTTP_200_OK)

class DashboardReportView(APIView):
    def get(self, request, *args, **kwargs):

        orders = Z2HOrders.objects.all()

        yet_to_be_couriered_orders_count = orders.filter(order_status="yet_to_be_couriered").count()
        in_transit_orders_count = orders.filter(order_status="in_transit").count()
        delivered_orders_count = orders.filter(order_status="delivered").count()
        cancelled_orders_count = orders.filter(order_status="cancelled").count()

        customers = Z2HCustomers.objects.all().values_list('user', flat=True)

        register_user_count = RegisterUser.objects.exclude(
            Q(user__id__in=list(customers))
        ).filter(is_active=True, is_admin_user=False).count()

        customers_level_one_commission_not_got_paid_count = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(is_level_one_completed=True) & Q(is_level_one_commission_paid=False)
        ).count()

        customer_level_two_commission_not_got_paid_count = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(is_level_two_completed=True) & Q(is_level_two_commission_paid=False)
        ).count()

        customer_level_three_commission_not_got_paid_count = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(is_level_three_completed=True) & Q(is_level_three_commission_paid=False)
        ).count()

        customer_level_four_commission_not_got_paid_count = Z2HCustomers.objects.exclude(is_admin_user=True).filter(
            Q(is_level_four_completed=True) & Q(is_level_four_commission_paid=False)
        ).count()

        data = {
            "yet_to_be_couriered_orders_count": yet_to_be_couriered_orders_count,
            "in_transit_orders_count": in_transit_orders_count,
            "delivered_orders_count": delivered_orders_count,
            "cancelled_orders_count": cancelled_orders_count,
            "register_user_count": register_user_count,
            "customers_level_one_commission_not_got_paid_count": customers_level_one_commission_not_got_paid_count,
            "customer_level_two_commission_not_got_paid_count": customer_level_two_commission_not_got_paid_count,
            "customer_level_three_commission_not_got_paid_count": customer_level_three_commission_not_got_paid_count,
            "customer_level_four_commission_not_got_paid_count": customer_level_four_commission_not_got_paid_count,
        }

        return Response(data=data, status=status.HTTP_200_OK)
    
class NoDownlineReportsView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        customer = Z2HCustomers.objects.exclude(is_admin_user=True).values_list('id', flat=True)

        customer_not_got_downline = Z2HCustomers.objects.exclude(
            Q(customer__id__in=list(customer)) | Q(is_admin_user=True)
        ).filter(plan_start_date__lte=timezone.now() - timedelta(days=10))

        customer_not_got_downline_data = CustomerNotGotDownlineSerializer(customer_not_got_downline, many=True).data

        return Response(data={
            "customers_not_got_downline": customer_not_got_downline_data
        }, status=status.HTTP_200_OK)


class UpdateNotificationsView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_update_user_registration_status(self, register_uid):
        RegisterUser.objects.filter(uid=register_uid).update(
            is_referrer_got_notified_for_joining=True
        )

        return True
    
    def get_update_product_purchase_status(self, customer_uid):
        Z2HCustomers.objects.filter(uid=customer_uid).update(
            is_referrer_got_notified_for_joined_level_one=True
        )

        return True
    
    def get_update_level_completion_status(self, customer_uid, level):
        if level == "one":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_one_completion=True
            )
        elif level == "two":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_two_completion=True
            )
        elif level == "three":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_three_completion=True
            )
        elif level == "four":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_four_completion=True
            )

        return True
    
    def get_update_commisison_paid_status(self, customer_uid, level):
        if level == "one":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_one_commission_paid=True
            )
        elif level == "two":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_two_commission_paid=True
            )
        elif level == "three":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_three_commission_paid=True
            )
        elif level == "four":
            Z2HCustomers.objects.filter(uid=customer_uid).update(
                is_user_got_notified_for_level_four_commission_paid=True
            )

        return True

    def validate_inputs(self, notification_type, data, register_uid, customer_uid, level):
        
        if notification_type not in ["user_registration", "product_purchase", "level_completion", "commission_payment"]:
            data["message"] = (
                "Notification type must be like user_registration, product_purchase, level_completion or commission_payment. Invalid Notification Type!!!"
            )
            return data, False
        
        elif notification_type == "user_registration" and not register_uid:
            data["message"] = "Register Uid Not Found!!!"
            return data, False

        elif notification_type and not customer_uid:
            data["message"] = "Customer Uid Not Found!!!"
            return data, False
        
        elif notification_type in ["level_completion", "commission_payment"] and not level:
            data["message"] = "Level Not Found!!!"
            return data, False
        
        elif notification_type in ["level_completion", "commission_payment"] and level not in ["one", "two", "three", "four"]:
            data["message"] = "Level must be like one, two, three or four. Invalid level!!!"
            return data, False

        return data, True

    def put(self, request, *args, **kwargs):
        notification_type = request.data.get("notificationType", None)
        register_uid = request.data.get("registerUid", None)
        customer_uid = request.data.get("customerUid", None)
        level = request.data.get("level", None)

        data = {
            "status": "Error"
        }

        success_response = status.HTTP_200_OK
        error_response = status.HTTP_400_BAD_REQUEST

        data, validation_status = self.validate_inputs(notification_type, data, register_uid, customer_uid, level)

        if not validation_status:
            return Response(data=data, status=error_response)
        
        if notification_type == "user_registration" and register_uid:
            self.get_update_user_registration_status(register_uid)

        if notification_type == "product_purchase" and customer_uid:
            self.get_update_product_purchase_status(customer_uid)

        if notification_type == "level_completion" and customer_uid and level:
            self.get_update_level_completion_status(customer_uid, level)

        if notification_type == "commission_payment" and customer_uid and level:
            self.get_update_commisison_paid_status(customer_uid, level)

        data["status"] = "Success"
        data["message"] = "Notification Updated Successfully!!!"

        return Response(data=data, status=success_response)

