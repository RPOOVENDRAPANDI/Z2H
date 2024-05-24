from rest_framework import permissions
from .models import RegisterUser
import uuid
import os

class ReferrerLimitPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PATCH':
            return True
        
        referred_by = request.data.get('referred_by', None)
        if not referred_by:
            return False
        try:
            uuid.UUID(referred_by, version=4)
        except ValueError:
            return False
        
        return RegisterUser.objects.filter(referred_by__uid=referred_by).count() < int(os.environ["PRIMARY_LEG_COUNT"])