
from django.db import models
from django.db import models
from django.utils.safestring import mark_safe # new


# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_price = models.IntegerField()
    product_description = models.TextField(max_length=1000)
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='product/')
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
        return str(self.product_name)


# model named Post
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )

    # define a username filed with bound  max length it can have
    username = models.CharField(max_length=20, blank=False,
                                null=False)

    # This is used to write a post
    text = models.TextField(blank=False, null=False)

    # Values for gender are restricted by giving choices
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              default=Male)

    time = models.DateTimeField(auto_now_add=True)


