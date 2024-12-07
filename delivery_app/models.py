from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    ROLE_CHOICES = (
        ('courier', 'courier'),
        ('client', 'client'),
        ('owner', 'owner'),
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Store(models.Model):
    store_name = models.CharField(max_length=32)
    store_description = models.TextField()
    address = models.CharField(max_length=32, )
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store_image = models.FileField(upload_to='store_image/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.store_name}'

    def get_avg_rating(self):
        ratings = self.store_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0

    def get_total_people(self):
        ratings = self.store_reviews.all()
        if ratings.exists():
            if ratings.count() > 3:
                return f'3+'
            return ratings.count()
        return 0

    def get_check_good(self):
        ratings = self.store_reviews.all()
        num = 0
        if ratings.exists():
            for i in ratings:
                if i.rating > 3:
                    num += 1
                    return f'{round((num * 100) / ratings.count())}%'
        return f'0%'




class Contact(models.Model):
    contact_info = PhoneNumberField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f'{self.store}, {self.contact_info}'


class Product(models.Model):
    product_name = models.CharField(max_length=16)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    product_image = models.ImageField(upload_to='product_image/', verbose_name='product_images',
                                      null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}, {self.store}'


class ProductCombo(models.Model):
    combo_name = models.CharField(max_length=16)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combos')
    combo_image = models.ImageField(upload_to='combo_image/')

    def __str__(self):
        return f'{self.combo_name}, {self.store}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f'{self.user}'


class CarItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product}, {self.quantity}'


class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_order')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=64)
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_order')
    created_date = models.DateTimeField(auto_now_add=True)
    ORDER_CHOICES = (
        ('ожидает обработки', 'ожидает обработки'),
        ('в процессе доставки', 'в процессе доставки'),
        ('доставлен', 'доставлен'),
        ('отменен', 'отменен')
    )
    status_orders = models.CharField(max_length=24, choices=ORDER_CHOICES, default='ожидает обработки')

    def __str__(self):
        return f'{self.client}, {self.status_orders}, {self.courier}'


class Courier(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_courier')
    STATUS_COURIER = (
        ('доступен', 'доступен'),
        ('занят', 'занят')
    )
    status_courier = models.CharField(max_length=16, choices=STATUS_COURIER, default='доступен')
    current_orders = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='current_orders')

    def __str__(self):
        return f'{self.user}, {self.status_courier}'


class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client},{self.store}, {self.rating}'


class CourierReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_review')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courier_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.courier}, {self.rating}'








