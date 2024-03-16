from rest_framework import permissions
from .models import RegisterUser
import uuid

class ReferrerLimitPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            uuid.UUID(request.data['referred_by'], version=4)
        except ValueError:
            return False
        
        return RegisterUser.objects.filter(referred_by__uid=request.data['referred_by']).count() < 5