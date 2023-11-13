from rest_framework.routers import DefaultRouter

from .views import ConfigurationViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'config', ConfigurationViewSet, basename='configuration')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls
