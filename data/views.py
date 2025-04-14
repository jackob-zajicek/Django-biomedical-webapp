from rest_framework import viewsets, permissions
from .models import BiomedicalDevice, BiomedicalData
from .serializers import BiomedicalDeviceSerializer, BiomedicalDataSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = BiomedicalDevice.objects.all()
    serializer_class = BiomedicalDeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DataViewSet(viewsets.ModelViewSet):
    queryset = BiomedicalData.objects.all()
    serializer_class = BiomedicalDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(device__owner=self.request.user)