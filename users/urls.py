from django.urls import path
from .views import RegisterView
from . import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]

