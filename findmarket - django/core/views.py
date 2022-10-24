from unicodedata import category
from django.shortcuts import render
from django.shortcuts import render
from .models import Produtos
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.http import HttpResponseRedirect


# Create your views here.

#---------------cooper
def cooper(request):
    mercado = {'mercado':'Cooper'}
    produtos_list = Produtos.objects.all().filter(**mercado).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def cooperfeijao(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'feijao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
    
def cooperarroz(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'arroz'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def coopermacarrao(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'macarrao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def coopermolho(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'molho de tomate'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def cooperpapel(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'papel higienico'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def coopersal(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'sal'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def cooperdetergente(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'detergente'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def cooperfarinha(request):
    mercado = {'mercado':'Cooper'}
    categoria = {'categoria':'farinha'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_cooper.html', {'produtos': produtos, 'meu_filtro': meu_filtro})



#---------------atacadao
def atacadao(request):
    mercado = {'mercado':'Atacadao'}
    produtos_list = Produtos.objects.all().filter(**mercado).order_by('price_weight_volume')
    
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def atacadaofeijao(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'feijao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
    
def atacadaoarroz(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'arroz'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def atacadaomacarrao(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'macarrao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def atacadaomolho(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'molho de tomate'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def atacadaopapel(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'papel higienico'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def atacadaosal(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'sal'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def atacadaodetergente(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'detergente'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def atacadaofarinha(request):
    mercado = {'mercado':'Atacadao'}
    categoria = {'categoria':'farinha'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_atacadao.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

#---------------rede
def rede(request):
    mercado = {'mercado':'Rede Top'}
    produtos_list = Produtos.objects.all().filter(**mercado).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def redefeijao(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'feijao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
    
def redearroz(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'arroz'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def redemacarrao(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'macarrao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def redemolho(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'molho de tomate'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def redepapel(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'papel higienico'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def redesal(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'sal'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def rededetergente(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'detergente'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def redefarinha(request):
    mercado = {'mercado':'Rede Top'}
    categoria = {'categoria':'farinha'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_rede.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

#---------------giassi
def giassi(request):
    mercado = {'mercado':'Giassi'}
    produtos_list = Produtos.objects.all().filter(**mercado).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def giassifeijao(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'feijao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
    
def giassiarroz(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'arroz'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def giassimacarrao(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'macarrao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def giassimolho(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'molho de tomate'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def giassipapel(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'papel higienico'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def giassisal(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'sal'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def giassidetergente(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'detergente'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def giassifarinha(request):
    mercado = {'mercado':'Giassi'}
    categoria = {'categoria':'farinha'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_giassi.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


#---------------fort
def fort(request):
    mercado = {'mercado':'Fort Atacadista'}
    produtos_list = Produtos.objects.all().filter(**mercado).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)
    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def fortfeijao(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'feijao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
    
def fortarroz(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'arroz'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def fortmacarrao(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'macarrao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def fortmolho(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'molho de tomate'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def fortpapel(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'papel higienico'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def fortsal(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'sal'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def fortdetergente(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'detergente'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def fortfarinha(request):
    mercado = {'mercado':'Fort Atacadista'}
    categoria = {'categoria':'farinha'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_fort.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

# -------------bistek
    
def bistek(request):
    mercado = {'mercado':'Bistek'}
    produtos_list = Produtos.objects.all().filter(**mercado).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def bistekfeijao(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'feijao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
    
def bistekarroz(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'arroz'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def bistekmacarrao(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'macarrao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def bistekmolho(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'molho de tomate'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def bistekpapel(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'papel higienico'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def bisteksal(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'sal'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def bistekdetergente(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'detergente'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def bistekfarinha(request):
    mercado = {'mercado':'Bistek'}
    categoria = {'categoria':'farinha'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_bistek.html', {'produtos': produtos, 'meu_filtro': meu_filtro})


# -------------sams
def sams(request):
    mercado = {'mercado':'Sams'}
    produtos_list = Produtos.objects.all().filter(**mercado).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def samsfeijao(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'feijao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
    
def samsarroz(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'arroz'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def samsmacarrao(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'macarrao'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def samsmolho(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'molho de tomate'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def samspapel(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'papel higienico'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def samssal(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'sal'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def samsdetergente(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'detergente'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})

def samsfarinha(request):
    mercado = {'mercado':'Sams'}
    categoria = {'categoria':'farinha'}
    produtos_list = Produtos.objects.all().filter(**mercado)
    produtos_list = produtos_list.filter(**categoria).order_by('price_weight_volume')
    meu_filtro = ProductFilter(request.GET, queryset=produtos_list)
    produtos_list = meu_filtro.qs
    paginator = Paginator(produtos_list, 12)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, '_sams.html', {'produtos': produtos, 'meu_filtro': meu_filtro})
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
    produtos_list = produtos_list.filter(categoria='detergente').order_by('price_weight_volume')
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
