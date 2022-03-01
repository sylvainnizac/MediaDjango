from django import forms
from src.products.models import Product


class ProductForm(forms.ModelForm):
    """
        form used in product creation and update
    """

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
        self.fields['can_be_sold'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Product
        fields = ("name", "stockpile", "price", "can_be_sold")
