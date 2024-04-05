from django.urls import path
from apps.app import views

app_name = 'plan_details'

urlpatterns = [
    path('plan_details/', views.Z2HPlanDetailsListView.as_view(), name='plan_details'),
]