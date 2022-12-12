from django.contrib import admin

# Register your models here.
from .models import DocumentManagementSystem


class DMSadmin(admin.ModelAdmin):
    list_display = ['id','name','subject', 'document', 'start_date', 'end_date']


admin.site.register(DocumentManagementSystem, DMSadmin)
