from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'excluir_produto.html', {'produto': produto})