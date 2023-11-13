from rest_framework import serializers

from .models import Configuration, Order
from ..accounts.serializers import UserAsCounterpartySerializer
from ..erp_data.models import ConstructionObject
from ..erp_data.serializers import CounterpartySerializer, ConstructionObjectSerializer


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        #extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}}
        extra_kwargs = {'created_by': {'read_only': True },
                        'counterparty_guid': {'read_only': True}
                        }


class OrderListSerializer(serializers.ModelSerializer):
    construction_object = serializers.SerializerMethodField()
    created_by = UserAsCounterpartySerializer()

    def get_construction_object(self, obj):
        construction_object = ConstructionObject.objects.filter(guid=obj.construction_object_guid).first()
        serializer = ConstructionObjectSerializer(construction_object)
        return serializer

    class Meta:
        model = Order
        fields = '__all__'
