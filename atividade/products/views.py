from django.shortcuts import render
from .models import Produto, Categoria, Fornecedor

# Create your views here.

def view_produtos(request):
  context = Produto.objects.all()
  return render(request, "produtos.html", {"produtos": context})

def view_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {"categorias": categorias})

def view_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "fornecedores.html", {"fornecedores": fornecedores})

def detalhes_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id) 
    return render(request, "detalhes_produto.html", {"produto": produto})