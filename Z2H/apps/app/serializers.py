from rest_framework import serializers
from .models import (
    Z2HPlanDetails,
    Z2HProductCategories,
    Z2HProductSubCategories,
    Z2HProducts,
    Z2HProductImages,
)

class Z2HPlanDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Z2HPlanDetails
        fields = (
            'id', 'is_active', 'uid', 'name', 'level_one_amount', 'level_two_amount', 'level_three_amount', 'level_four_amount',
            'registration_fee',
        )

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