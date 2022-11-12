from django import forms
from .models import *

from ckeditor.widgets import CKEditorWidget


class SupportAdminForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ('title', 'contents')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Title'})


class TermConditionForm(forms.ModelForm):

    class Meta:
        model = TermCondition
        fields = "__all__"
