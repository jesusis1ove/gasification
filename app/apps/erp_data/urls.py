from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'counterparties', CounterpartyViewSet, basename='counterparties')
router.register(r'objects', ConstructionObjectViewSet, basename='constraction-objects')
router.register(r'order-types', OrderTypeViewSet, basename='order-types')

urlpatterns = router.urls