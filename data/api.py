from ninja import NinjaAPI, Schema
from typing import Literal
from .models import BiomedicalData
from ninja.security import django_auth

api = NinjaAPI(auth=django_auth)

class InputData(Schema):
    value: Literal[0, 1]

@api.post("/receive", auth=None)  
def receive_data(request, data: InputData):
    if not request.user.is_authenticated:
        return {"error": "Authentication required"}

    Data.objects.create(
        user=request.user,
        value=bool(data.value)
    )
    return {"status": "success", "received_value": data.value}
    
