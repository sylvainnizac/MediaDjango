from django import forms
from src.products.models import Product


class ProductForm(forms.ModelForm):
    """
        form used in product creation and update
    """

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ('name', 'stockpile', 'price')