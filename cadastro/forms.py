from django.forms import ModelForm
from .models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [

            'nome', 'login', 'senha', 'perfil',

        ]

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = [

            'nome', 'cnpj', 'inscricaoestadual', 'email',

        ]

class perfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = [

            'perfil',

        ]