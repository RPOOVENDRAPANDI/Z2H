from django.urls import path
from apps.app import views
from rest_framework.routers import DefaultRouter

app_name = 'plan_details'

router = DefaultRouter()
router.register(r'plan_details', views.Z2HPlanDetailsViewSet, basename='plan_details')
router.register(r'orders', views.Z2HOrdersViewSet, basename='orders')
router.register(r'product_categories', views.Z2HProductCategoriesViewSet, basename='product_categories')
router.register(
    r'product_sub_categories/(?P<product_category_uid>[0-9a-f-]{36})', 
    views.Z2HProductSubCategoriesViewSet, 
    basename='product_sub_categories'
)
urlpatterns = router.urls

urlpatterns += [
    path(
        r'products/<str:product_sub_category_uid>/',
        views.Z2HProductsView.as_view(),
        name="products"
    ),
    path(
        r'products_list/', views.Z2HProductsListView.as_view(), name="products_list"
    ),
    path(
        r'orders_details/<str:product_uid>/', views.Z2HOrdersListView.as_view(), name="orders_details"
    ),
    path(
        r'demo_videos/', views.Z2HAdVideosView.as_view(), name="demo_videos"
    ),
    path(
        r'update_payment/', views.PostPaymentView.as_view(), name="update_payment"
    ),
    path(
        r'web_roles_and_pages/', views.Z2HWebPagesView.as_view(), name='web_roles_and_pages'
    ),
    path(
        r'save_web_user_settings/', views.SaveWebUserSettingsView.as_view(), name='save_web_user_settings'
    ),
    path('web_user_role_page/', views.Z2HWebPageRolesView.as_view(), name='web_user_role_page'),
]