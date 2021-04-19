from django.contrib import admin
from .models import Categoria, Contato


# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    #  mostra todos os dados na listagem dos contatos no django admin

    list_display_links = ('id', 'nome', 'sobrenome')
    #  torna os atributos clicáveis

    #  list_filter = ('nome', 'sobrenome')
    #  adiciona um campo de filtragem

    list_per_page = 10
    #  mostra 10 registros por páginas

    search_fields = ('nome', 'sobrenome', 'telefone', 'email', 'categoria')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
