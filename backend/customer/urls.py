from django.urls import path

from . import views

urlpatterns = [
    path('', views.Customers, name='Customers'),
    path('add_customers', views.AddCustomers, name='AddCustomers'),
    path('update_customers/<int:id>', views.UpdateCustomer, name='UpdateCustomer'),
]