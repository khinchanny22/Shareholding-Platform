from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path('', views.login_request, name="login_request"),
    path("logout_request", views.logout_request, name="logout_request"),
]