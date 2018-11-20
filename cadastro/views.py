from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

@login_required
def cadastro(request):
    return render(request, 'cadastro.html')

class Autentica(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


# ----------------------  LIST ----------------------------

class usuarioList(Autentica, ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'

class perfilList(Autentica, ListView):
    model = Perfil
    template_name = 'perfil/perfil_list.html'

class clienteList(Autentica, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'

# ----------------------- CREATE ---------------------------

class usuarioCreate(Autentica, CreateView):
    model = Usuario
    fields = ['nome', 'login', 'senha', 'perfil', ]
    template_name = 'usuario/usuario_create.html'
    success_url = reverse_lazy('usuario_list')

class perfilCreate(Autentica, CreateView):
    model = Perfil
    fields = ['perfil', ]
    template_name = 'perfil/perfil_create.html'
    success_url = reverse_lazy('perfil_list')

class clienteCreate(Autentica, CreateView):
    model = Cliente
    fields = ['nome', 'cnpj', 'inscricaoestadual', 'email', ]
    template_name = 'cliente/cliente_create.html'
    success_url = reverse_lazy('cliente_list')

# ------------------------ UPDATE --------------------------

class usuarioUpdate(Autentica, UpdateView):
    model = Usuario
    fields = ['nome', 'login', 'senha', 'perfil', ]
    template_name = 'usuario/usuario_update.html'
    success_url = reverse_lazy('usuario_list')

class perfilUpdate(Autentica, UpdateView):
    model = Perfil
    fields = ['perfil', ]
    template_name = 'perfil/perfil_update.html'
    success_url = reverse_lazy('perfil_list')

class clienteUpdate(Autentica, UpdateView):
    model = Cliente
    fields = ['nome', 'cnpj', 'inscricaoestadual', 'email', ]
    template_name = 'cliente/cliente_update.html'
    success_url = reverse_lazy('cliente_list')

# ------------------------- DELETE -------------------------

class usuarioDelete(Autentica, DeleteView):
    model = Usuario
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario_list')

class perfilDelete(Autentica, DeleteView):
    model = Perfil
    template_name = 'perfil/perfil_delete.html'
    success_url = reverse_lazy('perfil_list')

class clienteDelete(Autentica, DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('cliente_list')


