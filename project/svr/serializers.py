from rest_framework import serializers
from svr.models import Client, Order, Comment, Delivery, Catalog, Extra


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'client_status', 'telegram_id', 'telegram_payload')


# class CoffeeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         models = Coffee
#         fields = ('coffee', 'coffee_price')
#
#
# class DesertSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         models = Desert
#         fields = ('desert', 'desert_prise')


class CatalogSerializers(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ('name', 'category', 'price',)


class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('client_name', 'coffee', 'desert', 'comment', 'delivery',)


class ExtraSerializers(serializers.ModelSerializer):

    class Meta:
        model = Extra
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment', 'order_created', 'order_receipt')


class DeliverySerializers(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ('delivery',)
