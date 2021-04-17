from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    count_persons = forms.IntegerField(min_value=0, max_value=99, required=True)
    address = forms.CharField(max_length=256, required=True)

    class Meta:
        model = Order
        fields = ['address', 'count_persons']
