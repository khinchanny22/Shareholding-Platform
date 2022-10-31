from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from .models import Product, ProductPrice


class ProductAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.product_image.url))

    list_display = ['product_name', 'product_price', 'product_quantity', 'product_description', 'image_tag']
    search_fields = ['product_name', 'product_price',]
    list_filter = ['product_name', 'product_price',]


admin.site.register(Product, ProductAdmin)


class ProducePriceAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price']
    list_filter = ['product_name', 'product_price']
    search_fields = ['product_name', 'product_price']


admin.site.register(ProductPrice, ProducePriceAdmin)
