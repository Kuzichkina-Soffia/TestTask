from django import forms
from .models import Order, Dish

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']
        widgets = {
            'items': forms.CheckboxSelectMultiple,  # Выбор блюд через чекбоксы
        }

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']