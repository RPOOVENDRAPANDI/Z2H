from django.db import models
from apps.utils.models import ZeroToHeroBaseModel
from apps.user.models import Z2HUser

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

class Z2HOrders(ZeroToHeroBaseModel):
    ORDER_TYPE_CHOICES = (
        ('company', 'company'),
        ('customer', 'customer'),
    )
    ORDER_STATUS_CHOICES = (
        ('pending', 'Added to cart waiting for customer confirmation'),
        ('yet_to_be_couriered', 'Confimed by customer - Payment done- Waiting for dispatch by company'),
        ('couriered', 'Couriered by company'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    ordered_by = models.ForeignKey(Z2HUser, on_delete=models.CASCADE, null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    order_cgst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_sgst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_igst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_gst_total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_status = models.CharField(max_length=64, null=True, blank=True, default='pending')
    order_type = models.CharField(max_length=64, null=True, blank=True, default='customer')
    delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_details = models.JSONField(default=dict, null=True, blank=True)
    payment_details = models.JSONField(default=dict, null=True, blank=True)

class Z2HOrderItems(ZeroToHeroBaseModel):
    order = models.ForeignKey(Z2HOrders, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Z2HProducts, on_delete=models.CASCADE, null=True, blank=True)
    hsn_code = models.CharField(max_length=64, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    cgst_percentage = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    cgst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    sgst_percentage = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    sgst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    igst_percentage = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    igst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    gst_total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)