from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import authentication, permissions
from .models import (
    Z2HPlanDetails,
    Z2HProductCategories,
    Z2HProductSubCategories,
    Z2HProducts,
)
from apps.app.serializers import (
    Z2HPlanDetailsSerializer,
    Z2HProductCategoriesSerializer,
    Z2HProductSubCategoriesSerializer,
    Z2HProductSerializer,
)

# Create your views here.

class Z2HPlanDetailsListView(ListAPIView):
    queryset = Z2HPlanDetails.objects.all()
    serializer_class = Z2HPlanDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

class Z2HProductCategoriesListView(ListAPIView):
    queryset = Z2HProductCategories.objects.all()
    serializer_class = Z2HProductCategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

class Z2HProductSubCategoriesListView(ListAPIView):
    queryset = Z2HProductSubCategories.objects.all()
    serializer_class = Z2HProductSubCategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = '[0-9a-f-]{36}'

    def get_queryset(self):
        return Z2HProductSubCategories.objects.filter(category__uid=self.kwargs['product_category_uid'])
    
class Z2HProductListView(ListAPIView):
    queryset = Z2HProducts.objects.all()
    serializer_class = Z2HProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = '[0-9a-f-]{36}'

    def get_queryset(self):
        return Z2HProducts.objects.filter(sub_category__uid=self.kwargs['product_sub_category_uid'])