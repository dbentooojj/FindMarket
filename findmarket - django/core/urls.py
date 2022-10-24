# criando as paginas do site (urls - views(o que vai acontecer) - templates(visual do site)))

from django.urls import path, include
from .views import homepage, login, cafe, papel, cadastro, endereco, principal, principal2, feijao, arroz, macarrao, sal, molho_tomate, farinha_trigo, cafe, detergente, contato, sams, bistek, atacadao, rede, giassi, cooper, fort

#cooper
from .views import cooperfeijao, cooperarroz, coopermacarrao, coopermolho, cooperpapel, cooperfarinha, cooperdetergente, coopersal, coopercafe
#sams
from .views import samsfeijao, samsarroz, samsmacarrao, samsmolho, samspapel, samsfarinha, samsdetergente, samssal, samscafe
#fort
from .views import fortfeijao, fortarroz, fortmacarrao, fortmolho, fortpapel, fortfarinha, fortdetergente, fortsal, fortcafe
#giassi
from .views import giassifeijao, giassiarroz, giassimacarrao, giassimolho, giassipapel, giassifarinha, giassidetergente, giassisal, giassicafe
#rede
from .views import redefeijao, redearroz, redemacarrao, redemolho, redepapel, redefarinha, rededetergente, redesal, redecafe
#atacadao
from .views import atacadaofeijao, atacadaoarroz, atacadaomacarrao, atacadaomolho, atacadaopapel, atacadaofarinha, atacadaodetergente, atacadaosal, atacadaocafe
#bistek
from .views import bistekfeijao, bistekarroz, bistekmacarrao, bistekmolho, bistekpapel, bistekfarinha, bistekdetergente, bisteksal, bistekcafe

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('sams/principal/', sams, name='sams'),
    path('fort/principal/', fort, name='fort'),
    path('cooper/principal/', cooper, name='cooper'),
    path('giassi/principal/', giassi, name='giassi'),
    path('bistek/principal/', bistek, name='bistek'),
    path('rede/principal/', rede, name='rede'),
    path('atacadao/principal/', atacadao, name='atacadao'),
    path('endereco/', endereco, name='endereco'),
    path('principal/principal/', principal, name='principal'),
    path('principal2/', principal2, name='principal2'),
    path('principal/feijao/', feijao, name='feijao'),
    path('principal/papel/', papel, name='papel'),
    path('principal/arroz/', arroz, name='arroz'),
    path('principal/macarrao/', macarrao, name='macarrao'),
    path('principal/sal/', sal, name='sal'),
    path('principal/molho/', molho_tomate, name='molho_tomate'),
    path('principal/farinha/', farinha_trigo, name='farinha_trigo'),
    path('principal/cafe/', cafe, name='cafe'),
    path('principal/detergente/', detergente, name='detergente'),
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
    path('cooper/cafe/', coopercafe, name='coopercafe'),

    #sams
    path('sams/feijao/', samsfeijao, name='samsfeijao'),
    path('sams/arroz/', samsarroz, name='samsarroz'),
    path('sams/macarrao/', samsmacarrao, name='samsmacarrao'),
    path('sams/molho/', samsmolho, name='samsmolho'),
    path('sams/papel/', samspapel, name='samspapel'),
    path('sams/farinha/', samsfarinha, name='samsfarinha'),
    path('sams/detergente/', samsdetergente, name='samsdetergente'),
    path('sams/sal/', samssal, name='samssal'),
    path('sams/cafe/', samscafe, name='samscafe'),

    #fort
    path('fort/feijao/', fortfeijao, name='fortfeijao'),
    path('fort/arroz/', fortarroz, name='fortarroz'),
    path('fort/macarrao/', fortmacarrao, name='fortmacarrao'),
    path('fort/molho/', fortmolho, name='fortmolho'),
    path('fort/papel/', fortpapel, name='fortpapel'),
    path('fort/farinha/', fortfarinha, name='fortfarinha'),
    path('fort/detergente/', fortdetergente, name='fortdetergente'),
    path('fort/sal/', fortsal, name='fortsal'),
    path('fort/cafe/', fortcafe, name='fortcafe'),

    #giassi
    path('giassi/feijao/', giassifeijao, name='giassifeijao'),
    path('giassi/arroz/', giassiarroz, name='giassiarroz'),
    path('giassi/macarrao/', giassimacarrao, name='giassimacarrao'),
    path('giassi/molho/', giassimolho, name='giassimolho'),
    path('giassi/papel/', giassipapel, name='giassipapel'),
    path('giassi/farinha/', giassifarinha, name='giassifarinha'),
    path('giassi/detergente/', giassidetergente, name='giassidetergente'),
    path('giassi/sal/', giassisal, name='giassisal'),
    path('giassi/cafe/', giassicafe, name='giassicafe'),

    #rede
    path('rede/feijao/', redefeijao, name='redefeijao'),
    path('rede/arroz/', redearroz, name='redearroz'),
    path('rede/macarrao/', redemacarrao, name='redemacarrao'),
    path('rede/molho/', redemolho, name='redemolho'),
    path('rede/papel/', redepapel, name='redepapel'),
    path('rede/farinha/', redefarinha, name='redefarinha'),
    path('rede/detergente/', rededetergente, name='rededetergente'),
    path('rede/sal/', redesal, name='redesal'),
    path('rede/cafe/', redecafe, name='redecafe'),

    #atacadao
    path('atacadao/feijao/', atacadaofeijao, name='atacadaofeijao'),
    path('atacadao/arroz/', atacadaoarroz, name='atacadaoarroz'),
    path('atacadao/macarrao/', atacadaomacarrao, name='atacadaomacarrao'),
    path('atacadao/molho/', atacadaomolho, name='atacadaomolho'),
    path('atacadao/papel/', atacadaopapel, name='atacadaopapel'),
    path('atacadao/farinha/', atacadaofarinha, name='atacadaofarinha'),
    path('atacadao/detergente/', atacadaodetergente, name='atacadaodetergente'),
    path('atacadao/sal/', atacadaosal, name='atacadaosal'),
    path('atacadao/cafe/', atacadaocafe, name='atacadaocafe'),

    #bistek
    path('bistek/feijao/', bistekfeijao, name='bistekfeijao'),
    path('bistek/arroz/', bistekarroz, name='bistekarroz'),
    path('bistek/macarrao/', bistekmacarrao, name='bistekmacarrao'),
    path('bistek/molho/', bistekmolho, name='bistekmolho'),
    path('bistek/papel/', bistekpapel, name='bistekpapel'),
    path('bistek/farinha/', bistekfarinha, name='bistekfarinha'),
    path('bistek/detergente/', bistekdetergente, name='bistekdetergente'),
    path('bistek/sal/', bisteksal, name='bisteksal'),
    path('bistek/cafe/', bistekcafe, name='bistekcafe'),

]
