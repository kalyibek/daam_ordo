from django.shortcuts import render, redirect
from django.urls import reverse
from .cart import Cart
from www.models import Food
from .forms import CartAddFoodForm


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddFoodForm(
            initial={
                'quantity': item['quantity'],
                'update': True,
            }
        )

    context = {
        'cart': cart,
    }

    return render(request, 'cart.html', context)


def cart_add(request, id):
    if request.method == 'POST':
        cart = Cart(request)
        food = Food.objects.get(id=id)
        form = CartAddFoodForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                food=food,
                quantity=cd['quantity'],
                update_quantity=cd['update'],
            )

        return redirect('cart:cart')


def cart_remove(request, id):
    cart = Cart(request)
    food = Food.objects.get(id=id)
    cart.remove(food)
    return redirect('cart:cart')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(reverse('index'))


