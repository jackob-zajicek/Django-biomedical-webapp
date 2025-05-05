from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
    
class BiomedicalData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_file = models.FileField(upload_to='biomedical_data/')
    timestamp = models.DateTimeField(auto_now_add=True)