from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, DataViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'data', DataViewSet)

urlpatterns = router.urls