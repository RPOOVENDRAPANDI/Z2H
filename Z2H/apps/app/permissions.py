from rest_framework import permissions
from apps.user.models import Z2HCustomers

class CustomerExistsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            z2h_customers = Z2HCustomers.objects.filter(user=request.user)
            if not z2h_customers.first():
                return True
            
            is_customer_completed_level = True
            for customer in z2h_customers:
                if (
                    customer.is_level_one_completed == True and
                    customer.is_level_two_completed == True and
                    customer.is_level_three_completed == True and
                    customer.is_level_four_completed == True
                ):
                    continue
                else:
                    is_customer_completed_level = False
                    break
                
            return is_customer_completed_level
                
        return False