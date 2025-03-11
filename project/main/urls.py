from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dishes', views.dishes, name='dishes'),
    path('orders', views.orders, name='orders'),
    path('archive_order/<int:order_id>/', views.archive_order, name='archive_order'),
]