from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect

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
    def get_wish_count(self):
        return Wishlist.objects.filter(user=self).count()


    def __str__(self):
        return self.email   
    
   

class Category(models.Model):
    name = models.CharField(max_length = 30,unique=True)
    slug= models.SlugField(max_length = 50, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name 
 
    def get_products(self):
         return Product.objects.filter(category=self.slug)
        

class Product(models.Model):
    stock_status=    [
    ("instock", "instock"),
    ("instock", "instock"),
    ]
    name=models.CharField(max_length=100)
    slug= models.SlugField(max_length = 150, unique=True)
    sort_description=models.CharField(max_length = 300,null=True)
    description = models.TextField()
    regular_price = models.DecimalField(decimal_places=2,max_digits=10)
    sale_price = models.DecimalField(decimal_places=2,max_digits=10,default=0)
    SKU = models.CharField(max_length = 150)
    stock_status = models.CharField(max_length = 150,choices=stock_status)
    feature = models.BooleanField(default=False)
    quantity = models.IntegerField(default=10)
    imagesname = models.ImageField(upload_to='images/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name="products")
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name         
    
        
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="carts")
    is_paid = models.BooleanField(default=False)

    def get_cart_total(self): 
        price=[]
        cart_items=self.cart_items.all()
        for cart_item in cart_items:
            if cart_item.product.sale_price > 0:
                product_price=cart_item.product.sale_price*cart_item.quantity
            else:
                product_price=cart_item.product.regular_price*cart_item.quantity

            price.append(product_price)
        return sum(price)

   
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    def get_product_price(self):
        if self.product.sale_price > 0:
            product_price=self.product.sale_price*self.quantity  
        else:
            product_price=self.product.regular_price*self.quantity
        return product_price
    

    
class HomeSlider(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=100)
    price=models.FloatField()
    link=models.CharField(max_length=100)
    images = models.ImageField(upload_to='images/slider')
    # status=models.BooleanField()
    
class HomeCategory(models.Model):
    sel_categories=models.CharField(max_length=150)
    no_of_product=models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)
    

class Sale(models.Model):
    BOOL_CHOICES = ((1, 'ACTIVE'), (0, 'INACTIVE'))
    status= models.BooleanField(choices=BOOL_CHOICES)      
    saledate = models.DateTimeField()


    def __str__(self):
        return str(self.saledate.strftime('%Y-%m-%d %H:%M:%S')) 


class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



class Coupons(models.Model):
    types=[
    ("fixed", "fixed"),
    ("percent", "percent"),
    ]
    code =models.CharField(max_length=100)
    type=models.CharField(max_length=100, choices=types)
    value=models.DecimalField(decimal_places=0,max_digits=5)
    cart_value=models.DecimalField(decimal_places=0,max_digits=7)
    date_joined = models.DateTimeField(default=timezone.now)        
