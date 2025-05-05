from django.db import models
from django.conf import settings

class BiomedicalData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    data_file = models.FileField(upload_to='medical_data/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title