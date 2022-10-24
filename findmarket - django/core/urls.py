# criando as paginas do site (urls - views(o que vai acontecer) - templates(visual do site)))

from django.urls import path, include
from .views import homepage, login, cadastro, endereco, principal, principal2, feijao, arroz, macarrao, sal, molho_tomate, farinha_trigo, cafe, detergente, contato, sams, bistek, atacadao, rede, giassi, cooper, fort

#cooper
from .views import cooperfeijao, cooperarroz, coopermacarrao, coopermolho, cooperpapel, cooperfarinha, cooperdetergente, coopersal
#sams
from .views import samsfeijao, samsarroz, samsmacarrao, samsmolho, samspapel, samsfarinha, samsdetergente, samssal
#fort
from .views import fortfeijao, fortarroz, fortmacarrao, fortmolho, fortpapel, fortfarinha, fortdetergente, fortsal
#giassi
from .views import giassifeijao, giassiarroz, giassimacarrao, giassimolho, giassipapel, giassifarinha, giassidetergente, giassisal
#rede
from .views import redefeijao, redearroz, redemacarrao, redemolho, redepapel, redefarinha, rededetergente, redesal
#atacadao
from .views import atacadaofeijao, atacadaoarroz, atacadaomacarrao, atacadaomolho, atacadaopapel, atacadaofarinha, atacadaodetergente, atacadaosal
#bistek
from .views import bistekfeijao, bistekarroz, bistekmacarrao, bistekmolho, bistekpapel, bistekfarinha, bistekdetergente, bisteksal

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('sams/', sams, name='sams'),
    path('fort/', fort, name='fort'),
    path('cooper/', cooper, name='cooper'),
    path('giassi/', giassi, name='giassi'),
    path('bistek/', bistek, name='bistek'),
    path('rede/', rede, name='rede'),
    path('atacadao/', atacadao, name='atacadao'),
    path('endereco/', endereco, name='endereco'),
    path('principal/', principal, name='principal'),
    path('principal2/', principal2, name='principal2'),
    path('feijao/', feijao, name='feijao'),
    path('arroz/', arroz, name='arroz'),
    path('macarrao/', macarrao, name='macarrao'),
    path('sal/', sal, name='sal'),
    path('molho_tomate/', molho_tomate, name='molho_tomate'),
    path('farinha_trigo/', farinha_trigo, name='farinha_trigo'),
    path('cafe/', cafe, name='cafe'),
    path('detergente/', detergente, name='detergente'),
    path('contato/', contato, name='contato'),

    #cooper
    path('cooper/feijao/', cooperfeijao, name='cooperfeijao'),
    path('cooper/arroz/', cooperarroz, name='cooperarroz'),
    path('cooper/macarrao/', coopermacarrao, name='coopermacarrao'),
    path('cooper/molho/', coopermolho, name='coopermolho'),
    path('cooper/papel/', cooperpapel, name='cooperpapel'),
    path('cooper/farinha/', cooperfarinha, name='cooperfarinha'),
    path('cooper/detergente/', cooperdetergente, name='cooperdetergente'),
    path('cooper/sal/', coopersal, name='coopersal'),

    #sams
    path('sams/feijao/', samsfeijao, name='samsfeijao'),
    path('sams/arroz/', samsarroz, name='samsarroz'),
    path('sams/macarrao/', samsmacarrao, name='samsmacarrao'),
    path('sams/molho/', samsmolho, name='samsmolho'),
    path('sams/papel/', samspapel, name='samspapel'),
    path('sams/farinha/', samsfarinha, name='samsfarinha'),
    path('sams/detergente/', samsdetergente, name='samsdetergente'),
    path('sams/sal/', samssal, name='samssal'),

    #fort
    path('fort/feijao/', fortfeijao, name='fortfeijao'),
    path('fort/arroz/', fortarroz, name='fortarroz'),
    path('fort/macarrao/', fortmacarrao, name='fortmacarrao'),
    path('fort/molho/', fortmolho, name='fortmolho'),
    path('fort/papel/', fortpapel, name='fortpapel'),
    path('fort/farinha/', fortfarinha, name='fortfarinha'),
    path('fort/detergente/', fortdetergente, name='fortdetergente'),
    path('fort/sal/', fortsal, name='fortsal'),

    #giassi
    path('giassi/feijao/', giassifeijao, name='giassi'),
    path('giassi/arroz/', giassiarroz, name='giassi'),
    path('giassi/macarrao/', giassimacarrao, name='giassi'),
    path('giassi/molho/', giassimolho, name='giassi'),
    path('giassi/papel/', giassipapel, name='giassi'),
    path('giassi/farinha/', giassifarinha, name='giassi'),
    path('giassi/detergente/', giassidetergente, name='giassi'),
    path('giassi/sal/', giassisal, name='giassi'),

    #rede
    path('rede/feijao/', redefeijao, name='redefeijao'),
    path('rede/arroz/', redearroz, name='redearroz'),
    path('rede/macarrao/', redemacarrao, name='redemacarrao'),
    path('rede/molho/', redemolho, name='redemolho'),
    path('rede/papel/', redepapel, name='redepapel'),
    path('rede/farinha/', redefarinha, name='redefarinha'),
    path('rede/detergente/', rededetergente, name='rededetergente'),
    path('rede/sal/', redesal, name='redesal'),

    #atacadao
    path('atacadao/feijao/', atacadaofeijao, name='atacadaofeijao'),
    path('atacadao/arroz/', atacadaoarroz, name='atacadaoarroz'),
    path('atacadao/macarrao/', atacadaomacarrao, name='atacadaomacarrao'),
    path('atacadao/molho/', atacadaomolho, name='atacadaomolho'),
    path('atacadao/papel/', atacadaopapel, name='atacadaopapel'),
    path('atacadao/farinha/', atacadaofarinha, name='atacadaofarinha'),
    path('atacadao/detergente/', atacadaodetergente, name='atacadaodetergente'),
    path('atacadao/sal/', atacadaosal, name='atacadaosal'),

    #bistek
    path('bistek/feijao/', bistekfeijao, name='bistekfeijao'),
    path('bistek/arroz/', bistekarroz, name='bistekarroz'),
    path('bistek/macarrao/', bistekmacarrao, name='bistekmacarrao'),
    path('bistek/molho/', bistekmolho, name='bistekmolho'),
    path('bistek/papel/', bistekpapel, name='bistekpapel'),
    path('bistek/farinha/', bistekfarinha, name='bistekfarinha'),
    path('bistek/detergente/', bistekdetergente, name='bistekdetergente'),
    path('bistek/sal/', bisteksal, name='bisteksal'),

]
