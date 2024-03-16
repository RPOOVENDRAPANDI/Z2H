from django.urls import path
from rest_framework import routers
from apps.user import views

app_name = 'user'

# router = routers.SimpleRouter()

# router.register(r'register', RegisterUserView, basename="register-user")

# urlpatterns = router.urls
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name="token"),
    path('me/', views.ManageUserView.as_view(), name="me"),
    path('register/', views.RegisterUserView.as_view(), name="register-user")
]