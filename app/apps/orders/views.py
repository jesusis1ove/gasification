from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed, NotAuthenticated

from .serializers import ConfigurationSerializer, OrderCreateSerializer, OrderListSerializer, OrderUpdateSerializer
from .models import Configuration, Order
from .permissions import IsOrderOwnerOrReadOnly


class ConfigurationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        if self.action in ('update', 'partial_update'):
            return OrderUpdateSerializer
        return OrderCreateSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(created_by=user)

    def create(self, request, *args, **kwargs):
        counterparty = request.user.get_counterparty_guid()
        if counterparty is None:
            return Response({'detail': 'counterparty is None'}, status.HTTP_400_BAD_REQUEST)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user,
                            counterparty_guid=counterparty)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, url_path='accept', methods=['path', 'put'], permission_classes=[IsAdminUser])
    def accept(self, request, pk):
        instance = self.get_object()
        instance.accept()
        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(detail=True, url_path='cancel', methods=['path', 'put'],
            permission_classes=[IsAdminUser | IsOrderOwnerOrReadOnly])
    def cancel(self, request, pk):
        instance = self.get_object()
        instance.cancel()
        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(detail=True, url_path='on-confirm', methods=['path', 'put'], permission_classes=[IsAdminUser])
    def on_confirm(self, request, pk):
        date_on_confirm = request.data.get('date_confirm')
        instance = self.get_object()
        instance.on_confirm(date_on_confirm)
        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(detail=True, url_path='confirm', methods=['path', 'put'], permission_classes=[IsOrderOwnerOrReadOnly])
    def confirm(self, request, pk):
        print('11111111111111 CONFIRM')
        instance = self.get_object()
        if instance.status == 'on_confirm':
            instance.confirm()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, 'detail': PermissionDenied.default_detail},
                        status=PermissionDenied.status_code)

    @action(detail=True, url_path='decline', methods=['patch', 'put'], permission_classes=[IsOrderOwnerOrReadOnly])
    def decline(self, request, pk):
        instance = self.get_object()
        if instance.status == 'on_confirm':
            instance.decline()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, 'detail': PermissionDenied.default_detail},
                        status=PermissionDenied.status_code)
