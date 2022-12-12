from django import forms
from django.forms import ModelForm

from .models import Product, ProductPrice, Post


class ProductForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Product

        # Custom fields
        fields = [
            "product_name", "product_price", "product_image", "product_quantity", "product_description"
        ]

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(ProductForm, self).clean()

        # extract the username and text field from the data
        product_name = self.cleaned_data.get('product_name')
        product_price = self.cleaned_data.get('product_price')
        product_image = self.cleaned_data.get('product_image')
        product_quantity = self.cleaned_data.get('product_quantity')
        product_description = self.cleaned_data.get('product_description')

        # conditions to be met for the username length
        if len(product_name) < 5:
            self._errors['product_name'] = self.error_class([
                'Minimum 5 characters required'])

        if int(product_price) < 1:
            self._errors['product_price'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        if len(product_image) < 100:
            self._errors['product_image'] = self.error_class([
                'Post Should Contain a minimum of 100 characters'])

        if int(product_quantity) < 1:
            self._errors['product_quantity'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        if len(product_description) < 10:
            self._errors['product_description'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        # return any errors if found
        return self.cleaned_data

class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = "__all__"


class PostForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Post

        # Custom fields
        fields = ["username", "gender", "text"]

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(PostForm, self).clean()

        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')

        # conditions to be met for the username length
        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
        if len(text) < 10:
            self._errors['text'] = self.error_class([
                'Post Should Contain a minimum of 10 characters'])

        # return any errors if found
        return self.cleaned_data