from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('users', views.User, name='User'),
]