from django import forms
from django.forms import RadioSelect
from .models import *


class Form(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = '__all__'
        exclude = ['id_produto', 'imagem_produto', 'link_produto', 'data_produto', 'preco_produto', 'mercado']

class SideBar(forms.Form):
    MARKET_CHOICES = [
        ('Bistek', 'Bistek'),
        ('Atacadao','Atacadao')
    ]
    Atacadao = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=MARKET_CHOICES,
    )