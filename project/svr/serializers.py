from rest_framework import serializers
from svr.models import Client, Order, Position, Temp


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'client_status', 'telegram_id', 'telegram_payload')


class PositionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('position_id', 'position_name', 'category', 'price')


class TempSerializers(serializers.ModelSerializer):

    class Meta:
        model = Temp
        fields = ('position_id', 'qty')


class OrderSerializers(serializers.ModelSerializer):
    positions = TempSerializers(source='temp_set', many=True)
    client_name = serializers.CharField(source='client_name.client_name')

    class Meta:
        model = Order
        fields = ('client_name', 'comment', 'delivery', 'positions')

