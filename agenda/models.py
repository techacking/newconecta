from django.db import models
from django.shortcuts import render

# Create your models here.

class Entre(models.Model):
    name = models.CharField('Descricao do evento', max_length=100)
    date = models.DateTimeField('Data do Evento')
    descricao = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return render('agenda.html')