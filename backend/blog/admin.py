from django.contrib import admin
from .models import *
from django.forms import Media, MediaDefiningClass


# Register your models here.
class PostBlogAdmin(admin.ModelAdmin):
    list_display = ['content_title', 'image', 'date', 'author', 'content']


admin.site.register(PostBlog, PostBlogAdmin)


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'email', 'website', 'comment']
    search_fields = ['author', 'email']
    list_filter = ['author', 'email']


admin.site.register(BlogComment, BlogCommentAdmin)
