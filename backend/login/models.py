from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __int__(self):
        return self.username


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     avatar = models.ImageField(default='default.jpg', upload_to='profile')
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.user.username


class UserProfileManager(models.Manager):
    pass


class UserProfile(models.Model):
    # user = models.OneToOneField(User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phoneNumber = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username


def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.created(user=kwargs['instance'])

    post_save.connect(createProfile, sender=User)


class UserProfileLogin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='users/default_user.png', upload_to='users', blank=True, null=True)
