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

class ArquivoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'titulo', 'formato', 'caminho')

class  BoletoAdmin(admin.ModelAdmin):
    list_display = ('vencimento', 'valor', 'taxa', 'codigobarra', 'cliente')

class  CondicaoAdmin(admin.ModelAdmin):
    list_display = ('condicao',)

class  ContatoAdmin(admin.ModelAdmin):
    list_display = ('ddd', 'telefone', 'tipo', 'cliente')

class  EnderecoAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'numero', 'cidade', 'estado', 'logradouro', 'cep', 'bairro', 'cliente')

class  EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'item', 'reserva',)

class  ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')

class  MediaClienteAdmin(admin.ModelAdmin):
    list_display = ('site', 'foto', 'cliente')

class  ReservaAdmin(admin.ModelAdmin):
    list_display = ('entrada', 'saida', 'descricaoReserva')

class  SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade', 'status', 'tipo')


admin.site.register(Usuario, UsuarioAdmin ),
admin.site.register(Perfil, PerfilAdmin ),
admin.site.register(Cliente, ClienteAdmin ),
admin.site.register(TipoSala, TipoSalaAdmin),
admin.site.register(Sala),
admin.site.register(Condicao, CondicaoAdmin),
admin.site.register(Contato),
admin.site.register(Servicos, ServicoAdmin),