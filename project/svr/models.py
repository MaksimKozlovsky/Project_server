from django.db import models
# Create your models here.

"""
Небольшая кофейня в бизнес-центре. В ТГ боте кофейни сегодняшнее меню (кофе, сахар (по необхолдимости), сладости).
Сотрудники бизнес-центра смотрит меню в ТГ боте выбирает и делает заказ.
В комментариях пишет к какому времени готовить заказ.
Оплата как на месте так и через ТГ бота.  
"""


class Client(models.Model):
    client_status = (
        ('Silver', '1 cup of coffee'),
        ('Gold', '2 cup of coffee'),
        ('Platinum', '3 and more cup of coffee'),
    )

    client_name = models.CharField(max_length=100, related_name='client', verbose_name='Клиент')
    client_rate = models.CharField(max_length=8, choices=client_status)

    def __str__(self):
        return self.client_name


class Coffee(models.Model):
    coffee_choices = (
        ('A', 'Americano'),
        ('C', 'Cappuccino'),
        ('L', 'Latte'),
    )

    coffee_choices = models.CharField(max_length=1, choices=coffee_choices,
                                      related_name='coffee', verbose_name='Кофе на выбор')
    coffee = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='coffee')

    def __str__(self) -> str:
        return f'{self.coffee} | {self.coffee_choices}'


class Sugar(models.Model):
    sugar_choices = (
        ('W', 'White sugar'),
        ('P', 'Piece sugar'),
        ('B', 'Brown sugar'),
    )
    sugar_choices = models.CharField(max_length=1, choices=sugar_choices,
                                     related_name='sugar', verbose_name='Сахар на выбор')
    sugar = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sugar')

    def __str__(self) -> str:
        return f'{self.sugar} | {self.sugar_choices}'


class Dessert(models.Model):
    desert_choices = (
        ('T', 'Tiramisu'),
        ('C', 'Cheesecake'),
        ('B', 'Brownie'),
    )
    desert_choices = models.CharField(max_length=1, choices=desert_choices)
    desert = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='desert')

    def __str__(self):
        return f'{self.desert} | {self.desert_choices}'


class Order(models.Model):
    order = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='order')


class Comments(models.Model):
    comment = models.CharField(max_length=250, null=True, blank=True)
    order_created = models.DateTimeField(auto_now_add=True)
    order_receipt = models.DateTimeField(blank=True, null=True)

