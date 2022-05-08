from django.db import models
from django.contrib.auth import get_user_model
from pathlib import Path
from django import forms


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.categoria}"


class Contato(models.Model):
    user = models.ForeignKey(get_user_model(),
            on_delete=models.CASCADE,
            related_name='contato',
            default=None)
    imagem = models.ImageField(blank=True,upload_to='fotos/%Y/%m/%d',)
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20,blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome}"

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('id','user')


    

# Create your models here.
