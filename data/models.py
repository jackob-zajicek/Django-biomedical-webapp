from django.db import models
from django.conf import settings

class BiomedicalDevice(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

class BiomedicalData(models.Model):
    device = models.ForeignKey(BiomedicalDevice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    data_type = models.CharField(max_length=100)
    value = models.JSONField()