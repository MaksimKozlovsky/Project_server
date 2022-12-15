from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets
from svr.models import Client, Order, Comment, Delivery, Position, Extra
from svr.serializers import ClientSerializer, OrderSerializers, \
    CommentSerializers, DeliverySerializers, PositionSerializers, ExtraSerializers


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


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

