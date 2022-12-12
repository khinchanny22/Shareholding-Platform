from django.db import models

from customer.models import Customer
from product.models import Product


# Create your models here.

class BuyShareToCustomer(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    share_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    share_quantity = models.CharField(max_length=100)
    share_pricing = models.CharField(max_length=10)
    buyer_share_tax = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer_name)