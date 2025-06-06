from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from data.models import BiomedicalData
from django.shortcuts import get_object_or_404, redirect

def index(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('users:index') 

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def data_list(request):
    user_data = BiomedicalData.objects.filter(user=request.user).order_by('-uploaded_at')
    context = {
        'user_data': user_data, 
        'user': request.user
    }
    return render(request, 'data/list.html', context)

@login_required
def upload_data(request):
    if request.method == 'POST':
        form = BiomedicalDataForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('data_list')
    else:
        form = BiomedicalDataForm()
    return render(request, 'data/upload.html', {'form': form})
    
@login_required
def data_delete(request, pk):
    if request.method == "POST":
        data = get_object_or_404(BiomedicalData, pk=pk, user=request.user)
        data.delete()
    return redirect('users:data_list')
