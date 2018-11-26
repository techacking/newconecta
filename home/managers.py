from django.db import models
from django.db.models import Max, Avg, Min, Count


class OrcamentoManager(models.Manager):
    def todosorcamento(self):
        return self.all().aggregate(Count('id'))['id__count']