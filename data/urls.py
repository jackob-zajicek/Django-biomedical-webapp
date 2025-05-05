from django.urls import path
from . import views

urlpatterns = [
    # ... ostatní cesty ...
    path('upload/', views.upload_data, name='upload_data'),
]