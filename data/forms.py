from django import forms
from .models import BiomedicalData

class BiomedicalDataForm(forms.ModelForm):
    class Meta:
        model = BiomedicalData
        fields = ['user', 'value']