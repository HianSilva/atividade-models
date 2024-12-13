from django.contrib import admin
from .models import Produto, Categoria, Fornecedor

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'descricao', 'preco', 'quantidade_estoque', 'data_criacao') 
    search_fields = ('codigo', 'nome')  
    list_filter = ('data_criacao',)  
    ordering = ('-data_criacao',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'descricao') 
    search_fields = ('codigo', 'nome')  
    list_filter = ('nome',)
    ordering = ('nome',)

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)

