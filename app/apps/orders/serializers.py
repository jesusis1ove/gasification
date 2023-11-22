from rest_framework import serializers

from .models import Configuration, Order
from ..accounts.serializers import UserAsCounterpartySerializer
from ..erp_data.models import ConstructionObject
from ..erp_data.serializers import CounterpartySerializer, ConstructionObjectSerializer


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    """Создание заявки"""
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'created_by': {'read_only': True},
                        'counterparty_guid': {'read_only': True},
                        'status': {'read_only': True},
                        }


class OrderUpdateSerializer(serializers.ModelSerializer):
    """Обновление заявки"""
    class Meta:
        model = Order
        exclude = ['counterparty_guid', 'created_by', 'status']


class OrderListSerializer(serializers.ModelSerializer):
    """Список заявок"""
    construction_object = serializers.SerializerMethodField()
    counterparty = serializers.SerializerMethodField()
    created_by = UserAsCounterpartySerializer()

    def get_construction_object(self, obj):
        construction_object = ConstructionObject.objects.filter(guid=obj.construction_object_guid).first()
        serializer = ConstructionObjectSerializer(construction_object)
        return serializer.data

    def get_counterparty(selfs, obj):
        return None

    class Meta:
        model = Order
        exclude = ['counterparty_guid', 'construction_object_guid']
