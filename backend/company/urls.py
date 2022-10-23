from django.urls import path

from . import views

urlpatterns = [
    # about us
    path('', views.CompanyIndex, name='CompanyIndex'),
    path('add_about', views.AddAboutUs, name='AddAboutUs'),
    path('index_about_backend', views.IndexAboutUs, name='IndexAboutUs'),
    path('contact_detail', views.CompanyContactUs, name='CompanyContactUs'),
    path('address_detail/<int:id>', views.AddressView, name='AddressView'),
    # contact us
    path('contact_us/', views.ContactUs, name='ContactUs'),
    path('contact/', views.Contacts, name='Contacts'),

]