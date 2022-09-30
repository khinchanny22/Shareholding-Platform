

from django.db import models
from django.db import models


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='images/products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class ProductPrice(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_price)
