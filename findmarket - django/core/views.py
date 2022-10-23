from unicodedata import category
from django.shortcuts import render
from django.shortcuts import render
from .models import Produtos
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.http import HttpResponseRedirect


# Create your views here.


def cooper(request):
    mercado = {'mercado':'Cooper'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
def atacadao(request):
    mercado = {'mercado':'Atacadao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
def rede_top(request):
    mercado = {'mercado':'Rede Top'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
def giassi(request):
    mercado = {'mercado':'Giassi'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
def fort(request):
    mercado = {'mercado':'Fort Atacadista'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
def bistek(request):
    mercado = {'mercado':'Bistek'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
def sams(request):
    mercado = {'mercado':'Sams'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def endereco(request):
    return render(request, 'enderecos.html')

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
   return dict_3

mercados = []

def principal(request):
    produtos_list = Produtos.objects.all().order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


def feijao(request):
    produtos_list = Produtos.objects.all().filter(categoria='feijao').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


def arroz(request):
    produtos_list = Produtos.objects.all().filter(categoria='arroz').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


def macarrao(request):
    produtos_list = Produtos.objects.all().filter(categoria='macarrao').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


def sal(request):
    produtos_list = Produtos.objects.all().filter(categoria='sal').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


def molho_tomate(request):
    produtos_list = Produtos.objects.all().filter(categoria='molho de tomate').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})



def farinha_trigo(request):
    produtos_list = produtos_list.filter(categoria='farinha').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def cafe(request):
    produtos_list = Produtos.objects.all().filter(categoria='cafe').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def detergente(request):
    produtos_list = produtos_list.filter(categoria='detergente').order_by('preco_produto')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def contato(request):
    return render(request, 'contato.html')

def mercado(request):
    mercados = {'mercado': 'Bistek', 'mercado': 'Fort Atacadista'}
    produtos_list = Produtos.objects.all().filter(**mercados)
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'principal.html', {'produtos': produtos})
