from django.db import models
# Create your models here.

"""
Небольшая кофейня в бизнес-центре. В ТГ боте кофейни сегодняшнее меню (кофе, сахар (по необхолдимости), сладости).
Сотрудники бизнес-центра смотрит меню в ТГ боте выбирает и делает заказ.
В комментариях пишет к какому времени готовить заказ.
Оплата как на месте так и через ТГ бота.  
"""
# 15-48 -> 16-10
# Poetry


# class Catalog(models.Model):
#
#     name = models.CharField(max_length=100, verbose_name='Наимерование')
#
#     category_assortment = (
#         ('C', 'Coffee'),
#         ('D', 'Desert'),
#     )
#     category = models.CharField(max_length=1, choices=category_assortment, verbose_name='Категория')
#     price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', null=True, blank=True)
#
#     def __str__(self):
#         return self.name


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


class Coffee(models.Model):

    coffee = models.CharField(max_length=100, verbose_name='Кофе')
    coffee_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена кофе')

    def __str__(self):
        return self.coffee


class Desert(models.Model):

    desert = models.CharField(max_length=100, verbose_name='Десерт')
    desert_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена десерта')

    def __str__(self):
        return self.desert


class Order(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='name')
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='coffee_order')
    desert = models.ForeignKey(Desert, on_delete=models.CASCADE, related_name='desert_order', null=True, blank=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ForeignKey('Delivery', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def total_price(self):
        pass

    # sugar_choices = (
    #     ('W', 'White sugar'),
    #     ('P', 'Piece sugar'),
    #     ('B', 'Brown sugar'),
    # )
    #
    # need_sugar = models.BooleanField(Client, choices=need_a_sugar, default=False)
    # if need_sugar:
    #     sugar = models.ForeignKey(Client, related_name='sugar', on_delete=models.CASCADE)
    #     sugar_choices = models.CharField(max_length=1, choices=sugar_choices,
    #                                      verbose_name='Сахар на выбор')

#     def __str__(self):
#         return self.coffee
# #        return f'{self.order} | {self.coffee} {self.sugar_choices}'


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






