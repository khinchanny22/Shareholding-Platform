from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    #
    path('support_index_frontend', views.IndexSupportFrontend, name='IndexSupportFrontend'),
    path('support_views_frontend/<int:id>', views.ViewsPolicy, name='ViewsPolicy'),
    path('support_update_frontend/<int:id>', views.UpdatePolicy, name='UpdatePolicy'),
    path('support_create_frontend', views.CreatePolicy, name='CreatePolicy'),
    #
    path('index_term_condition_frontend', views.IndexTermCondition, name='IndexTermCondition'),
    path('add_term_condition_frontend', views.AddTermCondition, name='AddTermCondition'),
    path('update_term_condition_frontend/<int:id>', views.UpdateTermCondition, name='UpdateTermCondition'),
    path('delete_term_condition_frontend/<int:id>', views.DeleteTermCondition, name='DeleteTermCondition'),
    path('views_term_condition_frontend/<int:id>', views.ViewsTermCondition, name='ViewsTermCondition'),

]
