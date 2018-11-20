from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'login', 'senha', 'perfil',)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('perfil', )
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'inscricaoestadual', 'email', )

admin.site.register(Usuario, UsuarioAdmin ),
admin.site.register(Perfil, PerfilAdmin ),
admin.site.register(Cliente, ClienteAdmin ),
