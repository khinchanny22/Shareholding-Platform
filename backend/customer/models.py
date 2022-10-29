from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=50, unique=True)
    customer_contact = models.CharField(max_length=15, unique=True)
    customer_email = models.EmailField(unique=True)
    customer_image = models.ImageField(upload_to='customer/')
    Customer_origin = models.CharField(max_length=20)
    customer_status = (
        ("SELECT", "SELECT"),
        ("Seller", "Seller"),
        ("Buyer", "Buyer"),
        ("Mandate", "Mandate"),
    )
    customer_status = models.CharField(max_length=20,
                                       choices=customer_status,
                                       default="SELECT")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer_image)
