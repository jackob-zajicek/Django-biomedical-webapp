from django.db import models
from django.contrib.auth.models import User

class BiomedicalData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_file = models.FileField(upload_to='medical_data/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    data_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.data_type}"