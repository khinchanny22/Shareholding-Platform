from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_request, name="login_request"),
    path("register", views.register_request, name="register"),
    path("logout_request", views.logout_request, name="logout_request"),

    # customer register frontend
    path('register_customer_frontend', views.CustomerRegisterFrontend, name='CustomerRegisterFrontend'),


]
