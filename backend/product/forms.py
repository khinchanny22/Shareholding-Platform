from django import forms

from .models import Product, ProductPrice


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = "__all__"