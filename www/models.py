import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    pass


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='food', null=True)
    image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT), null=True)
    compound = models.CharField(max_length=500)
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=50)
    weight = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT), null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('paid', "оплачен"),
        ('new', 'новый заказ'),
        ('canceled', 'отменен'),
    )
    fio = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=80)
    phone = PhoneNumberField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return f'{self.fio} - {self.total_price}'


class OrderFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Заказ {self.food.name} - {self.order.fio}'

