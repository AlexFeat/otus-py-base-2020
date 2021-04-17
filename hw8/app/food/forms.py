from django import forms
from .models import Food, Category, Country


class FoodForm(forms.ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField()
    cost = forms.FloatField(required=True, min_value=0)
    category = forms.ModelChoiceField(Category.objects)
    country = forms.ModelChoiceField(Country.objects)

    class Meta:
        model = Food
        fields = '__all__'
