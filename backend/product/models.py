
from django.db import models
from django.db import models
from django.utils.safestring import mark_safe # new


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='upload/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def image_tag(self):  # new
        return mark_safe('<img src="media/media/%s" width="150" height="150" />' % (self.product_image))


class ProductPrice(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_price)

    def product_price(self):
        return self.product_price
