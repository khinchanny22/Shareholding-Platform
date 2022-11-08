from django.urls import path

from . import views

urlpatterns = [
    path('', views.Customers, name='Customers'),
    path('add_customers_backend', views.AddCustomersBackend, name='AddCustomersBackend'),
    path('update_customers_backend/<int:id>', views.UpdateCustomerBackend, name='UpdateCustomerBackend'),
    path('views_customer_backend/<int:id>', views.ViewCustomerBackend, name='ViewCustomerBackend'),

    # customer frontend
    path('customer_register_frontend', views.RegisterCustomerFrontend, name='RegisterCustomerFrontend'),
]