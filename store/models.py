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

    def __str__(self):
        return self.email