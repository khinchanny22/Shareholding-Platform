from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

    def clean(self):
        customer_name = self.cleaned_data.get("customer_name")
        customer_contact = self.cleaned_data.get("customer_contact")
        # Check if user and password is matching and exists
        user = Customer(customer_name=customer_name, customer_contact=customer_contact)
        if not user:
            raise forms.ValidationError("This is an invalid data.")
