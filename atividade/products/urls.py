from django.urls import path
from .views import *

urlpatterns = [
    path('', view_produtos, name='lista_produtos'),
    path('produtos/<int:produto_id>/', detalhes_produto, name='detalhes_produto'),
    path('categorias/', view_categorias, name='lista_categorias'),
    path('fornecedores/', view_fornecedores, name='lista_fornecedores'),
]