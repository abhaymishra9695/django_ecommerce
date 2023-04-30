from django.contrib import admin
from .models import CustomUser
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display=['name','email','user_type','password']


admin.site.register(CustomUser,AdminUser)