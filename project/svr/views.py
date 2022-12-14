from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets
from svr.models import Client, Order, Comment, Delivery, Catalog, Extra
from svr.serializers import ClientSerializer, OrderSerializers, \
    CommentSerializers, DeliverySerializers, CatalogSerializers, ExtraSerializers


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializers


# class CoffeeViewSet(viewsets.ModelViewSet):
#     queryset = Coffee.objects.all()
#     serializer_class = CoffeeSerializer
#
#
# class DesertViewSet(viewsets.ModelViewSet):
#     queryset = Desert.objects.all()
#     serializer_class = DesertSerializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializers

