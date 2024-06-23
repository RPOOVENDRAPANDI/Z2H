from django.contrib import admin
from django.contrib.auth import get_user_model
from apps.user.models import (
    Role,
    Z2HCustomers,
    RegisterUser,
    Z2HUserRoles
)

User = get_user_model()

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'uid', 'email', 'name', 'is_staff', 'is_superuser', 'is_password_updated', 'is_first_login', 'is_active']

class RoleAdmin(admin.ModelAdmin):
    list_display = ['uid', 'name', 'description', 'login_mode', 'is_active']

class Z2HCustomersAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'uid', 'user', 'referrer', 'customer_number', 'is_level_one_completed', 'is_level_two_completed', 'is_level_three_completed', 
        'is_level_four_completed', 'is_admin_user', 'is_level_one_commission_paid', 'is_level_two_commission_paid', 'is_level_three_commission_paid',
        'is_level_four_commission_paid', 'is_active'
    ]

class RegisterUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'referred_by', 'user', 'name', 'mobile_number')

class Z2HUserRolesAdmin(admin.ModelAdmin):
    list_display = ('uid', 'user_uid', 'role_uid')


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Z2HCustomers, Z2HCustomersAdmin)
admin.site.register(RegisterUser, RegisterUserAdmin)
admin.site.register(Z2HUserRoles, Z2HUserRolesAdmin)