from django.contrib import admin

# Register your models here.
from .models import Product, ProductPrice


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_quantity', 'product_description']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPrice)
