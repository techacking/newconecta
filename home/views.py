from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import *
from pedido.models import *

# Create your views here.


class Autentica(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class Home(Autentica, View):
    def get(self, request):
        data = {}
        data['total'] = Orcamento.objects.todosorcamento()
        data['cliente'] = Cliente.objects.todoscliente()
        data['usuario'] = Usuario.objects.todosusuario()
        data['perfil'] = Perfil.objects.todosperfil()
        data['tiposala'] = TipoSala.objects.todostipos()
        return render(request, 'home/home.html', data)
