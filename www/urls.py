from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.sign_user, name='sign_user'),
    path('logout/', views.sign_out, name='sign_out'),
    path('food/<int:id>/', views.food_sort, name='sort'),
    path('order/', views.create_food_order, name='order'),
    path('drinks/', views.drinks_list, name='drinks'),
    path('admin/', views.create_food, name='admin'),
    path('admin/<int:id>/', views.update_food, name='update_dood'),
    path('admin/delete/<int:id>/', views.delete_food, name='delete_food'),
    path('admin/orders_list/', views.new_orders_list, name='new_orders'),
    path('admin/orders_history/', views.order_history, name='orders_history'),
    path('admin/order_accept/<int:id>/', views.accept_order, name='accept_order'),
    path('admin/order_cancel/<int:id>/', views.cancel_order, name='cancel_order'),
]
