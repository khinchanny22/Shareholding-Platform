from django.contrib import admin

from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email']

admin.site.register(Profile, ProfileAdmin)