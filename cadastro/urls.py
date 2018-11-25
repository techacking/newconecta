from django.urls import path
from .views import *

urlpatterns = [

    path('', cadastro, name='cadastro'),

    path('usuario_list/', usuarioList.as_view(), name='usuario_list'),
    path('usuario_create/', usuarioCreate.as_view(), name='usuario_create'),
    path('usuario_update/<int:pk>/', usuarioUpdate.as_view(), name='usuario_update'),
    path('usuario_delete/<int:pk>/', usuarioDelete.as_view(), name='usuario_delete'),

    path('perfil_list/', perfilList.as_view(), name='perfil_list'),
    path('perfil_create/', perfilCreate.as_view(), name='perfil_create'),
    path('perfil_update/<int:pk>/', perfilUpdate.as_view(), name='perfil_update'),
    path('perfil_delete/<int:pk>/', perfilDelete.as_view(), name='perfil_delete'),

    path('cliente_list/', clienteList.as_view(), name='cliente_list'),
    path('cliente_create/', clienteCreate.as_view(), name='cliente_create'),
    path('cliente_update/<int:pk>/', clienteUpdate.as_view(), name='cliente_update'),
    path('cliente_delete/<int:pk>/', clienteDelete.as_view(), name='cliente_delete'),

    path('tiposala_list/', tiposalaList.as_view(), name='tiposala_list'),
    path('tiposala_create/', tiposalaCreate.as_view(), name='tiposala_create'),
    path('tiposala_update/<int:pk>/', tiposalaUpdate.as_view(), name='tiposala_update'),
    path('tiposala_delete/<int:pk>/', tiposalaDelete.as_view(), name='tiposala_delete'),

    path('arquivo_list/', arquivoList.as_view(), name='arquivo_list'),
    path('arquivo_create/', arquivoCreate.as_view(), name='arquivo_create'),
    path('arquivo_update/<int:pk>/', arquivoUpdate.as_view(), name='arquivo_update'),
    path('arquivo_delete/<int:pk>/', arquivoDelete.as_view(), name='arquivo_delete'),

    path('boleto_list/', boletoList.as_view(), name='boleto_list'),
    path('boleto_create/', boletoCreate.as_view(), name='boleto_create'),
    path('boleto_update/<int:pk>/', boletoUpdate.as_view(), name='boleto_update'),
    path('boleto_delete/<int:pk>/', boletoDelete.as_view(), name='boleto_delete'),

    path('condicao_list/', condicaoList.as_view(), name='condicao_list'),
    path('condicao_create/', condicaoCreate.as_view(), name='condicao_create'),
    path('condicao_update/<int:pk>/', condicaoUpdate.as_view(), name='condicao_update'),
    path('condicao_delete/<int:pk>/', condicaoDelete.as_view(), name='condicao_delete'),

    path('contato_list/', contatoList.as_view(), name='contato_list'),
    path('contato_create/', contatoCreate.as_view(), name='contato_create'),
    path('contato_update/<int:pk>/', contatoUpdate.as_view(), name='contato_update'),
    path('contato_delete/<int:pk>/', contatoDelete.as_view(), name='contato_delete'),

    path('endereco_list/', enderecoList.as_view(), name='endereco_list'),
    path('endereco_create/', enderecoCreate.as_view(), name='endereco_create'),
    path('endereco_update/<int:pk>/', enderecoUpdate.as_view(), name='endereco_update'),
    path('endereco_delete/<int:pk>/', enderecoDelete.as_view(), name='endereco_delete'),

    path('evento_list/', eventoList.as_view(), name='evento_list'),
    path('evento_create/', eventoCreate.as_view(), name='evento_create'),
    path('evento_update/<int:pk>/', eventoUpdate.as_view(), name='evento_update'),
    path('evento_delete/<int:pk>/', eventoDelete.as_view(), name='evento_delete'),

    path('item_list/', itemList.as_view(), name='item_list'),
    path('item_create/', itemCreate.as_view(), name='item_create'),
    path('item_update/<int:pk>/', itemUpdate.as_view(), name='item_update'),
    path('item_delete/<int:pk>/', itemDelete.as_view(), name='item_delete'),

    path('mediaCliente_list/', mediaClienteList.as_view(), name='mediaCliente_list'),
    path('mediaCliente_create/', mediaClienteCreate.as_view(), name='mediaCliente_create'),
    path('mediaCliente_update/<int:pk>/', mediaClienteUpdate.as_view(), name='mediaCliente_update'),
    path('mediaCliente_delete/<int:pk>/', mediaClienteDelete.as_view(), name='mediaCliente_delete'),

    path('reservaCliente_list/', reservaList.as_view(), name='reserva_list'),
    path('reservaCliente_create/', reservaCreate.as_view(), name='reserva_create'),
    path('reservaCliente_update/<int:pk>/', reservaUpdate.as_view(), name='reserva_update'),
    path('reservaCliente_delete/<int:pk>/', reservaDelete.as_view(), name='reserva_delete'),

    path('sala_list/', salaList.as_view(), name='sala_list'),
    path('sala_create/', salaCreate.as_view(), name='sala_create'),
    path('sala_update/<int:pk>/', salaUpdate.as_view(), name='sala_update'),
    path('sala_delete/<int:pk>/', salaDelete.as_view(), name='sala_delete'),

    path('servicos_list/', servicosList.as_view(), name='servicos_list'),
    path('servicos_create/', servicosCreate.as_view(), name='servicos_create'),
    path('servicos_update/<int:pk>/', servicosUpdate.as_view(), name='servicos_update'),
    path('servicos_delete/<int:pk>/', servicosDelete.as_view(), name='servicos_delete'),
]