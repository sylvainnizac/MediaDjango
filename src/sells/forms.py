from django import forms
from src.products.models import Product
from src.sells.models import Sell


class SellForm(forms.ModelForm):
    """
        form used in sell creation and update
    """

    def __init__(self, *args, **kwargs):
        super(SellForm, self).__init__(*args, **kwargs)
        self.fields["product"]=forms.ModelChoiceField(queryset=Product.objects.filter(can_be_sold=True).all())
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Sell
        fields = ("client_name", "quantity", "product")
