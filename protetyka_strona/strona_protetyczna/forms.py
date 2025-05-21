from django import forms
from .models import CennikPozycja

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CennikForm(forms.ModelForm):
    class Meta:
        model = CennikPozycja
        fields = ['nazwa', 'opis', 'cena']