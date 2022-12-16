from rest_framework import serializers
from svr.models import Client, Order, Comment, Delivery, Position, Extra


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'client_status', 'telegram_id', 'telegram_payload')


class PositionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('position_name', 'category', 'price',)


class ExtraSerializers(serializers.ModelSerializer):

    class Meta:
        model = Extra
        fields = ('order', 'position_name', 'qty')


class OrderSerializers(serializers.ModelSerializer):
    order_list = ExtraSerializers(source='extra_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('client_name', 'order_list', 'comment', 'delivery')

    def create(self, validated_data):
        order_list = validated_data.pop('order_list')
        profile_instance = Order.objects.create(**validated_data)
        for order in order_list:
            Extra.objects.create(user=profile_instance, **order)
        return profile_instance


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment', 'order_created', 'order_receipt')


class DeliverySerializers(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ('delivery',)

