from django.db import models
from django.db.models import Max, Avg, Min, Count


class OrcamentoManager(models.Manager):
    def todosorcamento(self):
        return self.all().aggregate(Count('id'))['id__count']

class ClienteManager(models.Manager):
    def todoscliente(self):
        return self.all().aggregate(Count('id'))['id__count']

class PedidosManager(models.Manager):
    def todospedido(self):
        return self.all().aggregate(Count('id'))['id__count']

class UsuariosManager(models.Manager):
    def todosusuario(self):
        return self.all().aggregate(Count('id'))['id__count']

class PerfilManager(models.Manager):
    def todosperfil(self):
        return self.all().aggregate(Count('id'))['id__count']

class TiposalaManager(models.Manager):
    def todostipos(self):
        return self.all().aggregate(Count('id'))['id__count']
