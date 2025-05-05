from django.conf import settings
from django.db import models

class BiomedicalData(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='biomedical_data' 
    )
    title = models.CharField(max_length=200)
    data_file = models.FileField(upload_to='medical_data/%Y/%m/%d/')
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']  

    def __str__(self):
        return self.title