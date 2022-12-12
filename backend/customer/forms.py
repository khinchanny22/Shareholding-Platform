from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

    def clean(self):

        # data from the form is fetched using super function
        super(CustomerForm, self).clean()

        # extract the username and text field from the data
        customer_name = self.cleaned_data.get('customer_name')
        customer_contact = self.cleaned_data.get('customer_contact')

        # conditions to be met for the username length
        if len(customer_name) < 5:
            self._errors['customer_name'] = self.error_class([
                'Minimum 5 characters required'])
        if int(customer_contact) < 10:
            self._errors['customer_contact'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        # return any errors if found
        return self.cleaned_data
