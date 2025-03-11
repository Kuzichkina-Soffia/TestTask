from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Order
from django.utils import timezone
from django.db import models
from .forms import OrderForm
from .forms import OrderStatusForm


def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.calculate_total_price()  # Вычисляем общую стоимость
            return redirect('orders')
    else:
        form = OrderForm()

    # Подсчёт выручки за оплаченные заказы
    total_revenue = Order.objects.filter(status='paid').aggregate(total=models.Sum('total_price'))['total'] or 0

    return render(request, 'index.html', {'form': form, 'total_revenue': total_revenue})


def orders(request):
    query = request.GET.get('query')  # Получаем поисковый запрос
    status_filter = request.GET.get('status')  # Получаем фильтр по статусу

    orders = Order.objects.filter(archived_at__isnull=True)  # Показываем только неархивированные заказы

    if query:
        orders = orders.filter(table_number__icontains=query)  # Поиск по номеру стола
    if status_filter:
        orders = orders.filter(status=status_filter)  # Фильтр по статусу

    return render(request, 'orders.html', {'orders': orders})

# def orders(request):
#     if request.method == 'POST':
#         order_id = request.POST.get('order_id')  # Получаем ID заказа
#         order = Order.objects.get(id=order_id)
#         form = OrderStatusForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('orders')  # Обновляем страницу
#     else:
#         orders = Order.objects.all().order_by('-id')  # Сортировка по ID (новые сверху)
#
#     return render(request, 'orders.html', {'orders': orders})


def archive_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.archived_at = timezone.now()  # Устанавливаем текущее время архивации
    order.save()
    return redirect('orders')


def dishes(request):
    dishes = Dish.objects.all().order_by('name')  # Получаем все блюда из базы, Сортировка по названию
    return render(request, 'dishes.html', {'dishes': dishes})
