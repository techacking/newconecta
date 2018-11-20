from django.db import models

# Create your models here.

class Perfil(models.Model):
    perfil = models.CharField(max_length=50)

    def __str__(self):
        return self.perfil


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    perfil = models.ForeignKey(Perfil, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    cnpj = models.CharField(max_length=30)
    inscricaoestadual = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=False)

    def __str__(self):
        return self.nome
