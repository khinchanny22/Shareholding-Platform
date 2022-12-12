import datetime

from django import forms
from django.db.models import DateField

from .models import DocumentManagementSystem


class DmsForm(forms.ModelForm):
    start_date = forms.DateField(label='Start Date', initial=datetime.date.today,
                                 widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                                 help_text='Please Select Starting Date')
    end_date = forms.DateField(label='End Date', initial=datetime.date.today,
                               widget=forms.widgets.DateInput(attrs={'type': 'date'}),
                               help_text='Please Select End Date')

    class Meta:
        model = DocumentManagementSystem
        fields = "__all__"
