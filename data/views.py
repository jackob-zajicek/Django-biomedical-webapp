from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import BiomedicalData
from .forms import BiomedicalDataForm
from django.shortcuts import redirect, get_object_or_404
from .models import BiomedicalData
from django.contrib.auth.decorators import login_required

@login_required
def data_list(request):
    user_data = BiomedicalData.objects.filter(user=request.user)
    return render(request, 'data/list.html', {'user_data': user_data})

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


