from django.contrib import admin

# Register your models here.
from .models import Product, ProductPrice


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_price', 'product_quantity', 'product_description', 'product_image']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice)
