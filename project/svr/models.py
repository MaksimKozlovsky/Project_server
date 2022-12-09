from django.db import models
# Create your models here.

"""
Небольшая кофейня в бизнес-центре. В ТГ боте кофейни сегодняшнее меню (кофе, сахар (по необхолдимости), сладости).
Сотрудники бизнес-центра смотрит меню в ТГ боте выбирает и делает заказ.
В комментариях пишет к какому времени готовить заказ.
Оплата как на месте так и через ТГ бота.  
"""
# 15-48 -> 16-10

class Client(models.Model):

    client_status = (
        ('Silver', '1 cup of coffee'),
        ('Gold', '2 cup of coffee'),
        ('Platinum', '3 and more cup of coffee'),
    )

    client_name = models.CharField(max_length=100, related_name='client', verbose_name='Клиент')
    client_rate = models.CharField(max_length=8, choices=client_status)
    telegram_id = models.PositiveIntegerField(null=True)
    telegram_payload = models.JSONField(null=True)

    def __str__(self):
        return self.client_name


class Order(models.Model):
    Americano = 'A'
    Cappuccino = 'C'
    Latte = 'L'
    coffee_choices = [
        (Americano, 'Americano'),
        (Cappuccino, 'Cappuccino'),
        (Latte, 'Latte'),
    ]

    coffee_choices = models.CharField(max_length=1, choices=coffee_choices,
                                      related_name='coffee', verbose_name='Кофе на выбор')
    coffee = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='coffee')
    order = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='order')

    need_a_sugar = (
        ('Y', 'Yes'),
        ('N', 'No')
    )

    sugar_choices = (
        ('W', 'White sugar'),
        ('P', 'Piece sugar'),
        ('B', 'Brown sugar'),
    )

    need_sugar = models.BooleanField(Client, choices=need_a_sugar, default=False)
    if need_sugar:
        sugar = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sugar')
        sugar_choices = models.CharField(max_length=1, choices=sugar_choices,
                                         related_name='sugar', verbose_name='Сахар на выбор')

    def __str__(self):
        return f'{self.order} | {self.coffee_choices} {self.sugar_choices}'


class Desert(models.Model):
    desert_choice = (
        ('T', 'Tiramisu'),
        ('C', 'Cheesecake'),
        ('B', 'Brownie'),
    )
    desert_choices = models.CharField(max_length=1, choices=desert_choice)
    desert = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='desert')

    def __str__(self):
        return f'{self.desert} | {self.desert_choices}'


class Comments(models.Model):
    comment = models.CharField(Order, max_length=250, null=True, blank=True)
    order_created = models.DateTimeField(auto_now_add=True)
    order_receipt = models.DateTimeField(blank=True, null=True)


class Delivery(models.Model):
    delivery_choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    delivery = models.BooleanField(Client, choices=delivery_choices, default=False)
    if delivery_choices:
        delivery_address = models.CharField(max_length=150, verbose_name='Укажите этаж и кабинет',
                                            null=True, blank=True)


