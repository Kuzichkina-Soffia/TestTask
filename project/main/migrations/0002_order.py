# Generated by Django 5.1.7 on 2025-03-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(verbose_name='Номер стола')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая стоимость')),
                ('status', models.CharField(choices=[('waiting', 'В ожидании'), ('ready', 'Готово'), ('paid', 'Оплачено')], default='waiting', max_length=10, verbose_name='Статус')),
                ('items', models.ManyToManyField(to='main.dish', verbose_name='Блюда')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
