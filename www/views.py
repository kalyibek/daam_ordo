from django.shortcuts import render
from . import models


def index(request):
    foods = models.Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'index.html', context)
