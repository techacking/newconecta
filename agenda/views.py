from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus import DateTimePickerInput
from django.views import generic

from django.views import View
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
import json



class Autenticaagenda(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

class agenda(Autenticaagenda, ListView):
    model = Entre
    template_name = 'entre/agenda.html'

# ----------------------  LIST ----------------------------

class entreList(Autenticaagenda, ListView):
    model = Entre
    template_name = 'entre/entre_list.html'

# ----------------------- CREATE ---------------------------


class entreCreate(Autenticaagenda, CreateView):
    model = Entre
    fields = ['name', 'date', 'descricao', ]
    template_name = 'entre/entre_create.html'
    success_url = reverse_lazy('agenda')
    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = DateTimePickerInput(
            options={
                "format": "DD/MM/YYYY",
                "locale": "pt",
            }
        )
        return form


# ------------------------ UPDATE --------------------------

class entreUpdate(Autenticaagenda, UpdateView):
    model = Entre
    fields = ['name', 'date', 'descricao', ]
    template_name = 'entre/entre_update.html'
    success_url = reverse_lazy('agenda')
    def get_form(self):
        form = super().get_form()
        form.fields['date'].widget = DateTimePickerInput(
            options={
                "format": "DD/MM/YYYY",
                "locale": "pt",
            }
        )
        return form
# ------------------------- DELETE -------------------------

class entreDelete(Autenticaagenda, DeleteView):
    model = Entre
    template_name = 'entre/entre_delete.html'
    success_url = reverse_lazy('agenda')
