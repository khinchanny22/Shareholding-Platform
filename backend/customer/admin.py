from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_contact', 'customer_email', 'Customer_origin']
admin.site.register(Customer, CustomerAdmin)

