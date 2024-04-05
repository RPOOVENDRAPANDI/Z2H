from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import authentication, permissions
from .models import Z2HPlanDetails
from apps.app.serializers import Z2HPlanDetailsSerializer

# Create your views here.

class Z2HPlanDetailsListView(ListAPIView):
    queryset = Z2HPlanDetails.objects.all()
    serializer_class = Z2HPlanDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]