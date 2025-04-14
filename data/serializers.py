from rest_framework import serializers
from .models import BiomedicalDevice, BiomedicalData

class BiomedicalDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomedicalDevice
        fields = '__all__'

class BiomedicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomedicalData
        fields = '__all__'