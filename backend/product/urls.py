from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductIndex, name='ProductIndex'),
    path('add_product', views.AddProduct, name='AddProduct'),
    path('updated_product/<int:id>', views.UpdateProduct, name='UpdateProduct'),
    # product price
    path('product_price', views.ProductCost, name='ProductCost'),
    path('add_product_price', views.AddProductPrice, name='AddProductPrice'),
]