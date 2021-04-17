from django import forms
from .models import User


class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email', 'name', 'password']


class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email', 'password']
