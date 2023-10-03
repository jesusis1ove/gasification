from rest_framework import serializers

from .models import Counterparty, ConstructionObject, OrderType


class CounterpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields = ('id', 'counterparty_inn', 'name', 'guid')


class ConstructionObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionObject
        fields = '__all__'


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'
