from django import forms
from django.forms import NumberInput

from .models import *


class BlogForm(forms.ModelForm):
    start_date = forms.DateField(widget=NumberInput(attrs={
        'type': 'date',
        'class': 'form-control'
    }))

    class Meta:
        model = PostBlog
        fields = "__all__"


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = "__all__"
