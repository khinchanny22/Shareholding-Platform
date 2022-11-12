from django.db import models
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Policy(models.Model):
    title = models.CharField(max_length=200)
    contents = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class TermCondition(models.Model):
    title = models.CharField(max_length=200)
    contents = CKEditor5Field(config_name='extends',null=True)

    def __str__(self):
        return self.title
