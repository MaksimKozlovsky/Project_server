from django.db import models
# Create your models here.

"""
Небольшая кофейня в бизнес-центре. В ТГ боте кофейни сегодняшнее меню (кофе, сахар (по необхолдимости), сладости).
Сотрудники бизнес-центра смотрит меню в ТГ боте выбирает и делает заказ.
В комментариях пишет к какому времени готовить заказ. Возможна доставка.
Оплата как на месте так и через ТГ бота.  
"""
# 15-48 -> 16-10
# Poetry
# autocomplite


class Position(models.Model):

    position_name = models.CharField(max_length=100, verbose_name='Наимерование')

    category_assortment = (
        ('Coffee', 'Coffee'),
        ('Desert', 'Desert'),
    )
    category = models.CharField(max_length=6, choices=category_assortment, verbose_name='Категория')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.position_name}'


class Client(models.Model):

    client_st = (
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('P', 'Platinum'),
    )

    client_name = models.CharField(max_length=100, verbose_name='Клиент')
    client_status = models.CharField(max_length=1, choices=client_st, null=True, blank=True)
    telegram_id = models.PositiveIntegerField(null=True, blank=True)
    telegram_payload = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.client_name


class Order(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', related_name='name')
    positions = models.ManyToManyField(Position, through='Extra', related_name='coffee')
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ForeignKey('Delivery', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.client_name}'


class Extra(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказчик')
    position_name = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Каталог')
    qty = models.IntegerField(verbose_name='Колличество')

    def __str__(self):
        return f'{self.position_name.category} | {self.position_name.price}'

    # def total(self):
    #     return self.qty * self.position.price
    #
    # def __str__(self):
    #     return f'{self.order.client_name}' \
    #            f'{self.position.price} * {self.qty} = {self.total}'


class Comment(models.Model):
    comment = models.CharField(max_length=250, verbose_name='Коментарий к заказу')
    order_created = models.DateTimeField(auto_now_add=True)
    order_receipt = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.comment


class Delivery(models.Model):
    delivery = models.CharField(max_length=100, verbose_name='Способ доставки')

    def __str__(self):
        return self.delivery






