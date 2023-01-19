from django.contrib import admin
from django.contrib.admin.options import TabularInline
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import messages

from svr.models import Client, Order, Position, Temp


# Register your models here.

class TempInLine(admin.TabularInline):
    extra = 1
    model = Temp


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    inlines = (TempInLine,)
    list_display = ('position_name', 'category', 'price',)
    list_filter = ('category',)
    search_fields = ('position_name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_status',)
    list_filter = ('client_status',)
    search_fields = ('client_name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (TempInLine,)
    list_display = ('client_name', 'comment', 'delivery',)
    list_filter = ('client_name',)
    search_fields = ('client_name',)


@admin.register(Temp)
class TempAdmin(admin.ModelAdmin):

    list_display = ('order', 'position', 'qty')
    list_filter = ('order',)
    search_fields = ('order',)
