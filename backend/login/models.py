from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __int__(self):
        return self.username
