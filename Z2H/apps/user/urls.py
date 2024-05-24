from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.user import views

app_name = 'user'

router = DefaultRouter()
router.register('web_user', views.WebUserViewSet, basename='web_user')
router.register('customer', views.CustomerViewSet, basename='customer')
urlpatterns = router.urls

urlpatterns += [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('login/', views.UserLoginView.as_view(), name="token"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('update_password/', views.UpdatePasswordView.as_view(), name="update-password"),
    path('me/', views.ManageUserView.as_view(), name="me"),
    path('register/', views.RegisterUserView.as_view(), name="register-user"),
    path('users_list/', views.ListUsersView.as_view(), name="users-list"),
    path('validate_referrer/', views.ValidateReferrerView.as_view(), name="validate-referrer"),
    path('info/', views.GetUserInfoView.as_view(), name='user-info'),
    path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('update_register_user/', views.UpdateRegisterUderDetailsView.as_view(), name='update-register-user'),
]