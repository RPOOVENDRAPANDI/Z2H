from django.urls import path
from rest_framework import routers
from apps.user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('login/', views.UserLoginView.as_view(), name="token"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('update_password/', views.UpdatePasswordView.as_view(), name="update-password"),
    path('me/', views.ManageUserView.as_view(), name="me"),
    path('register/', views.RegisterUserView.as_view(), name="register-user"),
    path('users_list/', views.ListUsersView.as_view(), name="users-list"),
    path('validate_referrer/', views.ValidateReferrerView.as_view(), name="validate-referrer"),
]