from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


def index(request):
    foods = models.Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'index.html', context)


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
        return redirect('index')

    else:
        return render(request, 'login.html')


def sign_out(request):
    logout(request)
    return redirect('index')
