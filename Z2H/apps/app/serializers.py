from rest_framework import serializers
from .models import (
    Z2HPlanDetails,
    Z2HProductCategories,
    Z2HProductSubCategories,
    Z2HProducts,
    Z2HProductImages,
    Z2HOrders,
    Z2HOrderItems,
    Z2HAdvertisements,
    Z2HWebPages,
    Z2HWebPageRoles,
)
from apps.user.models import Role, RegisterUser
from datetime import datetime

class Z2HPlanDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Z2HPlanDetails
        fields = '__all__'

class Z2HProductCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Z2HProductCategories
        fields = (
            'id', 'is_active', 'uid', 'name', 'description',
        )

class Z2HProductSubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Z2HProductSubCategories
        fields = (
            'id', 'is_active', 'uid', 'name', 'description', 'category',
        )

class Z2HProductSerializer(serializers.ModelSerializer):
    product_image_urls = serializers.SerializerMethodField()
    sub_category_uid = serializers.CharField(source='sub_category.uid')
    category_uid = serializers.CharField(source='sub_category.category.uid')

    class Meta:
        model = Z2HProducts
        fields = (
            'id', 'is_active', 'uid', 'name', 'description', 'sub_category_uid', 'category_uid', 'product_image_urls', 
            'price', 'discount', 'offer_price'
        )

    def get_product_image_urls(self, obj):
        return [image.product_image_url for image in Z2HProductImages.objects.filter(product=obj, is_active=True)]
    
class Z2HOrderSerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(source='uid')
    order_date = serializers.SerializerMethodField()
    courier_date = serializers.SerializerMethodField()
    delivery_date = serializers.SerializerMethodField()
    delivery_through = serializers.SerializerMethodField()
    delivery_number = serializers.SerializerMethodField()
    delivery_address = serializers.SerializerMethodField()
    payment_mode = serializers.SerializerMethodField()
    payment_status = serializers.SerializerMethodField()
    payment_date = serializers.SerializerMethodField()
    payment_reference = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    mobile_number = serializers.SerializerMethodField()
    order_igst_amount = serializers.SerializerMethodField()
    order_status = serializers.SerializerMethodField()

    class Meta:
        model = Z2HOrders
        fields = (
            'order_id', 'order_date', 'order_cgst_amount', 'order_sgst_amount', 'order_igst_amount', 'order_gst_total_amount',
            'order_total_amount', 'order_status', 'delivery_date', 'delivery_through', 'delivery_number', 'delivery_address',
            'payment_mode', 'payment_status', 'payment_date', 'payment_reference', 'customer_name', 'mobile_number',
            'courier_date', 'delivery_date',
        )

    def get_delivery_through(self, obj):
        if not obj.delivery_details:
            return None
        return obj.delivery_details.get('delivery_through', None)
    
    def get_delivery_number(self, obj):
        if not obj.delivery_details:
            return None
        return obj.delivery_details.get('delivery_number', None)
    
    def get_delivery_address(self, obj):
        if not obj.delivery_details:
            return None
        return obj.delivery_details.get('delivery_address', None)
    
    def get_payment_mode(self, obj):
        if not obj.payment_details:
            return None
        return obj.payment_details.get('payment_mode', None)
    
    def get_payment_status(self, obj):
        if not obj.payment_details:
            return None
        return obj.payment_details.get('payment_status', None)
    
    def get_payment_date(self, obj):
        if not obj.payment_details:
            return None
        return (
            datetime.strptime(obj.payment_details['payment_date'], "%Y-%m-%d %H:%M:%S.%f%z").strftime("%d-%m-%Y") \
                if obj.payment_details.get('payment_date', None) else None
        )
    
    def get_payment_reference(self, obj):
        if not obj.payment_details:
            return None
        return obj.payment_details.get('payment_reference', None)
    
    def get_customer_name(self, obj):
        return obj.ordered_by.name
    
    def get_mobile_number(self, obj):
        return RegisterUser.objects.filter(user=obj.ordered_by).first().mobile_number
    
    def get_order_igst_amount(self, obj):
        return obj.order_igst_amount if obj.order_igst_amount else 0.00
    
    def get_order_date(self, obj):
        return obj.order_date.strftime("%d-%m-%Y") if obj.order_date else None
    
    def get_courier_date(self, obj):
        return obj.courier_date.strftime("%d-%m-%Y") if obj.courier_date else None
    
    def get_delivery_date(self, obj):
        return obj.delivery_date.strftime("%d-%m-%Y") if obj.delivery_date else None
    
    def get_order_status(self, obj):
        return obj.order_status.capitalize() if obj.order_status else None
    
class Z2HOrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(source='product.uid')
    product_name = serializers.CharField(source='product.name')

    class Meta:
        model = Z2HOrderItems
        fields = (
            'product_id', 'product_name', 'quantity', 'hsn_code', 'price', 'cgst_percentage', 'cgst_amount', 'sgst_percentage',
            'sgst_amount', 'igst_percentage', 'igst_amount', 'gst_total_amount', 'total_amount'
        )

class Z2HAdvertisementsSerializer(serializers.ModelSerializer):
    demo_urls = serializers.SerializerMethodField()

    class Meta:
        model = Z2HAdvertisements
        fields = (
            'id', 'is_active', 'uid', 'name', 'description', 'demo_urls',
        )

    def get_demo_urls(self, obj):
        return obj.data.get('demo_urls', [])
    
class Z2HWebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Z2HWebPages
        fields = '__all__'

class Z2HWebPageRolesSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()
    web_page_name = serializers.SerializerMethodField()

    class Meta:
        model = Z2HWebPageRoles
        fields = ('uid', 'role_uid', 'web_page_uid', 'role_name', 'web_page_name', 'is_active')

    def get_role_name(self, obj):
        return Role.objects.filter(uid=obj.role_uid).first().name
    
    def get_web_page_name(self, obj):
        return Z2HWebPages.objects.filter(uid=obj.web_page_uid).first().name