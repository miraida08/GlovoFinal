from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart_items', CarItemViewSet, basename='cart_items')
router.register(r'store_review', StoreReviewViewSet, basename='store_review')
router.register(r'courier_review', CourierReviewViewSet, basename='courier_review')
router.register(r'order', OrderViewSet, basename='orders')
router.register(r'courier', CourierViewSet, basename='couriers')


urlpatterns = [
    path('', include(router.urls)),
    path('store/', StoreListAPIView.as_view(), name='store_list'),
    path('store/<int:pk>/', StoreDetailAPIView.as_view(), name='store_detail'),
    path('create/', StoreCreateAPiView.as_view(), name='store_create'),
    path('create/<int:pk>/', StoreDetailUpdateDeletelAPIView.as_view(), name='store_edit'),
    path('product/', ProductCreateAPiView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailUpdateDeletelAPIView.as_view(), name='store_edit'),
    path('product_combo/', ProductComboCreateAPiView.as_view(), name='products'),
    path('product_combo/<int:pk>/', ProductComboDetailUpdateDeletelAPIView.as_view(), name='store_edit')

]