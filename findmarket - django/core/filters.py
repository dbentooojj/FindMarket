import django_filters
from django_filters import CharFilter
from .models import *


class ProductFilter(django_filters.FilterSet):
    nome_produto = CharFilter(field_name='nome_produto', lookup_expr='icontains', label='')


    class Meta:
        model = Produtos
        fields = '__all__'
        exclude = ['idprodutos', 'mercado', 'categoria', 'peso_produto', 'preco_produto', 'imagem_produto', 'link_produto', 'link_logo', 'data_produto', 'volume_produto', ]