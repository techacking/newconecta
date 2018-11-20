from django.forms import ModelForm
from .models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [

            'nome', 'login', 'senha', 'perfil',

        ]