from rest_framework import viewsets, permissions
from .models import BiomedicalData
from .serializers import BiomedicalDataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = BiomedicalData.objects.all()
    serializer_class = BiomedicalDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(device__owner=self.request.user)