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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.created_by and not self.request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if request.data.get('status'):
            new_status = request.data.get('status')
            if instance.status != new_status:
                if new_status == 'accepted' and not self.request.user.is_staff:
                    return Response(status=status.HTTP_403_FORBIDDEN)

                print('меняем статус')
        return super().update(request, *args, **kwargs)

    @action(detail=True, url_path='accept', methods=['path', 'put'], permission_classes=[IsAdminUser])
    def set_accepted(self, request, pk):
        instance = self.get_object()
        instance.set_accepted()
        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(detail=True, url_path='confirm', methods=['path', 'put'], permission_classes=[IsOrderOwnerOrReadOnly])
    def set_accepted_by_user(self, request, pk):
        instance = self.get_object()
        if instance.status == 'on_confirm':
            instance.set_accepted()
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response({'success': False, 'detail': PermissionDenied.default_detail},
                        status=PermissionDenied.status_code)

    @action(detail=True, url_path='cancel', methods=['path', 'put'],
            permission_classes=[IsAdminUser, IsOrderOwnerOrReadOnly])
    def set_cancelled(self, request, pk):
        instance = self.get_object()
        instance.set_cancelled()
        return Response({'success': True}, status=status.HTTP_200_OK)

    @action(detail=True, url_path='on-confirm', methods=['path', 'put'], permission_classes=[IsAdminUser])
    def set_on_confirm(self, request, pk):
        date_on_confirm = request.data.get('date_confirm')
        instance = self.get_object()
        instance.set_on_confirm(date_on_confirm)
        return Response({'success': True}, status=status.HTTP_200_OK)

