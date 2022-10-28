from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sign_user, name='sign_user'),
    path('logout/', views.sign_out, name='sign_out'),


]
