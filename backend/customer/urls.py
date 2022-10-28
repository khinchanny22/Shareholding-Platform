from django.urls import path

from . import views

urlpatterns = [
    path('', views.Customers, name='Customers'),
    path('add_customers_backend', views.AddCustomersBackend, name='AddCustomersBackend'),
    path('update_customers/<int:id>', views.UpdateCustomer, name='UpdateCustomer'),
]