from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from .permissions import CheckStatus, CheckOwner, CheckProductOwner


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailSerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer


class StoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


class StoreCreateAPiView(generics.CreateAPIView):
    serializer_class = StoreSerializer
    permission_classes = [CheckStatus]


class StoreDetailUpdateDeletelAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [CheckStatus, CheckOwner]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCreateAPiView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [CheckStatus]


class ProductDetailUpdateDeletelAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CheckStatus, CheckProductOwner]


class ProductComboDetailUpdateDeletelAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializer
    permission_classes = [CheckStatus, CheckProductOwner]


class ProductComboCreateAPiView(generics.CreateAPIView):
    serializer_class = ProductComboSerializer
    permission_classes = [CheckStatus]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class CourierReviewViewSet(viewsets.ModelViewSet):
    queryset = CourierReview.objects.all()
    serializer_class = CourierReviewSerializer


class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CarItemViewSet(viewsets.ModelViewSet):
    queryset = CarItem.objects.all()
    serializer_class = CartItemSerializer


class ProductComboViewSet(viewsets.ModelViewSet):
    queryset = ProductCombo.objects.all()
    serializer_class = ProductComboSerializer