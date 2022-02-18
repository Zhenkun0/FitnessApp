from datetime import date

from django.core.mail import send_mail, EmailMultiAlternatives
from django.db import models
from django.template.loader import get_template
from fitness import settings
from django.contrib.auth.models import *
from PIL import Image


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is necessary')

        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Trainee(AbstractBaseUser, PermissionsMixin):
    trainee = models.BooleanField("trainee", default=True)
    # TODO create Order class
    # trainer = models.ForeignKey(
    #     Trainer, blank=True, null=True, on_delete=models.SET_NULL
    # )
    user_name = models.CharField("user_name", max_length=255, null=False)
    first_name = models.CharField("first_name", max_length=255)
    email = models.EmailField("email", max_length=255, unique=True)
    last_name = models.CharField("last_name", max_length=255)
    height = models.DecimalField(max_digits=100, decimal_places=1, null=True, blank=True)
    weight = models.DecimalField(max_digits=100, decimal_places=1, null=True, blank=True)
    goal_setting = models.CharField(max_length=50, default='PowerLifting')
    dob = models.DateField(default=date.today)
    gender = models.CharField(max_length=6, default="Male")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name', 'height', 'weight']

    def __str__(self):
        return self.email
