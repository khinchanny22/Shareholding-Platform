from django import forms

from .models import Product, ProductPrice


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        # def __init__(self, *args, **kwargs):
        #     super(ProductForm, self).__init__(*args, **kwargs)
        #     for field_name, field in self.fields.items():
        #         field.widget.attrs['class'] = 'form-control'


class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = "__all__"
