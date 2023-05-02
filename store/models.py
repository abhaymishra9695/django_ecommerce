from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name=models.CharField(max_length=100)
    email = models.EmailField(_("email address"), unique=True)
    images=models.ImageField(upload_to="usersimage")
    user_type=models.CharField(max_length=5, default="USER",help_text="admin for ADMIN and user or costumer for USER")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_cart_count(self):
        return CartItem.objects.filter(cart__is_paid=False, cart__user=self).count()

    def __str__(self):
        return self.email   
    
   

class Category(models.Model):
    name = models.CharField(max_length = 30,unique=True)
    slug= models.SlugField(max_length = 50, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name 
        

class Product(models.Model):
    stock_status=    [
    ("IN", "instock"),
    ("out", "outofstock"),
    ]
    name=models.CharField(max_length=100)
    slug= models.SlugField(max_length = 150, unique=True)
    sort_description=models.CharField(max_length = 300,null=True)
    description = models.TextField()
    regular_price = models.DecimalField(decimal_places=2,max_digits=10)
    sale_price = models.DecimalField(decimal_places=2,max_digits=10, null=True)
    SKU = models.CharField(max_length = 150)
    stock_status = models.CharField(max_length = 150,choices=stock_status)
    feature = models.BooleanField(default=False)
    quantity = models.IntegerField(default=10)
    imagesname = models.CharField(max_length = 150,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name         
        
        
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="carts")
    is_paid = models.BooleanField(default=False)

    def get_cart_total(self):  # sourcery skip: for-append-to-extend, list-comprehension
        cart_items=cart_items.all()
        price=[]
        for cart_item in cart_items:
            price.append(cart_item.product.regular_price)
        return sum(price)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def get_product_price(self):
        return self.product.regular_price
  
    
    
      
        
        
        
        

        
          