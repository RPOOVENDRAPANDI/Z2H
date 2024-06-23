from django.contrib import admin
from apps.app.models import (
    Z2HWebPages,
    Z2HWebPageRoles,
    Z2HPlanDetails,
    Z2HAdvertisements,
    Z2HProductCategories,
    Z2HProductSubCategories,
    Z2HProducts,
    Z2HProductImages,
    Z2HOrders,
    Z2HOrderItems,
    Z2HProductsReturned
)

# Register your models here.

class Z2HWebPagesAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'description', 'is_active')

class Z2HWebPageRolesAdmin(admin.ModelAdmin):
    list_display = ('uid', 'role_uid', 'web_page_uid', 'is_active')

class Z2HPlanDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HPlanDetails._meta.get_fields() if field.name != 'z2hproducts']

class Z2HAdvertisementsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HAdvertisements._meta.get_fields()]

class Z2HProductCategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HProductCategories._meta.get_fields() if field.name != 'z2hproductsubcategories']

class Z2HProductSubCategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HProductSubCategories._meta.get_fields() if field.name != 'z2hproducts']

class Z2HProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HProducts._meta.get_fields() if field.name not in ('z2hproductimages', 'z2horderitems')]

class Z2HProductImagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HProductImages._meta.get_fields()]

class Z2HOrdersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HOrders._meta.get_fields() if field.name not in ('z2horderitems',)]

class Z2HOrderItemsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HOrderItems._meta.get_fields()]

class Z2HProductsReturnedAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Z2HProductsReturned._meta.get_fields()]

admin.site.register(Z2HWebPages, Z2HWebPagesAdmin)
admin.site.register(Z2HWebPageRoles, Z2HWebPageRolesAdmin)
admin.site.register(Z2HPlanDetails, Z2HPlanDetailsAdmin)
admin.site.register(Z2HAdvertisements, Z2HAdvertisementsAdmin)
admin.site.register(Z2HProductCategories, Z2HProductCategoriesAdmin)
admin.site.register(Z2HProductSubCategories, Z2HProductSubCategoriesAdmin)
admin.site.register(Z2HProducts, Z2HProductsAdmin)
admin.site.register(Z2HProductImages, Z2HProductImagesAdmin)
admin.site.register(Z2HOrders, Z2HOrdersAdmin)
admin.site.register(Z2HOrderItems, Z2HOrderItemsAdmin)
admin.site.register(Z2HProductsReturned, Z2HProductsReturnedAdmin)