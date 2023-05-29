from django.contrib import admin
from .models import *
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display=['name','email','user_type','password']
admin.site.register(CustomUser,AdminUser)

class AdminCatogary(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,AdminCatogary)


class AdminProduct(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Product,AdminProduct)


admin.site.register(Cart)
admin.site.register(CartItem)
@admin.register(HomeSlider)
class AdminSlider(admin.ModelAdmin):
    list_display=['title','subtitle','price','link','images']

@admin.register(HomeCategory)
class AdminHomeCategory(admin.ModelAdmin):
    list_display=['sel_categories','no_of_product']

@admin.register(Sale)
class AdminSale(admin.ModelAdmin):
    list_display=['saledate','status']

@admin.register(Wishlist)
class AdminSale(admin.ModelAdmin):
    list_display=['user','product']

@admin.register(Coupons)
class AdminSale(admin.ModelAdmin):
    list_display=['code','type','minimum_amount','value']