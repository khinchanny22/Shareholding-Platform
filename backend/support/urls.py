from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('support_index_frontend', views.IndexSupportFrontend, name='IndexSupportFrontend'),
    path('index_term_condition_frontend', views.IndexTermCondition, name='IndexTermCondition'),

]
