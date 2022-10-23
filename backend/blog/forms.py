from django import forms
from django.forms import NumberInput

from .models import *


class BlogForm(forms.ModelForm):
    date = forms.DateField(widget=NumberInput(attrs={
        'type': 'date',
        'class': 'form-control'
    }))

    class Meta:
        model = PostBlog
        fields = "__all__"
