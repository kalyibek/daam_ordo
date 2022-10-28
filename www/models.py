import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT), null=True)
    compound = models.CharField(max_length=500)
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
