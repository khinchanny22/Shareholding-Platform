from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=15, unique=True)
    customer_email = models.EmailField(unique=True)
    Customer_origin = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name
