from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='data_list'),
    path('upload/', views.upload_data, name='upload_data'),
]