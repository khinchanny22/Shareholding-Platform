from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django_ckeditor_5.fields import CKEditor5Field

from customer.models import Customer


class DocumentManagementSystem(models.Model):
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subject_status = (
        ("SELECT", "SELECT"),
        ("Activated Account", "Activated Account"),
        ("Reset Password", "Reset Password"),
        ("Commission", "Commission"),
        ("Others", "Others"),
    )
    subject = models.CharField(max_length=20,
                               choices=subject_status,
                               default="SELECT")
    document = models.ImageField(upload_to='dms')
    start_date = models.DateField()
    end_date = models.DateField()
    dms_status = (
        ("SELECT", "SELECT"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Padding", "Padding"),
        ("Others", "Others"),
    )
    dms_status = models.CharField(max_length=20,
                               choices=dms_status,
                               default="SELECT")
    description = CKEditor5Field(blank=True, null=True, config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
