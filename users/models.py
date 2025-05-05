from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    objects = UserManager()


