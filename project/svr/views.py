from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.http import JsonResponse


from svr.models import Client, Order, Position, Temp
from svr.serializers import ClientSerializer, OrderSerializers, \
    PositionSerializers, TempSerializers


@api_view(['GET'])
def ping(request):
    return Response({'status': 'OK'}, status=status.HTTP_200_OK)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            order_data = request.data
            positions_data = order_data.pop('positions')

            print(order_data)
            print(positions_data)

            client = Client.objects.get_or_create(client_name=order_data.pop('client_name'))[0]

            order = Order.objects.create(client_name=client, **order_data)
            temps = [
                Temp.objects.create(order=order, position_id=position_data["position_id"], qty=position_data["qty"])
                for position_data in positions_data
            ]
            order.temp_set.set(temps)
            return Response(self.serializer_class(order).data)

        return Response(serializer.errors)


class TempViewSet(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializers

