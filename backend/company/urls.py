from django.urls import path

from . import views

urlpatterns = [
    # about us
    path('', views.CompanyIndex, name='CompanyIndex'),


    # url about us backend
    path('add_about', views.AddAboutUs, name='AddAboutUs'),
    path('index_about_backend', views.IndexAboutUs, name='IndexAboutUs'),
    path('view_about_backend/<int:id>', views.ViewAboutUsBackend, name='ViewAboutUsBackend'),
    path('update_about_backend/<int:id>', views.UpdateAboutUsBackend, name='UpdateAboutUsBackend'),

    # url contact us backend
    path('index_contact_backend', views.IndexContactBackend, name='IndexContactBackend'),
    path('view_contact_backend/<int:id>', views.ViewContactUsBackend, name='ViewContactUsBackend'),

    # contact us frontend
    path('index_contact_frontend', views.IndexContactUsFrontend, name='IndexContactUsFrontend'),
    path('add_contact_frontend', views.AddContactUsFrontend, name='AddContactUsFrontend'),

    path('contact_detail', views.CompanyContactUs, name='CompanyContactUs'),
    path('address_detail/<int:id>', views.AddressView, name='AddressView'),

]