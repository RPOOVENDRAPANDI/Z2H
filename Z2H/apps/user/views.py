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
)
from apps.user.permissions import ReferrerLimitPermission
from apps.user.models import Z2HUser, Z2HCustomers, Z2HUserRoles, Role, RegisterUser
from apps.utils.tasks import send_email
import random
import string
from rest_framework.decorators import action

LOOKUP_REGEX = '[0-9a-f-]{36}'

def generate_password(length=8):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    password = ''.join(random.choices(letters, k=length-2))
    password += random.choice(letters.upper())
    password += random.choice(digits)
    password += random.choice(special_chars)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

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

        user_info = {
            'uid': user.uid,
            'name': user.name,
            'email': user.email,
            'role': role.name,
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
            'referrer_uid': customer.uid,
            'referrer_name': referrer.name,
            'referrer_city': referrer.city,
            'referrer_town': referrer.town,
            'referrer_mobile_number': referrer.mobile_number,
            'profile_photo_path': user.profile_photo_path,
            'enable_payment': enable_payment,
            "is_existing_user": is_existing_user,
            "user_customer_uid": user_customer.uid if user_customer else None,
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

        referred_by = Z2HCustomers.objects.filter(uid=request_data.get('referred_by')).first()

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
            
            send_email(to_email=request_data['email_address'], body=body, subject=subject)

            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        
        referred_by = Z2HCustomers.objects.filter(uid=referrer_uid).first()
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
                return Response(data=data, status=status.HTTP_201_CREATED)

        data['status'] = "error"
        data['message'] = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Z2HCustomers.objects.all()
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        queryset = self.queryset.filter(is_active=True).order_by('id')
        
        first_record = queryset.first()
        if first_record:
            queryset = queryset.exclude(id=first_record.id)

        return queryset

    @action(detail=False, methods=['GET', ], url_path='customer_details', url_name='customer-details')
    def get_customer_details(self, request, *args, **kwargs):
        customer_uid = request.query_params.get('customer_uid', None)

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
