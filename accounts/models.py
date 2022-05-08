from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.categoria}"

class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField(blank=True)
    telefone = models.CharField(max_length=20,blank=True)
    descricao = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.nome}"


    

# Create your models here.
