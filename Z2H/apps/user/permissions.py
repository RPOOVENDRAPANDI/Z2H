from rest_framework import permissions
from .models import RegisterUser
import uuid
import os

class ReferrerLimitPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            uuid.UUID(request.data['referred_by'], version=4)
        except ValueError:
            return False
        
        return RegisterUser.objects.filter(referred_by__uid=request.data['referred_by']).count() < int(os.environ["PRIMARY_LEG_COUNT"])