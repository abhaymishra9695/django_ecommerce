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