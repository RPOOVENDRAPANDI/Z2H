from rest_framework import permissions
from .models import RegisterUser, Z2HCustomers
import uuid
import os

class ReferrerLimitPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PATCH', 'PUT','POST']:
            return True
        
        referred_by = request.data.get('referred_by', None)
        if not referred_by:
            return False
        
        customer = Z2HCustomers.objects.filter(customer_number=referred_by).first()

        if not customer:
            return False
        
        return RegisterUser.objects.exclude(
            is_admin_user=True
        ).filter(referred_by=customer).count() < int(os.environ["PRIMARY_LEG_COUNT"])