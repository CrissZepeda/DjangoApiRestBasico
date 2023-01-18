from django import forms
from .models import Reservas


class registerReserva(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['nombre','fono', 'fecha', 'hora', 'cantidad', 'observacion']
        widgets = {
            'nombre': forms.TextInput(attrs={"class": "form-control"}),
            'fono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control'}),
            'cantidad': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'})
        }
        


