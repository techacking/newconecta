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

]