from django import forms
from django.forms import ModelForm
from .models import Hospedagem


class HospedagemForm(ModelForm):
    class Meta:
        model = Hospedagem
        fields = '__all__'
        widgets = {
            'data_entrada' : forms.DateInput(attrs={"class":"form-control", "type":"date"}),
            'data_saida' : forms.DateInput(attrs={"class":"form-control", "type":"date"}),
            'valor' : forms.NumberInput(attrs={'class': 'form-control', "type": "number"}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'quarto': forms.Select(attrs={'class': 'form-control'})
        }