from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CounterpartySerializer, ConstructionObjectSerializer, OrderTypeSerializer
from .models import Counterparty, ConstructionObject, OrderType


class CounterpartyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CounterpartySerializer

    def get_queryset(self):
        queryset = Counterparty.objects.all()
        return queryset


class ConstructionObjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConstructionObjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['counterparty_guid']

    def get_queryset(self):
        queryset = ConstructionObject.objects.all()
        return queryset


class OrderTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderTypeSerializer

    def get_queryset(self):
        queryset = OrderType.objects.all()
        return queryset