from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('', views.signout, name='signout'),
]