from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'user_role']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'age', 'user_role']


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class StoreListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    check_good = serializers.SerializerMethodField()

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category', 'avg_rating', 'total_people', 'check_good']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()

    def get_check_good(self, obj):
        return obj.get_check_good()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['client_order', 'products', 'delivery_address', 'status_orders', 'created_date', 'courier']


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['status_courier', 'user', 'current_orders']


class StoreReviewSerializer(serializers.ModelSerializer):
    client = UserReviewSerializer(read_only=True)
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = StoreReview
        fields = ['client', 'comment', 'rating', 'created_date']


class CourierReviewSerializer(serializers.ModelSerializer):
    client = UserReviewSerializer(read_only=True)

    class Meta:
        model = CourierReview
        fields = ['client', 'comment', 'rating', 'created_date']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'product_image']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_info']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = '__all__'


class ProductComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCombo
        fields = ['combo_name', 'combo_image', 'price', 'description']


class StoreDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    contacts = ContactSerializer(read_only=True, many=True)
    products = ProductSerializer(many=True, read_only=True)
    combos = ProductComboSerializer(many=True, read_only=True)
    store_reviews = StoreReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category', 'store_description', 'address', 'owner',
                  'contacts', 'products', 'combos', 'store_reviews']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_name', 'store_description', 'address', 'store_image', 'category', 'owner']