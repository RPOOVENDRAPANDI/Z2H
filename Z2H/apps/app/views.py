from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .models import (
    Z2HPlanDetails,
    Z2HProductCategories,
    Z2HProductSubCategories,
    Z2HProducts,
    Z2HOrderItems,
    Z2HAdvertisements,
)
from apps.app.serializers import (
    Z2HPlanDetailsSerializer,
    Z2HProductCategoriesSerializer,
    Z2HProductSubCategoriesSerializer,
    Z2HProductSerializer,
    Z2HOrderSerializer,
    Z2HOrderItemSerializer,
    Z2HAdvertisementsSerializer,
)

# Create your views here.

LOOKUP_REGEX = '[0-9a-f-]{36}'

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
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        return Z2HProductSubCategories.objects.filter(category__uid=self.kwargs['product_category_uid'])
    
class Z2HProductsView(ListAPIView):
    queryset = Z2HProducts.objects.all()
    serializer_class = Z2HProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        return Z2HProducts.objects.filter(sub_category__uid=self.kwargs['product_sub_category_uid'])
    
class Z2HProductsListView(ListAPIView):
    queryset = Z2HProducts.objects.all()
    serializer_class = Z2HProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Z2HProducts.objects.all()
    
class Z2HOrdersListView(ListAPIView):
    queryset = Z2HOrderItems.objects.all()
    serializer_class = Z2HOrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = LOOKUP_REGEX

    def get_queryset(self):
        return Z2HOrderItems.objects.filter(order__ordered_by=self.request.user, product__uid=self.kwargs['product_uid'])
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        order = queryset.first().order

        data = {
            "products": self.get_serializer(queryset, many=True).data,
            "order": Z2HOrderSerializer(order).data
        }

        return Response(data, status=status.HTTP_200_OK)
    
class Z2HAdVideosView(ListAPIView):
    queryset = Z2HAdvertisements.objects.all()
    serializer_class = Z2HAdvertisementsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Z2HAdvertisements.objects.filter(name='demo_video', is_active=True)
