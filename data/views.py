from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BiomedicalDataForm

@login_required
def upload_data(request):
    if request.method == 'POST':
        form = BiomedicalDataForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('profile')
    else:
        form = BiomedicalDataForm()
    return render(request, 'upload_data.html', {'form': form})