from django.db import models
from apps.utils.models import ZeroToHeroBaseModel

# Create your models here.

class Z2HPlanDetails(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    level_one_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_two_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_three_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_four_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    registration_fee = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)

class Z2HProductCategories(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Z2HProductSubCategories(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Z2HProductCategories, on_delete=models.CASCADE, null=True, blank=True)

class Z2HProducts(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sub_category = models.ForeignKey(Z2HProductSubCategories, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    discount_type = models.CharField(max_length=64, null=True, blank=True)
    discount_start_date = models.DateTimeField(null=True, blank=True)
    discount_end_date = models.DateTimeField(null=True, blank=True)
    offer_price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)

class Z2HProductImages(ZeroToHeroBaseModel):
    product_image_url = models.CharField(max_length=256, null=True, blank=True)
    product = models.ForeignKey(Z2HProducts, on_delete=models.CASCADE, null=True, blank=True)