from django.contrib import admin
from . import models


admin.site.register(models.FoodType)
admin.site.register(models.Food)
