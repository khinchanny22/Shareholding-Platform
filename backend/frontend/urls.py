from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontend, name='frontend'),
    path('frontend_products', views.FrontendProducts, name='FrontendProducts'),
    path('Product_Details', views.ProductDetails, name='ProductDetails'),
    path('Shopping_Cart', views.ShoppingCart, name='ShoppingCart'),
    path('Layout_Product', views.LayoutProduct, name='LayoutProduct'),
]