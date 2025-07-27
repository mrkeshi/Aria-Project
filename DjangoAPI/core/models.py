from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models
from workspace_module.models import Project
from phonenumber_field.modelfields import PhoneNumberField


def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    about=models.TextField(null=True,blank=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    email = models.EmailField(unique=True) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone_number = PhoneNumberField(blank=True, null=True,verbose_name="شماره تلفن")
    current_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True,auto_now_add=True)

    objects=CustomUserManager()
    # def __str__(self):
    #     return self.email
