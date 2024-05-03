from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication, permissions, status
from .models import (
    Z2HPlanDetails,
    Z2HProductCategories,
    Z2HProductSubCategories,
    Z2HProducts,
    Z2HOrders,
    Z2HOrderItems,
    Z2HAdvertisements,
    Z2HWebPages,
    Z2HWebPageRoles,
)
from apps.app.serializers import (
    Z2HPlanDetailsSerializer,
    Z2HProductCategoriesSerializer,
    Z2HProductSubCategoriesSerializer,
    Z2HProductSerializer,
    Z2HOrderSerializer,
    Z2HOrderItemSerializer,
    Z2HAdvertisementsSerializer,
    Z2HWebPageSerializer,
    Z2HWebPageRolesSerializer,
)
from apps.user.serializers import RoleSerializer
from apps.user.models import Z2HCustomers, RegisterUser, Z2HUser, Role
from apps.app.permissions import CustomerExistsPermission
from django.utils import timezone
import os

# Create your views here.

LOOKUP_REGEX = '[0-9a-f-]{36}'
PRIMARY_LEG_COUNT = int(os.environ.get('PRIMARY_LEG_COUNT'))

class Z2HPlanDetailsViewSet(ModelViewSet):
    queryset = Z2HPlanDetails.objects.all()
    serializer_class = Z2HPlanDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'

class Z2HProductCategoriesListView(ListAPIView):
    queryset = Z2HProductCategories.objects.all()
    serializer_class = Z2HProductCategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

class Z2HProductSubCategoriesListView(ListAPIView):
    queryset = Z2HProductSubCategories.objects.all()
    serializer_class = Z2HProductSubCategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        return Z2HProductSubCategories.objects.filter(category__uid=self.kwargs['product_category_uid'])
    
class Z2HProductsView(ListAPIView):
    queryset = Z2HProducts.objects.all()
    serializer_class = Z2HProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        return Z2HProducts.objects.filter(sub_category__uid=self.kwargs['product_sub_category_uid'])
    
class Z2HProductsListView(ListAPIView):
    queryset = Z2HProducts.objects.all()
    serializer_class = Z2HProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Z2HProducts.objects.all()
    
class Z2HOrdersListView(ListAPIView):
    queryset = Z2HOrderItems.objects.all()
    serializer_class = Z2HOrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        return Z2HOrderItems.objects.filter(order__ordered_by=self.request.user, product__uid=self.kwargs['product_uid'])
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        order = queryset.first().order

        data = {
            "products": self.get_serializer(queryset, many=True).data,
            "order": Z2HOrderSerializer(order).data
        }

        return Response(data, status=status.HTTP_200_OK)
    
class Z2HAdVideosView(ListAPIView):
    queryset = Z2HAdvertisements.objects.all()
    serializer_class = Z2HAdvertisementsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Z2HAdvertisements.objects.filter(name='demo_video', is_active=True)
    
class PostPaymentView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, CustomerExistsPermission]

    def check_required_key_exists(self, request_data_keys):
        required_keys = ['payment_mode', 'payment_status', 'payment_reference', 'product']
        for key in required_keys:
            if key not in request_data_keys:
                return False
        
        return True
    
    def create_order(self, request, request_data):
        payment_details = {
            "payment_date": str(timezone.now()),
            "payment_mode": request_data['payment_mode'],
            "payment_status": request_data['payment_status'],
            "payment_reference": request_data['payment_reference']
        }

        z2h_orders = Z2HOrders.objects.create(
            ordered_by=request.user,
            order_date=timezone.now(),
            order_cgst_amount=0.0,
            order_sgst_amount=0.0,
            order_total_amount=0.0,
            order_status='pending',
            order_type='customer',
            delivery_date=None,
            delivery_details=None,
            payment_details=payment_details,
        )

        return z2h_orders
    
    def create_order_details(self, request, request_data, order):

        product = Z2HProducts.objects.filter(uid=request_data['product']).first()

        cgst_percentage = 2.50
        cgst_amount = 2.50
        sgst_percentage = 2.50
        sgst_amount = 2.50
        igst_percentage = 0.00
        igst_amount = 0.00
        gst_total_amount = cgst_amount + sgst_amount + igst_amount
        price = float(product.offer_price) - cgst_amount - sgst_amount
        total_amount = price + gst_total_amount

        z2h_order_items = Z2HOrderItems.objects.create(
            order=order,
            product=product,
            hsn_code=product.hsn_code,
            quantity=1,
            price=price,
            cgst_percentage=cgst_percentage,
            cgst_amount=cgst_amount,
            sgst_percentage=sgst_percentage,
            sgst_amount=sgst_amount,
            igst_percentage=igst_percentage,
            igst_amount=igst_amount,
            gst_total_amount=gst_total_amount,
            total_amount=total_amount,
        )

        return z2h_order_items
    
    def update_order_details(self, request, order):
        z2h_order_items = Z2HOrderItems.objects.filter(order=order)

        order_cgst_amount = 0.0
        order_sgst_amount = 0.0
        order_gst_total_amount = 0.0
        order_total_amount = 0.0

        for item in z2h_order_items:
            order_cgst_amount += float(item.cgst_amount)
            order_sgst_amount += float(item.sgst_amount)
            order_gst_total_amount += float(item.gst_total_amount)
            order_total_amount += float(item.total_amount)

        Z2HOrders.objects.filter(uid=order.uid).update(
            order_cgst_amount=order_cgst_amount,
            order_sgst_amount=order_sgst_amount,
            order_gst_total_amount=order_gst_total_amount,
            order_total_amount=order_total_amount,
        )

        return True
    
    def update_customer_details(self, request):
        register_user = RegisterUser.objects.filter(user=request.user).first()
        active_plan = Z2HPlanDetails.objects.get(name='SILVER')

        Z2HCustomers.objects.create(
            user=request.user,
            referrer=register_user.referred_by,
            active_plan_uid=active_plan.uid,
            plan_start_date=timezone.now(),
        )

        return True
    
    # def update_referrer_level_one(self, z2hcustomer_referrer, z2hcustomers_under_referrer):
    #     if z2hcustomers_under_referrer.count() == PRIMARY_LEG_COUNT:
    #         z2hcustomer_referrer.is_level_one_completed = True
    #         z2hcustomer_referrer.save()

    #     return True
    
    # def update_referrer_level_two(self, z2hcustomer_referrer, z2hcustomers_under_referrer):
    #     print("Test")
    #     SECONDARY_LEG_COUNT = PRIMARY_LEG_COUNT * PRIMARY_LEG_COUNT

    #     z2hcustomers_count = 0
    #     for level_one_customer in z2hcustomers_under_referrer:
    #         z2hcustomers_count += Z2HCustomers.objects.filter(referrer=level_one_customer).count()

    #     if z2hcustomers_count == SECONDARY_LEG_COUNT:
    #         z2hcustomer_referrer.is_level_two_completed = True
    #         z2hcustomer_referrer.save()
        
    #     return True
    
    # def update_referrer_level_three(self, z2hcustomer_referrer, z2hcustomers_under_referrer):
    #     THIRD_LEG_COUNT = PRIMARY_LEG_COUNT * PRIMARY_LEG_COUNT * PRIMARY_LEG_COUNT

    #     z2hcustomers_count = 0
    #     for level_one_customer in z2hcustomers_under_referrer:
    #         for level_two_customer in Z2HCustomers.objects.filter(referrer=level_one_customer):
    #             z2hcustomers_count += Z2HCustomers.objects.filter(referrer=level_two_customer).count()

    #     if z2hcustomers_count == THIRD_LEG_COUNT:
    #         z2hcustomer_referrer.is_level_three_completed = True
    #         z2hcustomer_referrer.save()

    #     return True
    
    # def update_referrer_level_four(self, z2hcustomer_referrer, z2hcustomers_under_referrer):
    #     FOURTH_LEG_COUNT = PRIMARY_LEG_COUNT * PRIMARY_LEG_COUNT * PRIMARY_LEG_COUNT * PRIMARY_LEG_COUNT

    #     z2hcustomers_count = 0
    #     for level_one_customer in z2hcustomers_under_referrer:
    #         for level_two_customer in Z2HCustomers.objects.filter(referrer=level_one_customer):
    #             for level_three_customer in Z2HCustomers.objects.filter(referrer=level_two_customer):
    #                 z2hcustomers_count += Z2HCustomers.objects.filter(referrer=level_three_customer).count()

    #     if z2hcustomers_count == FOURTH_LEG_COUNT:
    #         z2hcustomer_referrer.is_level_four_completed = True
    #         z2hcustomer_referrer.save()
        
    #     return True
        
    def update_referrer_level(self, request):
        z2hcustomer = Z2HCustomers.objects.filter(user=request.user, is_level_four_completed=False)

        referrer = z2hcustomer.first().referrer

        z2hcustomer_referrer = Z2HCustomers.objects.filter(id=referrer.id).first()
        admin_user = Z2HUser.objects.filter(is_superuser=True).first()

        z2hcustomers_under_referrer = Z2HCustomers.objects.filter(
            referrer=z2hcustomer_referrer
        ).exclude(
            user__id=admin_user.id
        )

        if not z2hcustomer_referrer.is_level_one_completed:
            if z2hcustomers_under_referrer.count() == PRIMARY_LEG_COUNT:
                z2hcustomer_referrer.is_level_one_completed = True
                z2hcustomer_referrer.save()

    def post(self, request, *args, **kwargs):
        data = {
            'status': 'success',
            'message': 'Data Saved Successfully!!!',
        }

        request_data = request.data
        request_data_keys = request_data.keys()
        request_data_keys = list(request_data_keys)

        required_keys_exists = self.check_required_key_exists(request_data_keys)

        if not required_keys_exists:
            data['status'] = 'error'
            data['message'] = 'Required Details Not Found!!!'
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        if request_data['payment_status'] != 'success':
            data['status'] = 'error'
            data['message'] = 'Payment Failed!!!'
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        
        create_order = self.create_order(request, request_data)
        create_order.save()

        create_order_details = self.create_order_details(request, request_data, create_order)
        create_order_details.save()

        update_order_details = self.update_order_details(request, create_order)

        if update_order_details:
            self.update_customer_details(request)
            self.update_referrer_level(request)

        user_customer = Z2HCustomers.objects.filter(user=request.user, is_level_four_completed=False).first()
        data["customer_uid"] = str(user_customer.uid)

        return Response(data=data, status=status.HTTP_200_OK)
    
class Z2HWebPagesView(ListAPIView):
    queryset = Z2HWebPages.objects.all()
    serializer_class = Z2HWebPageSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        role = Role.objects.filter(login_mode='web')
        data = {
            "pages": self.get_serializer(self.get_queryset(), many=True).data,
            "roles": RoleSerializer(role, many=True).data
        }

        return Response(data, status=status.HTTP_200_OK)
    
class SaveWebUserSettingsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def update_web_page_user(self, request_data, system_role_uid, users_page_uid):
        web_page_role = None

        if request_data['users'] == True:
            user_web_page_exists = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=users_page_uid
            ).first()
            if not user_web_page_exists:
                web_page_role = Z2HWebPageRoles.objects.create(
                    role_uid=system_role_uid,
                    web_page_uid=users_page_uid
                )
            if user_web_page_exists:
                user_web_page_exists.is_active = True
                user_web_page_exists.save()

        elif request_data['users'] == False:
            web_page_role = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=users_page_uid
            ).first()
            if web_page_role:
                web_page_role.is_active = False

        if web_page_role:
            web_page_role.save()
    
    def update_web_page_products(self, request_data, system_role_uid, products_page_uid):
        web_page_role = None

        if request_data['products'] == True:
            products_web_page_exists = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=products_page_uid
            ).first()
            if not products_web_page_exists:
                web_page_role = Z2HWebPageRoles.objects.create(
                    role_uid=system_role_uid,
                    web_page_uid=products_page_uid
                )
            if products_web_page_exists:
                products_web_page_exists.is_active = True
                products_web_page_exists.save()

        elif request_data['products'] == False:
            web_page_role = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=products_page_uid
            ).first()
            if web_page_role:
                web_page_role.is_active = False

        if web_page_role:
            web_page_role.save()
    
    def update_web_page_orders(self, request_data, system_role_uid, orders_page_uid):
        web_page_role = None

        if request_data['orders'] == True:
            orders_web_page_exists = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=orders_page_uid
            ).first()
            if not orders_web_page_exists:
                web_page_role = Z2HWebPageRoles.objects.create(
                    role_uid=system_role_uid,
                    web_page_uid=orders_page_uid
                )
            if orders_web_page_exists:
                orders_web_page_exists.is_active = True
                orders_web_page_exists.save()

        elif request_data['orders'] == False:
            web_page_role = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=orders_page_uid
            ).first()
            if web_page_role:
                web_page_role.is_active = False

        if web_page_role:
            web_page_role.save()
    
    def update_web_page_customer(self, request_data, system_role_uid, customers_page_uid):
        web_page_role = None

        if request_data['customers'] == True:
            customers_web_page_exists = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=customers_page_uid
            ).first()
            if not customers_web_page_exists:
                web_page_role = Z2HWebPageRoles.objects.create(
                    role_uid=system_role_uid,
                    web_page_uid=customers_page_uid
                )
            if customers_web_page_exists:
                customers_web_page_exists.is_active = True
                customers_web_page_exists.save()

        elif request_data['customers'] == False:
            web_page_role = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=customers_page_uid
            ).first()
            if web_page_role:
                web_page_role.is_active = False

        if web_page_role:
            web_page_role.save()
    
    def update_web_page_reports(self, request_data, system_role_uid, reports_page_uid):
        web_page_role = None

        if request_data['reports'] == True:
            reports_web_page_exists = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=reports_page_uid
            ).first()
            if not reports_web_page_exists:
                web_page_role = Z2HWebPageRoles.objects.create(
                    role_uid=system_role_uid,
                    web_page_uid=reports_page_uid
                )
            if reports_web_page_exists:
                reports_web_page_exists.is_active = True
                reports_web_page_exists.save()

        elif request_data['reports'] == False:
            web_page_role = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=reports_page_uid
            ).first()
            if web_page_role:
                web_page_role.is_active = False

        if web_page_role:
            web_page_role.save()
    
    def update_web_page_settings(self, request_data, system_role_uid, settings_page_uid):
        web_page_role = None

        if request_data['settings'] == True:
            settings_web_page_exists = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=settings_page_uid
            ).first()
            if not settings_web_page_exists:
                web_page_role = Z2HWebPageRoles.objects.create(
                    role_uid=system_role_uid,
                    web_page_uid=settings_page_uid
                )
            if settings_web_page_exists:
                settings_web_page_exists.is_active = True
                settings_web_page_exists.save()

        elif request_data['settings'] == False:
            web_page_role = Z2HWebPageRoles.objects.filter(
                role_uid=system_role_uid,
                web_page_uid=settings_page_uid
            ).first()
            if web_page_role:
                web_page_role.is_active = False

        if web_page_role:
            web_page_role.save()

    def post(self, request, *args, **kwargs):
        data = {
            'status': 'success',
            'message': 'Data Saved Successfully!!!',
        }

        request_data = request.data

        system_role_uid = request_data['systemRoleUid']
        users_page = Z2HWebPages.objects.filter(name='users').first()
        products_page = Z2HWebPages.objects.filter(name='products').first()
        orders_page = Z2HWebPages.objects.filter(name='orders').first()
        customers_page = Z2HWebPages.objects.filter(name='customers').first()
        reports_page = Z2HWebPages.objects.filter(name='reports').first()
        settings_page = Z2HWebPages.objects.filter(name='settings').first()

        self.update_web_page_user(request_data, system_role_uid, users_page.uid)
        self.update_web_page_products(request_data, system_role_uid, products_page.uid)
        self.update_web_page_orders(request_data, system_role_uid, orders_page.uid)
        self.update_web_page_customer(request_data, system_role_uid, customers_page.uid)
        self.update_web_page_reports(request_data, system_role_uid, reports_page.uid)
        self.update_web_page_settings(request_data, system_role_uid, settings_page.uid)

        return Response(data=data, status=status.HTTP_200_OK)
    
class Z2HWebPageRolesView(ListAPIView):
    queryset = Z2HWebPageRoles.objects.all()
    serializer_class = Z2HWebPageRolesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]