from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    gender=models.CharField(max_length=20)
    role=models.CharField(max_length=20)

    def __str__(self):
        return self.username