from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
