from django import forms
from django.forms import Textarea
from .models import ContactUs, Address, AboutUs, ContactUsFrontend


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class AboutUsForm(forms.ModelForm):
    company_info = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = AboutUs
        fields = "__all__"


class ContactUsFrontendForm(forms.ModelForm):
    class Meta:
        model = ContactUsFrontend
        fields = "__all__"
