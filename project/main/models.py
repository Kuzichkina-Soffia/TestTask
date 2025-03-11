from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.name} - {self.price} руб."

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Order(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.IntegerField(verbose_name="Номер стола")
    items = models.ManyToManyField('Dish', verbose_name="Блюда")  # Связь с таблицей Dish
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость", default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting', verbose_name="Статус")
    archived_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата архивации")

    def __str__(self):
        return f"Заказ #{self.id} (Стол {self.table_number})"

    def calculate_total_price(self):
        """Метод для вычисления общей стоимости заказа."""
        self.total_price = sum(dish.price for dish in self.items.all())
        self.save()

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
