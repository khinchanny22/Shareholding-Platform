from django.contrib import admin
from django.db import models
from .forms import *


class SupportAdmin(admin.ModelAdmin):
    list_display = ['title', 'contents']


admin.site.register(Policy, SupportAdmin)


class TermConditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'contents']


admin.site.register(TermCondition, TermConditionAdmin)
