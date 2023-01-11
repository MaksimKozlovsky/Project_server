from rest_framework import serializers
from svr.models import Client, Order, Position, Extra


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'client_status', 'telegram_id', 'telegram_payload')


class PositionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('position_id', 'position_name', 'category', 'price', 'qty')


class ExtraSerializers(serializers.ModelSerializer):
    position = serializers.CharField(source='position.position_name', read_only=True)
#    position_id = serializers.IntegerField(required=False)

    # def create(self, validated_data):
    #     return Extra.objects.create(**validated_data)

    class Meta:
        model = Extra
        fields = ('position_id', 'position', 'qty')


class OrderSerializers(serializers.ModelSerializer):
    positions = ExtraSerializers(source='extra_set', many=True)
    client_name = serializers.CharField(source='client_name.client_name')

    class Meta:
        model = Order
        fields = ('client_name', 'comment', 'delivery', 'positions')

    # def create(self, validated_data):
    #
    #     positions_data = validated_data.pop('positions')
    #     order = Order.objects.create(**validated_data)
    #     for position_data in positions_data:
    #         Extra.objects.create(order=order, **position_data)
    #     return order

# --------------------------

        # positions = validated_data.pop('positions')
        # extra_serializer = ExtraSerializers(data=positions)
        # if extra_serializer.is_valid():
        #     order = Order.objects.create(**validated_data)
        #
        #     validated_data['positions'] = positions.position_id
        #     validated_data['positions'] = positions.position_name
        #     validated_data['positions'] = positions.qty
        #
        #     # Здесь надо обработать твои позиции и посоздавать их
        #     extra_serializer.save()
        #
        #     for extra in extra_serializer.data:
        #         order.add(Extra.objects.create(**extra))
        #     #
        #
        #     return order
        #
        # return extra_serializer.errors

# --------------------

        # positions_data = validated_data.pop('positions')
        # order = Order.objects.create(**validated_data)
        #
        # for position in positions_data:
        #     position, created = Extra.objects.get_or_create(name=position['name'])
        #     order.positions.add(position)
        # return order

# --------------------

        # positions = validated_data['positions']
        #
        # extra_serializer = ExtraSerializers(data=positions)
        # if extra_serializer.is_valid():
        #     extra_serializer.save()
        # return Order.objects.create(**validated_data)

# ----------------------

        # return Order.objects.create(
        #     client_name=validated_data['client_name'],
        #     comment=validated_data['comment'],
        #     delivery=validated_data['delivery'],
        #     positions=validated_data['positions'],
        #     qty=validated_data['qty']
        # )

# ------------------------

        # obj: Order = super().create(**validated_data)
        # positions=validated_data["positions"]
        # client_name=validated_data["client_name"]
        #
        # return Order(**validated_data)

# -------------------------

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
