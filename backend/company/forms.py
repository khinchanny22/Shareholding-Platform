from django import forms

from .models import ContactUs, Address, AboutUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"
