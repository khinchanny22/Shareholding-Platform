from django import forms
from .models import *


class SellerForm(forms.ModelForm):
    class Meta:
        model = BuyShareToCustomer
        fields = "__all__"
