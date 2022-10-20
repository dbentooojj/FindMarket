# criando as paginas do site (urls - views(o que vai acontecer) - templates(visual do site)))

from django.urls import path, include
from .views import homepage, login, cadastro, endereco, principal, feijao, arroz, macarrao, sal, molho_tomate, farinha_trigo, cafe, detergente, contato, market_forms

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('TesteForms', market_forms, name='market_forms'),
    path('endereco/', endereco, name='endereco'),
    path('principal/', principal, name='principal'),
    path('feijao/', feijao, name='feijao'),
    path('arroz/', arroz, name='arroz'),
    path('macarrao/', macarrao, name='macarrao'),
    path('sal/', sal, name='sal'),
    path('molho_tomate/', molho_tomate, name='molho_tomate'),
    path('farinha_trigo/', farinha_trigo, name='farinha_trigo'),
    path('cafe/', cafe, name='cafe'),
    path('detergente/', detergente, name='detergente'),
    path('contato/', contato, name='contato'),
]
