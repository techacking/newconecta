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

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = [
            'cliente', 'ddd', 'telefone', 'tipo'
                  ]

class SalaForm(ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'capacidade', 'status', 'tipo', ]

class TipoSala(ModelForm):
    class Meta:
        model = TipoSala
        fields = ['tipo', ]