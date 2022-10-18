from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import Produtos
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.db.models import Q
from itertools import chain



# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def endereco(request):
    return render(request, 'enderecos.html')


def a(request):
    produtos_list = Produtos.objects.all()
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})



def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
   return dict_3

mercados = []

def principal(request, mercados):
    if len(mercados) == 0:
        mercados_list = ['Fort Atacadista','Sams']
    else:
        mercados_list = mercados

    mercado_dic1 = {'mercado':f'{mercados_list[0]}'}
    try:
        mercado_dic2 = {'mercado':f'{mercados_list[1]}'}
    except:
        mercado_dic2 = mercado_dic1
    try:
        mercado_dic3 = {'mercado':f'{mercados_list[2]}'}
    except:
        mercado_dic3 = mercado_dic1
    try:
        mercado_dic4 = {'mercado':f'{mercados_list[3]}'}
    except:
        mercado_dic4 = mercado_dic1
    try:
        mercado_dic5 = {'mercado':f'{mercados_list[4]}'}
    except:
        mercado_dic5 = mercado_dic1
    try:
        mercado_dic6 = {'mercado':f'{mercados_list[5]}'}
    except:
        mercado_dic6 = mercado_dic1
    try:
        mercado_dic7 = {'mercado':f'{mercados_list[6]}'}
    except:
        mercado_dic7 = mercado_dic1

    produtos_list = Produtos.objects.all().filter(**mercado_dic1)|Produtos.objects.all().filter(**mercado_dic2)|Produtos.objects.all().filter(**mercado_dic3)|Produtos.objects.all().filter(**mercado_dic4)|Produtos.objects.all().filter(**mercado_dic5)|Produtos.objects.all().filter(**mercado_dic6)|Produtos.objects.all().filter(**mercado_dic7)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


def feijao(request):
    produtos_list = Produtos.objects.all().filter(categoria='feijao')
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})


def arroz(request):
    produtos_list = Produtos.objects.all().filter(categoria='arroz')
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})


def macarrao(request):
    produtos_list = Produtos.objects.all().filter(categoria='macarrao')
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})


def sal(request):
    produtos_list = Produtos.objects.all().filter(categoria='sal')
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})


def molho_tomate(request):
    produtos_list = Produtos.objects.all().filter(categoria='molho de tomate')
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})


def farinha_trigo(request):
    produtos_list = Produtos.objects.all().filter(categoria='farinha')
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})

def cafe(request):
    produtos_list = Produtos.objects.all().filter(categoria='cafe')
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})

def detergente(request):
    produtos_list = Produtos.objects.all().filter(categoria='detergente')

    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})

def contato(request):
    return render(request, 'contato.html')

def mercado(request):
    mercados = {'mercado': 'Bistek', 'mercado': 'Fort Atacadista'}
    produtos_list = Produtos.objects.all().filter(**mercados)
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})
    
    