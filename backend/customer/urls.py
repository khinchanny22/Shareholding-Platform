from django.urls import path

from . import views

urlpatterns = [
    path('', views.Customer, name='Customer'),
]