from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'user_type', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'images')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_type')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

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