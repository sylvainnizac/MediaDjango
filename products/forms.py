from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    stockpile = forms.IntegerField(initial=0)
    price = forms.FloatField(initial=0.0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Product
        fields = ('name', 'stockpile', 'price')