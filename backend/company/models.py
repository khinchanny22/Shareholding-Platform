from django.db import models


# Create your models here.
class AboutUs(models.Model):
    company = models.CharField(max_length=1000)
    company_info = models.TextField()
    mission = models.CharField(max_length=1000)
    mission_description = models.TextField()
    vision = models.CharField(max_length=1000)
    vision_description = models.TextField()

    def __str__(self):
        return self.company


class ContactUs(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.subject


class ContactUsFrontend(models.Model):
    username = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Address(models.Model):
    phone = models.IntegerField()
    email = models.EmailField()
    fax = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return str(self.phone)
