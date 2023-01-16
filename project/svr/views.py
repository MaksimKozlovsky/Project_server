from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
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

#            client = Client.objects.filter(client_name=order_data.pop("client_name")).first()

            client = Client.objects.filter(client_name=order_data.get("client_name")).first() or \
                     Client.objects.create(client_name=order_data.pop('client_name'))

            order = Order.objects.create(client_name=client, **order_data)
            extras = [
                Extra.objects.create(order=order, position_id=position_data["position_id"], qty=position_data["qty"])
                # Extra.objects.create(order=order, position_id=position_data["position_id"],
                #                      position=position_data["position_name"], qty=position_data["qty"])
                for position_data in positions_data
            ]
            order.extra_set.set(extras)
            return Response(self.serializer_class(order).data)

        return Response(serializer.errors)


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializers

