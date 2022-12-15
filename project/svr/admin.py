from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import messages

from svr.models import Client, Order, Comment, Delivery, Position, Extra


# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
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
    list_display = ('client_name', 'comment', 'delivery',)
    list_filter = ('client_name',)
    search_fields = ('client_name',)


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('order', 'position', 'qty')
    list_filter = ('order',)
    search_fields = ('order',)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'order_created', 'order_receipt',)
    list_filter = ('order_created',)
    search_fields = ('order_created',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('delivery',)
    list_filter = ('delivery',)
