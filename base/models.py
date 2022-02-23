from datetime import date

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    training_style = models.CharField(max_length=50, default='PowerLifting')
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class UserDetails(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=100, decimal_places=1, null=True, blank=True)
    weight = models.DecimalField(max_digits=100, decimal_places=1, null=True, blank=True)
    training_style = models.CharField(max_length=50, default='PowerLifting')
    dob = models.DateField(default=date.today)
    gender = models.CharField(max_length=6, default="Male")

    def __str__(self):
        return str(self.user)