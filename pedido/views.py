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
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def pedido(request):
    return render(request, 'pedido.html')

class Autenticapedido(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

# ----------------------  LIST ----------------------------

class orcamentoList(Autenticapedido, ListView):
    model = Orcamento
    template_name = 'orcamento/orcamento_list.html'

class pedidoList(Autenticapedido, ListView):
    model = Pedido
    template_name = 'pedido/pedido_list.html'

# ----------------------- CREATE ---------------------------

class orcamentoCreate(Autenticapedido, CreateView):
    model = Orcamento
    fields = ['cliente', 'dataevento', 'sala', 'montagem', ]
    template_name = 'orcamento/orcamento_create.html'
    success_url = reverse_lazy('orcamento_list')

class pedidoCreate(Autenticapedido, CreateView):
    model = Pedido
    fields = ['cliente', 'dataevento', 'sala', 'montagem', ]
    template_name = 'pedido/pedido_create.html'
    success_url = reverse_lazy('pedido_list')

# ------------------------ UPDATE --------------------------

class orcamentoUpdate(Autenticapedido, UpdateView):
    model = Orcamento
    fields = ['cliente', 'dataevento', 'sala', 'montagem', ]
    template_name = 'orcamento/orcamento_update.html'
    success_url = reverse_lazy('orcamento_list')

class pedidoUpdate(Autenticapedido, UpdateView):
    model = Pedido
    fields = ['orcamento']
    template_name = 'pedido/pedido_update.html'
    success_url = reverse_lazy('perfil_list')

# ------------------------- DELETE -------------------------

class orcamentoDelete(Autenticapedido, DeleteView):
    model = Orcamento
    template_name = 'orcamento/orcamento_delete.html'
    success_url = reverse_lazy('orcamento_list')

class pedidoDelete(Autenticapedido, DeleteView):
    model = Pedido
    template_name = 'pedido/pedido_delete.html'
    success_url = reverse_lazy('pedido_list')


