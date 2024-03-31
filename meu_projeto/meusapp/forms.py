from django import forms
from meusapp.models import Produto
from django.shortcuts import render 

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'imagem']