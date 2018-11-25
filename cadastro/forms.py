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

class Arquivo(ModelForm):
    class Meta:
        model = Arquivo
        fields = ['evento', 'titulo', 'formato', 'caminho']

class Boleto(ModelForm):
    class Meta:
        model = Boleto
        fields = ['vencimento', 'valor', 'taxa', 'codigobarra', 'cliente']

class Condicao(ModelForm):
    class Meta:
        model = Condicao
        fields = ['condicao']

class Contato(ModelForm):
    class Meta:
        model = Contato
        fields = ['ddd', 'telefone', 'tipo', 'cliente']

class Endereco(ModelForm):
    class Meta:
        model = Endereco
        fields = ['endereco', 'numero', 'cidade', 'estado', 'logradouro', 'cep', 'bairro', 'cliente']

class Evento(ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'tipo', 'item', 'reserva']

class Item(ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'valor']

class MediaCliente(ModelForm):
    class Meta:
        model = MediaCliente
        fields = ['site', 'foto', 'cliente']

class Reserva(ModelForm):
    class Meta:
        model = Reserva
        fields = ['entrada', 'saida', 'descricaoReserva']

class Sala(ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'capacidade', 'status', 'tipo']