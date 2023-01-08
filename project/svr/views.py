from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


from svr.models import Client, Order, Position, Extra
from svr.serializers import ClientSerializer, OrderSerializers, \
    PositionSerializers, ExtraSerializers


@api_view(['GET'])
def ping(request):
    return Response({'status': 'OK'}, status=status.HTTP_200_OK)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


@api_view(['GET'])
def get_ticket(request):
    all_pos = Position.position_name.objects.all()
    serializer = PositionSerializers(all_pos, many=True)
    return Response(serializer.data)


    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         return Response(status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializers

