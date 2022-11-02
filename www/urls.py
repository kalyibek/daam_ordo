from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sign_user, name='sign_user'),
    path('logout/', views.sign_out, name='sign_out'),
    path('food/<int:id>/', views.food_sort, name='sort'),
    path('drinks/', views.drinks_list, name='drinks'),
    path('admin/', views.create_food, name='admin'),
    path('admin/<int:id>/', views.update_food, name='update_dood'),
]
