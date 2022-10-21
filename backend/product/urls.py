from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.ProductIndex, name='ProductIndex'),
    path('add_product', views.AddProduct, name='AddProduct'),
    path('updated_product/<int:id>', views.UpdateProduct, name='UpdateProduct'),
    # product price
    path('product_price', views.ProductCost, name='ProductCost'),
    path('add_product_price', views.AddProductPrice, name='AddProductPrice'),
    path('update_product_price/<int:id>', views.UpdateProducePrice, name='UpdateProducePrice'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
