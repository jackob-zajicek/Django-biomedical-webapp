from django.urls import path, include
from . import views
from .api import api 

urlpatterns = [
    path('data_list/', views.data_list, name='data_list'),
    path('upload/', views.upload_data, name='upload_data'),
]