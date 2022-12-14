from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import messages

from svr.models import Client, Order, Position, Extra


# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('position_name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_status',)
    list_filter = ('client_status',)
    search_fields = ('client_name',)


class Admin(admin.TabularInline):
    extra = 1
    model = Extra


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (Admin,)
    list_display = ('client_name', 'comment', 'delivery',)
    list_filter = ('client_name',)
    search_fields = ('client_name',)


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):

    list_display = ('order', 'position', 'qty')
    list_filter = ('order',)
    search_fields = ('order',)
