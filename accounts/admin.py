from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'telefone', 'categoria']
    list_display_links = ['categoria']
    list_editable = ['nome','sobrenome', 'telefone']
    list_filter = ['nome', 'sobrenome', 'telefone']
    list_per_page = 10
    search_fields = ['nome', 'sobrenome','telefone']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']
    list_per_page = 10
    search_fields = ['categoria']


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
# Register your models here.
