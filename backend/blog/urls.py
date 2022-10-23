from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    # about us
    path('index_blog_post', views.IndexPostBlog, name='IndexPostBlog'),
    path('add_blog_post', views.AddPostBlog, name='AddPostBlog'),
    path('udpate_blog_post/<int:id>', views.UpdateBlogPost, name='UpdateBlogPost'),

    # url blog frontend
    path('index_blog_frontend', views.IndexBlogFrontend, name='IndexBlogFrontend'),

]