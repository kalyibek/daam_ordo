from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from . import models
from cart.forms import CartAddFoodForm
from cart.cart import Cart


def index(request):
    foods = models.Food.objects.all()
    types = models.FoodType.objects.all()
    drinks = models.Drink.objects.all()
    cart_form = CartAddFoodForm()
    context = {
        'foods': foods,
        'types': types,
        'drinks': drinks,
        'cart_form': cart_form,
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


def create_food_order(request):
    if request.method == 'POST':
        cart = Cart(request)

        fio = request.POST['fio']
        address = request.POST['address']
        phone = request.POST['phone']
        total_price = cart.get_total_price()

        order = models.Order.objects.create(
            fio=fio,
            address=address,
            phone=phone,
            total_price=total_price,
            status='new',
        )
        order.save()
        for item in cart:
            food = models.Food.objects.get(id=item['product'].id)
            food_order = models.OrderFood.objects.create(
                food=food,
                order=order,
                quantity=item['quantity'],
                price=item['total_price'],
            )
            food_order.save()

        cart.clear()
        return redirect(reverse('index'))

    return render(request, 'order.html')


@login_required(login_url='/login/')
def new_orders_list(request):
    orders = models.Order.objects.filter(status='new')
    context = {
        'orders': orders
    }
    return render(request, 'order_admin.html', context)


@login_required(login_url='/login/')
def accept_order(request, id):
    order = models.Order.objects.get(id=id)
    order.status = 'paid'
    order.save()
    return redirect(reverse('new_orders'))


@login_required(login_url='/login/')
def cancel_order(request, id):
    order = models.Order.objects.get(id=id)
    order.status = 'canceled'
    order.save()
    return redirect(reverse('new_orders'))


@login_required(login_url='/login/')
def order_history(request):
    new_orders = models.Order.objects.filter(status='new')
    orders = models.Order.objects.filter(Q(status='paid') | Q(status='canceled'))
    context = {
        'history': orders,
        'orders': new_orders,
    }
    return render(request, 'order_history.html', context)


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
    new_orders = models.Order.objects.filter(status='new')
    context = {
        'food_types': food_types,
        'foods': foods,
        'orders': new_orders,
    }

    return render(request, 'admin.html', context)


@login_required(login_url='/login/')
def update_food(request, id):
    food = models.Food.objects.get(id=id)
    food_types = models.FoodType.objects.all()
    new_orders = models.Order.objects.filter(status='new')
    if request.method == 'POST':
        food.name = request.POST['name']
        food.type = models.FoodType.objects.get(
            id=request.POST['type']
        )
        if request.FILES.get('image', False):
            food.image = request.FILES.get('image', False)

        food.compound = request.POST['compound']
        food.weight = request.POST['weight']
        food.price = request.POST['price']
        food.save()
        return redirect(reverse('admin'))

    context = {
        'food': food,
        'food_types': food_types,
        'orders': new_orders,
    }
    return render(request, 'food_update.html', context)


@login_required(login_url='/login/')
def delete_food(request, id):
    food = models.Food.objects.get(id=id)
    food.delete()
    return redirect(reverse('admin'))


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
