from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'login', 'senha', 'perfil',)

admin.site.register(Usuario, UsuarioAdmin ),
