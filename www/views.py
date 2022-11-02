from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


def index(request):
    foods = models.Food.objects.all()
    types = models.FoodType.objects.all()
    drinks = models.Drink.objects.all()
    context = {
        'foods': foods,
        'types': types,
        'drinks': drinks,
    }
    return render(request, 'index.html', context)


def food_sort(request, id):
    foods = models.Food.objects.filter(type=id)
    types = models.FoodType.objects.all()
    context = {
        'foods': foods,
        'types': types,
    }
    return render(request, 'index.html', context)


def drinks_list(request):
    drinks = models.Drink.objects.all()
    types = models.FoodType.objects.all()
    context = {
        'drinks': drinks,
        'types': types,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login/')
def create_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        compound = request.POST['compound']
        weight = request.POST['weight']
        price = request.POST['price']
        food_type = models.FoodType.objects.get(
            id=request.POST['type']
        )

        new_food = models.Food.objects.create(
            name=name,
            type=food_type,
            image=image,
            compound=compound,
            weight=weight,
            price=price,
        )
        new_food.save()
        return redirect(reverse('admin'))

    food_types = models.FoodType.objects.all()
    foods = models.Food.objects.all()
    context = {
        'food_types': food_types,
        'foods': foods,
    }

    return render(request, 'admin.html', context)


@login_required(login_url='/login/')
def update_food(request, id):
    food = models.Food.objects.get(id=id)
    food_types = models.FoodType.objects.all()
    if request.method == 'POST':
        food.name = request.POST['name']
        food.type = models.FoodType.objects.get(
            id=request.POST['type']
        )
        food.image = request.FILES['image']
        food.compound = request.POST['compound']
        food.weight = request.POST['weight']
        food.price = request.POST['price']
        food.save()
        return redirect(reverse('admin'))

    context = {
        'food': food,
        'food_types': food_types,
    }
    return render(request, 'food_update.html', context)


def sign_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is None:
            return HttpResponse('Invalid credentials.')
        login(request, user)
        return redirect('admin')

    else:
        return render(request, 'login.html')


def sign_out(request):
    logout(request)
    return redirect('index')
