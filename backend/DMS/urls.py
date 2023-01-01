from django.urls import path

from . import views

urlpatterns = [
    path('index_dms', views.DmsIndex, name='DmsIndex'),
    path('detail_dms/<int:id>', views.DmsView, name='DmsView'),
    path('create_dms', views.CreateDmsBackend, name='CreateDmsBackend'),

]