from django.contrib import admin

# Register your models here.
from .models import Product, ProductPrice


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_quantity', 'product_description', 'product_image']
    search_fields = ['product_name', 'product_price', 'product_quantity', 'product_description', 'product_image']
    list_filter = ['product_name', 'product_price', 'product_quantity', 'product_description', 'product_image']


admin.site.register(Product, ProductAdmin)


class ProducePriceAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price']
    list_filter = ['product_name', 'product_price']
    search_fields = ['product_name', 'product_price']


admin.site.register(ProductPrice, ProducePriceAdmin)
