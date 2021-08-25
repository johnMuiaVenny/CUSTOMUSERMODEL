from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CUSTOMACCOUNTMANAGER(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, user_type, password, **other_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, last_name=last_name, first_name=first_name, user_type=user_type, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, user_type, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("is_staff=True for SuperUser!")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser=True for SuperUser!")

        return self.create_user(email, username, first_name, last_name, user_type, password, **other_fields)



class NEWUSER(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(blank=True, max_length=200)
    last_name = models.CharField(blank=True, max_length=200)
    user_type = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(blank=True, max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CUSTOMACCOUNTMANAGER()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type']

    def __str__(self):
        return self.username
