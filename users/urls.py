from django.urls import path, include
from .views import RegisterView
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
path('register/', RegisterView.as_view(), name='register'),
    path('', views.index, name='index'),
    path('users/profile/', views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', include(router.urls)),
    path('data/', views.data_list, name='data_list'),
    path('data/upload/', views.upload_data, name='upload_data'),

]

