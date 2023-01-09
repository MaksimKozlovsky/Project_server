from rest_framework import serializers
from svr.models import Client, Order, Position, Extra


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'client_status', 'telegram_id', 'telegram_payload')


class PositionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'position_name', 'category', 'price',)


class ExtraSerializers(serializers.ModelSerializer):
    position = serializers.CharField(source='position.position_name')
#    order = serializers.CharField(source='order.id', read_only=True)

    def create(self, validated_data):
        return Extra.objects.create(**validated_data)

    class Meta:
        model = Extra
        fields = ('position', 'qty')
#        fields = ('order', 'position', 'qty')


class OrderSerializers(serializers.ModelSerializer):
    positions = ExtraSerializers(source='extra_set', many=True)
    client_name = serializers.CharField(source='client_name.client_name')

    class Meta:
        model = Order
        fields = ('client_name', 'comment', 'delivery', 'positions')

    def create(self, validated_data):

        positions = validated_data['positions']

        extra_serializer = ExtraSerializers(data=positions)
        if extra_serializer.is_valid():
            extra_serializer.save()
        return Order.objects.create(**validated_data)

        # return Order.objects.create(
        #     client_name=validated_data['client_name'],
        #     comment=validated_data['comment'],
        #     delivery=validated_data['delivery'],
        #     positions=validated_data['positions'],
        #     qty=validated_data['qty']
        # )

        # obj: Order = super().create(**validated_data)
        # positions=validated_data["positions"]
        # client_name=validated_data["client_name"]
        #
        # return Order(**validated_data)

    # def create(self, validated_data):
    #     obj: Order = super().create(validated_data)
    #     validated_data["positions"]
    #
    #     obj.extra_set.add
    #     order_list = validated_data.pop('order_list')
    #     profile_instance = Order.objects.create(**validated_data)
    #     for order in order_list:
    #         Extra.objects.create(profile_instance=profile_instance, **order)
    #     return profile_instance
