import site

from django.contrib import admin
from django.utils.html import format_html
from .models import *


class AdminProfile(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))

    list_display = ['customer', 'phone', 'image_tag', 'address']
    readonly_fields = ('image',)

    def image(self, obj):
        return obj.thumbnail_preview

    image.short_description = 'Thumbnail Preview'
    image.allow_tags = True


admin.site.register(Profile, AdminProfile)