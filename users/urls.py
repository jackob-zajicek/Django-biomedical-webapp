from django.urls import path, include
from .views import RegisterView, UserViewSet, index, profile_view, logout_view, data_list, upload_data, data_delete
from django.contrib.auth import views as auth_views
from rest_framework import routers

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', index, name='index'),  # hlavní stránka
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/profile/', profile_view, name='profile'),
    path('data/list/', data_list, name='data_list'),
    path('data/', data_list, name='data_list'),
    path('data/upload/', upload_data, name='upload_data'),
    path('data/delete/<int:pk>/', data_delete, name='data_delete'),
    path('users/', include(router.urls)),
]