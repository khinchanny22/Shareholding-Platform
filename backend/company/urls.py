from django.urls import path

from . import views

urlpatterns = [
    # about us
    path('', views.CompanyIndex, name='CompanyIndex'),
    path('contact_detail', views.CompanyContactUs, name='CompanyContactUs'),
    path('address_detail/<int:id>', views.AddressView, name='AddressView'),
    # contact us
    path('contact_us', views.ContactUs, name='ContactUs'),

]