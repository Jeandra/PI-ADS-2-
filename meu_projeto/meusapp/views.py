from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


def home(request):
    return render(request, 'home.html')  # Supondo que você tenha um template chamado 'home.html'

def listar_ptodutos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_ptodutos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_ptodutos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_ptodutos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_ptodutos')
    return render(request, 'excluir_produto.html', {'produto': produto})

def buscar_produtos(request):
    if 'query' in request.GET:
        query = request.GET['query']
        # Realize a busca no banco de dados
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        # Se não houver consulta, retorne todos os produtos
        produtos = Produto.objects.all()
    
    # Renderize a página com os resultados da busca
    return render(request, 'buscar_produtos.html', {'produtos': produtos})