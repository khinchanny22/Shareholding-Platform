from django.urls import path

from . import views

urlpatterns = [
    path('index_dms', views.DmsIndex, name='DmsIndex'),
    path('detail_dms/<int:id>', views.DmsView, name='DmsView'),
    path('update_dms_backend/<int:id>', views.UpdateDmsBackend, name='UpdateDmsBackend'),
    path('create_dms', views.CreateDmsBackend, name='CreateDmsBackend'),

]