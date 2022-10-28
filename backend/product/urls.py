from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    # url product backend
    path('', views.IndexProductBackend, name='IndexProductBackend'),
    path('add_product_backend', views.AddProductBackend, name='AddProductBackend'),
    path('updated_product_backend/<int:id>', views.UpdateProductBackend, name='UpdateProductBackend'),
    path('view_product_backend/<int:id>', views.ViewProductBackend, name='ViewProductBackend'),

    # product price
    path('product_price', views.ProductCost, name='ProductCost'),
    path('add_product_price', views.AddProductPrice, name='AddProductPrice'),
    path('update_product_price/<int:id>', views.UpdateProducePrice, name='UpdateProducePrice'),

    # look for share backend
    path('look_for_share', views.IndexLookShareBackend, name='IndexLookShareBackend'),

    # test Post
    path('post_test', views.Post, name='Post'),
]