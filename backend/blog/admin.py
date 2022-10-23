from django.contrib import admin
from .models import *
from django.forms import Media, MediaDefiningClass


# Register your models here.
class PostBlogAdmin(admin.ModelAdmin):
    list_display = ['content_title', 'image', 'date', 'author', 'content']


admin.site.register(PostBlog, PostBlogAdmin)
