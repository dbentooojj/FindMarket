from django import forms
from .models import *


class Form(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = '__all__'
        exclude = ['id_produto', 'imagem_produto', 'link_produto', 'data_produto', 'preco_produto', 'mercado']