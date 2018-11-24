from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'login', 'senha', 'perfil',)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('perfil', )

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'inscricaoestadual', 'email', )

class CondicaoAdmin(admin.ModelAdmin):
        list_display = ('condicao',)

class ServicoAdmin(admin.ModelAdmin):
        list_display = ('tiposervico',)

class TipoSalaAdmin(admin.ModelAdmin):
        list_display = ('tipo', )

admin.site.register(Usuario, UsuarioAdmin ),
admin.site.register(Perfil, PerfilAdmin ),
admin.site.register(Cliente, ClienteAdmin ),
admin.site.register(TipoSala, TipoSalaAdmin),
admin.site.register(Sala),
admin.site.register(Condicao, CondicaoAdmin),
admin.site.register(Contato),
admin.site.register(Servicos, ServicoAdmin),