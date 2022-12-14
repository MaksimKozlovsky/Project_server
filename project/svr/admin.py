from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import messages

from svr.models import Client, Order, Comment, Delivery, Catalog, Extra


# Register your models here.

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_status',)
    list_filter = ('client_status',)
    search_fields = ('client_name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'coffee', 'desert', 'comment', 'delivery',)
    list_filter = ('client_name',)
    search_fields = ('client_name',)


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('order', 'catalog', 'qty')
    list_filter = ('order',)
    search_fields = ('order',)


# @admin.register(Coffee)
# class DesertAdmin(admin.ModelAdmin):
#     list_display = ('coffee', 'coffee_price',)
#     list_filter = ('coffee_price',)
#     search_fields = ('coffee',)
#
#
# @admin.register(Desert)
# class DesertAdmin(admin.ModelAdmin):
#     list_display = ('desert', 'desert_price',)
#     list_filter = ('desert_price',)
#     search_fields = ('desert',)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'order_created', 'order_receipt',)
    list_filter = ('order_created',)
    search_fields = ('order_created',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('delivery',)
    list_filter = ('delivery',)
