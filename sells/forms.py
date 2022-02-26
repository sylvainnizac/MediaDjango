from datetime import datetime

from django import forms
from products.models import Product
from sells.models import Sell

# class SellForm(forms.ModelForm):
#     client_name = forms.CharField(max_length=128, help_text="Please enter the client name.")
#     quantity = forms.IntegerField(initial=0)
#     product = forms.ModelChoiceField(queryset=Product.objects.all())
#     date = forms.DateField(initial=datetime.now)
#     unit_price = forms.FloatField(initial=0.0)
# 
#     # An inline class to provide additional information on the form.
#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Sell
#         fields = ("client_name", "quantity", "product", "date", "unit_price")



class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ("client_name", "quantity", "product")

    def __init__(self, *args, **kwargs):
        super(SellForm, self).__init__(*args, **kwargs)
        self.fields["product"]=forms.ModelChoiceField(queryset=Product.objects.all())
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'