from django.shortcuts import render
from .models import Produtos
from django.core.paginator import Paginator
from .filters import ProductFilter


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def endereco(request):
    return render(request, 'enderecos.html')


def principal(request):
    produtos_list = Produtos.objects.all()
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
