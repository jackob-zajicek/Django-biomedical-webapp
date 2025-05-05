from rest_framework.routers import DefaultRouter
from .views import DataViewSet

router = DefaultRouter()
router.register(r'data', DataViewSet)

urlpatterns = router.urls