from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

@login_required
def cadastro(request):
    return render(request, 'cadastro.html')

class Autenticacad(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

# ----------------------  LIST ----------------------------

class usuarioList(Autenticacad, ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'

class perfilList(Autenticacad, ListView):
    model = Perfil
    template_name = 'perfil/perfil_list.html'

class clienteList(Autenticacad, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

class tiposalaList(Autenticacad, ListView):
    model = TipoSala
    template_name = 'tiposala/tiposala_list.html'

class arquivoList(Autenticacad, ListView):
    model = Arquivo
    template_name = 'arquivo/arquivo_list.html'


class boletoList(Autenticacad, ListView):
    model = Boleto
    template_name = 'boleto/boleto_list.html'

class condicaoList(Autenticacad, ListView):
    model = Condicao
    template_name = 'condicao/condicao_list.html'

class contatoList(Autenticacad, ListView):
    model = Contato
    template_name = 'contato/contato_list.html'

class enderecoList(Autenticacad, ListView):
    model = Endereco
    template_name = 'endereco/endereco_list.html'

class eventoList(Autenticacad, ListView):
    model = Evento
    template_name = 'evento/evento_list.html'

class itemList(Autenticacad, ListView):
    model = Item
    template_name = 'item/item_list.html'

class mediaClienteList(Autenticacad, ListView):
    model = MediaCliente
    template_name = 'mediaCliente/mediaCliente_list.html'

class reservaList(Autenticacad, ListView):
    model = Reserva
    template_name = 'reserva/reserva_list.html'

class salaList(Autenticacad, ListView):
    model = Sala
    template_name = 'sala/sala_list.html'

class servicosList(Autenticacad, ListView):
    model = Servicos
    template_name = 'servicos/servicos_list.html'


# ----------------------- CREATE ---------------------------

class usuarioCreate(Autenticacad, CreateView):
    model = Usuario
    fields = ['nome', 'login', 'senha', 'perfil', ]
    template_name = 'usuario/usuario_create.html'
    success_url = reverse_lazy('usuario_list')

class perfilCreate(Autenticacad, CreateView):
    model = Perfil
    fields = ['perfil']
    template_name = 'perfil/perfil_create.html'
    success_url = reverse_lazy('perfil_list')

class clienteCreate(Autenticacad, CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/cliente_create.html'
    success_url = reverse_lazy('cliente_list')

class tiposalaCreate(Autenticacad, CreateView):
    model = TipoSala
    fields = ['tipo', ]
    template_name = 'tiposala/tiposala_create.html'
    success_url = reverse_lazy('tiposala_list')

class arquivoCreate(Autenticacad, CreateView):
    model = Arquivo
    fields = ['caminho', 'titulo', 'formato', 'evento']
    template_name = 'arquivo/arquivo_create.html'
    success_url = reverse_lazy('arquivo_list')


class boletoCreate(Autenticacad, CreateView):
    model = Boleto
    fields = ['vencimento', 'valor', 'taxa', 'codigobarra', 'cliente']
    template_name = 'boleto/boleto_create.html'
    success_url = reverse_lazy('boleto_list')

class condicaoCreate(Autenticacad, CreateView):
    model = Condicao
    fields = ['condicao']
    template_name = 'condicao/condicao_create.html'
    success_url = reverse_lazy('condicao_list')

class contatoCreate(Autenticacad, CreateView):
    model = Contato
    fields = ['ddd', 'telefone', 'tipo', 'cliente']
    template_name = 'contato/contato_create.html'
    success_url = reverse_lazy('contato_list')


class enderecoCreate(Autenticacad, CreateView):
    model = Endereco
    fields = ['endereco', 'numero', 'cidade', 'estado', 'logradouro', 'cep', 'bairro', 'cliente' ]
    template_name = 'endereco/endereco_create.html'
    success_url = reverse_lazy('endereco_list')

class eventoCreate(Autenticacad, CreateView):
    model = Evento
    fields = ['titulo', 'tipo', 'item', 'reserva']
    template_name = 'evento/evento_create.html'
    success_url = reverse_lazy('evento_list')

class itemCreate(Autenticacad, CreateView):
    model = Item
    fields = ['nome', 'valor']
    template_name = 'item/item_create.html'
    success_url = reverse_lazy('item_list')

class mediaClienteCreate(Autenticacad, CreateView):
    model = MediaCliente
    fields = ['site', 'foto', 'cliente']
    template_name = 'mediaCliente/mediaCliente_create.html'
    success_url = reverse_lazy('mediaCliente_list')

class reservaCreate(Autenticacad, CreateView):
    model = Reserva
    fields = ['entrada', 'saida', 'descricaoReserva']
    template_name = 'reserva/reserva_create.html'
    success_url = reverse_lazy('reserva_list')

class salaCreate(Autenticacad, CreateView):
    model = Sala
    fields = ['nome', 'capacidade', 'status', 'tipo', ]
    template_name = 'sala/sala_create.html'
    success_url = reverse_lazy('sala_list')

class servicosCreate(Autenticacad, CreateView):
    model = Servicos
    fields = ['tiposervico']
    template_name = 'servicos/servicos_create.html'
    success_url = reverse_lazy('servicos_list')

# ------------------------ UPDATE --------------------------

class usuarioUpdate(Autenticacad, UpdateView):
    model = Usuario
    fields = ['nome', 'login', 'senha', 'perfil', ]
    template_name = 'usuario/usuario_update.html'
    success_url = reverse_lazy('usuario_list')

class perfilUpdate(Autenticacad, UpdateView):
    model = Perfil
    fields = ['perfil', ]
    template_name = 'perfil/perfil_update.html'
    success_url = reverse_lazy('perfil_list')

class clienteUpdate(Autenticacad, UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/cliente_update.html'
    success_url = reverse_lazy('cliente_list')

class tiposalaUpdate(Autenticacad, UpdateView):
    model = TipoSala
    fields = ['tipo', ]
    template_name = 'tiposala/tiposala_update.html'
    success_url = reverse_lazy('tiposala_list')

class arquivoUpdate(Autenticacad, UpdateView):
    model = Arquivo
    fields = ['caminho', 'titulo', 'formato', 'evento']
    template_name = 'arquivo/arquivo_update.html'
    success_url = reverse_lazy('arquivo_list')

class boletoUpdate(Autenticacad, UpdateView):
    model = Boleto
    fields = ['vencimento', 'valor', 'taxa', 'codigobarra', 'cliente',]
    template_name = 'boleto/boleto_update.html'
    success_url = reverse_lazy('boleto_list')

class condicaoUpdate(Autenticacad, UpdateView):
    model = Condicao
    fields = ['condicao']
    template_name = 'condicao/condicao_update.html'
    success_url = reverse_lazy('condicao_list')

class contatoUpdate(Autenticacad, UpdateView):
    model = Contato
    fields = ['ddd', 'telefone', 'tipo', 'cliente']
    template_name = 'contato/contato_update.html'
    success_url = reverse_lazy('contato_list')

class enderecoUpdate(Autenticacad, UpdateView):
    model = Endereco
    fields = ['endereco', 'numero', 'cidade', 'estado', 'logradouro', 'cep', 'bairro', 'cliente' ]
    template_name = 'endereco/endereco_update.html'
    success_url = reverse_lazy('endereco_list')

class eventoUpdate(Autenticacad, UpdateView):
    model = Evento
    fields = ['titulo', 'tipo', 'item', 'reserva']
    template_name = 'evento/evento_update.html'
    success_url = reverse_lazy('evento_list')

class itemUpdate(Autenticacad, UpdateView):
    model = Item
    fields = ['nome', 'valor']
    template_name = 'item/item_update.html'
    success_url = reverse_lazy('item_list')

class mediaClienteUpdate(Autenticacad, UpdateView):
    model = MediaCliente
    fields = ['site', 'foto', 'cliente']
    template_name = 'mediaCliente/,mediaCliente_update.html'
    success_url = reverse_lazy('mediaCliente_list')

class reservaUpdate(Autenticacad, UpdateView):
    model = Reserva
    fields = ['entrada', 'saida', 'descricaoReserva']
    template_name = 'reserva/reserva_update.html'
    success_url = reverse_lazy('reserva_list')

class salaUpdate(Autenticacad, UpdateView):
    model = Sala
    fields = ['nome', 'capacidade', 'status', 'tipo', ]
    template_name = 'sala/sala_update.html'
    success_url = reverse_lazy('sala_list')

class servicosUpdate(Autenticacad, UpdateView):
    model = Servicos
    fields = ['tiposervico']
    template_name = 'servicos/servicos_update.html'
    success_url = reverse_lazy('servicos_list')

# ------------------------- DELETE -------------------------

class usuarioDelete(Autenticacad, DeleteView):
    model = Usuario
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario_list')

class perfilDelete(Autenticacad, DeleteView):
    model = Perfil
    template_name = 'perfil/perfil_delete.html'
    success_url = reverse_lazy('perfil_list')

class clienteDelete(Autenticacad, DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('cliente_list')

class tiposalaDelete(Autenticacad, DeleteView):
    model = TipoSala
    template_name = 'tiposala/tiposala_delete.html'
    success_url = reverse_lazy('tiposala_list')

class arquivoDelete(Autenticacad, DeleteView):
    model = Arquivo
    template_name = 'arquivo/arquivo_delete.html'
    success_url = reverse_lazy('arquivo_list')

class boletoDelete(Autenticacad, DeleteView):
    model = Boleto
    template_name = 'boleto/boleto_delete.html'
    success_url = reverse_lazy('boleto_list')

class condicaoDelete(Autenticacad, DeleteView):
    model = Condicao
    template_name = 'condicao/condicao_delete.html'
    success_url = reverse_lazy('condicao_list')

class contatoDelete(Autenticacad, DeleteView):
    model = Contato
    template_name = 'contato/contato_delete.html'
    success_url = reverse_lazy('condicao_list')

class enderecoDelete(Autenticacad, DeleteView):
    model = Endereco
    template_name = 'endereco/endereco_delete.html'
    success_url = reverse_lazy('endereco_list')

class eventoDelete(Autenticacad, DeleteView):
    model = Evento
    template_name = 'evento/evento_delete.html'
    success_url = reverse_lazy('evento_list')

class itemDelete(Autenticacad, DeleteView):
    model = Item
    template_name = 'item/item_delete.html'
    success_url = reverse_lazy('item_list')

class mediaClienteDelete(Autenticacad, DeleteView):
    model = MediaCliente
    template_name = 'mediaCliente/mediaCliente_delete.html'
    success_url = reverse_lazy('mediaCliente_list')

class reservaDelete(Autenticacad, DeleteView):
    model = Reserva
    template_name = 'reserva/reserva_delete.html'
    success_url = reverse_lazy('reserva_list')

class salaDelete(Autenticacad, DeleteView):
    model = Sala
    template_name = 'sala/sala_delete.html'
    success_url = reverse_lazy('sala_list')

class servicosDelete(Autenticacad, DeleteView):
    model = Servicos
    template_name = 'servicos/servicos_delete.html'
    success_url = reverse_lazy('servicos_list')


