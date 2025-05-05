from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_data, name='upload_data'),
    path('', views.data_list, name='data_list'),
]