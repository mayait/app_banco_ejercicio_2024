from django import forms
import datetime
from .models import Cliente

class ClienteBaseForm(forms.Form):
    # Base form
    FAVORITE_COLORS_CHOICES = {
    "blue": "Blue",
    "green": "Green",
    "black": "Black",
    }
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    cedula = forms.CharField(max_length=12)

class ClienteForm(forms.Form):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'cedula']
