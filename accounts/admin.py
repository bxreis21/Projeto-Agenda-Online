from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['user','id','nome', 'sobrenome', 'telefone',]
    list_display_links = ['user','id','nome']
    list_filter = ['user']
    list_per_page = 10
    search_fields = ['user','nome', 'sobrenome','telefone']



admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
# Register your models here.
