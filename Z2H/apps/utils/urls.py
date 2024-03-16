from django.urls import path
from apps.utils import views

urlpatterns = [
    path(r'state/', views.StateView.as_view(), name='state'),
    path(r'district/<str:state_uid>/', views.DistrictView.as_view(), name='district'),
]