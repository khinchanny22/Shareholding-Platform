from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('users', views.User, name='User'),
    path('creare_users_backend', views.CreateUserBackend, name='CreateUserBackend'),
    path('view_user_backend', views.ViewUserManagement, name='ViewUserManagement'),
    path('update_user_backend', views.UpdateUsersBackend, name='UpdateUsersBackend'),

    # UserPermission
    path('user_permission', views.UserPermission, name='UserPermission'),

]