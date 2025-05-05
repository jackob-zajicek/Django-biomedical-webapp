from rest_framework import serializers
from .models import BiomedicalData

class BiomedicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiomedicalData
        fields = '__all__'