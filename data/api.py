from ninja import NinjaAPI, Schema
from .models import BiomedicalData
from ninja.security import django_auth
from ninja.errors import HttpError
import datetime
from pydantic import field_serializer
from django.views.decorators.csrf import csrf_exempt
from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            jwt_auth = JWTAuthentication()
            validated_token = jwt_auth.get_validated_token(token)
            return jwt_auth.get_user(validated_token)
        except Exception:
            return None


api = NinjaAPI(auth=JWTAuth()) 

class BiomedicalDataSchema(Schema):
    id: int
    user_id: int
    value: bool
    uploaded_at: datetime.datetime

    class Config:
        from_attributes = True

    @field_serializer('uploaded_at')
    def serialize_uploaded_at(self, v: datetime.datetime):
        return v.isoformat()

class BiomedicalDataCreateSchema(Schema):
    value: bool

@api.get("/data", response=list[BiomedicalDataSchema])
def list_data(request):
    user = request.user
    if not user.is_authenticated:
        raise HttpError(401, "Not authenticated")
    data = BiomedicalData.objects.filter(user=user).order_by('-uploaded_at')
    return data

@api.post("/data", response=BiomedicalDataSchema)
def create_data(request, data: BiomedicalDataCreateSchema):
    user = request.user
    if not user.is_authenticated:
        raise HttpError(401, "Not authenticated")
    bio_data = BiomedicalData.objects.create(user=user, value=data.value)
    return bio_data