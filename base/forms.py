from django import forms
from django.forms import ModelForm
from .models import Curso, Modelo, Formando


# Create forms
class FormandoForm(ModelForm):
    class Meta:
        model = Formando
        fields = '__all__'
        labels = {
            'nome': '',
            'habilitacoes': '',
            'email': '',
            'contacto': '',
            'morada': '',
            'codigo_postal': '',
            'localidade': '',
            'bi': '',
            'validade': '',
            'data_nascimento': '',
            'natural': '',
            'nacionalidade': '',
            'nif': '',
            'observacoes': '',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'habilitacoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Habilitações'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto'}),
            'morada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Morada'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codigo postal'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localidade'}),
            'bi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cartão de Cidadão Nº'}),
            'validade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Validade'}),
            'data_nascimento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidade'}),
            'natural': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Naturalidade'}),
            'nif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIF'}),
            'observacoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observações'}),
        }
