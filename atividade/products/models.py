from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    codigo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)      

    def __str__(self):
        return f"{self.nome}"                  

class Fornecedor(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return f"{self.nome}"    


class Produto(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    codigo = models.CharField(max_length=50, unique=True, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    categoria = models.ManyToManyField(Categoria, related_name="categoria")
    fornecedor = models.ForeignKey(Fornecedor, related_name="fornecedor", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"    