from django.db import models
from apps.utils.models import ZeroToHeroBaseModel
from apps.user.models import Z2HUser, Z2HCustomers

# Create your models here.

class Z2HWebPages(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

class Z2HWebPageRoles(ZeroToHeroBaseModel):
    role_uid = models.CharField(max_length=64, null=False, blank=False)
    web_page_uid = models.CharField(max_length=64, null=False, blank=False)

class Z2HPlanDetails(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    level_one_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_two_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_three_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_four_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    is_level_one_flat = models.BooleanField(default=True)
    is_level_one_percentage = models.BooleanField(default=False)
    level_one_percentage_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_one_flat_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    is_level_two_flat = models.BooleanField(default=True)
    is_level_two_percentage = models.BooleanField(default=False)
    level_two_percentage_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_two_flat_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    is_level_three_flat = models.BooleanField(default=True)
    is_level_three_percentage = models.BooleanField(default=False)
    level_three_percentage_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_three_flat_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    is_level_four_flat = models.BooleanField(default=True)
    is_level_four_percentage = models.BooleanField(default=False)
    level_four_percentage_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    level_four_flat_value = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    registration_fee = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)

class Z2HAdvertisements(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    data = models.JSONField(default=dict)

class Z2HProductCategories(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category_code = models.CharField(max_length=64, null=True, blank=True)

class Z2HProductSubCategories(ZeroToHeroBaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Z2HProductCategories, on_delete=models.CASCADE, null=True, blank=True)
    sub_category_code = models.CharField(max_length=64, null=True, blank=True)

class Z2HProducts(ZeroToHeroBaseModel):
    product_code = models.CharField(max_length=64, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sub_category = models.ForeignKey(Z2HProductSubCategories, on_delete=models.CASCADE, null=True, blank=True)
    hsn_code = models.CharField(max_length=64, null=True, blank=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    discount_type = models.CharField(max_length=64, null=True, blank=True)
    discount_start_date = models.DateTimeField(null=True, blank=True)
    discount_end_date = models.DateTimeField(null=True, blank=True)
    offer_price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    plan = models.ForeignKey(Z2HPlanDetails, on_delete=models.CASCADE, null=True, blank=True)

class Z2HProductImages(ZeroToHeroBaseModel):
    product_image_url = models.CharField(max_length=256, null=True, blank=True)
    product = models.ForeignKey(Z2HProducts, on_delete=models.CASCADE, null=True, blank=True)

class Z2HOrders(ZeroToHeroBaseModel):
    ORDER_TYPE_CHOICES = (
        ('company', 'company'),
        ('customer', 'customer'),
    )
    ORDER_STATUS_CHOICES = (
        ('yet_to_be_couriered', 'Confimed by customer - Payment done- Waiting for dispatch by company'),
        ('in_transit', 'Couriered by company'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    ordered_by = models.ForeignKey(Z2HUser, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Z2HCustomers, on_delete=models.CASCADE, null=True, blank=True)
    order_number = models.CharField(max_length=64, null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    total_product_price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_cgst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_sgst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_igst_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_gst_total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_total_amount = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    order_status = models.CharField(max_length=64, null=True, blank=True, default='yet_to_be_couriered')
    order_type = models.CharField(max_length=64, null=True, blank=True, default='customer')
    courier_date = models.DateTimeField(null=True, blank=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_details = models.JSONField(default=dict, null=True, blank=True)
    payment_details = models.JSONField(default=dict, null=True, blank=True)

class Z2HOrderItems(ZeroToHeroBaseModel):
    order = models.ForeignKey(Z2HOrders, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Z2HProducts, on_delete=models.CASCADE, null=True, blank=True)
    order_item_number = models.CharField(max_length=64, null=True, blank=True)
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