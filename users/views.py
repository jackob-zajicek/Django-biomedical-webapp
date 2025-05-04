from rest_framework import generics
from .models import CustomUser
from .serializers import RegisterSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

@login_required
def profile(request):
    return render(request, 'users/profile.html')