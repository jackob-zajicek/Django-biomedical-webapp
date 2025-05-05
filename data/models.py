from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
    
class BiomedicalData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_file = models.FileField(upload_to='biomedical_data/')
    uploaded_at = models.DateTimeField(auto_now_add=True)