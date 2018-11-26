from cadastro.models import *
from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from home.managers import *
from django.urls import reverse

class Tabelapreco(models.Model):
    tipovalor = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sala = models.ForeignKey(Sala, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipovalor


class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, blank=False, null=False, on_delete=models.CASCADE)
    dataevento = models.DateTimeField('Data para Orcamento')
    sala = models.ForeignKey(Sala, blank=False, null=False, on_delete=models.CASCADE)
    montagem = models.TextField()
    valor = models.ForeignKey(Tabelapreco, blank=True, null=True, on_delete=models.CASCADE)

    objects = OrcamentoManager()

    def __str__(self):
        return self.cliente.nome

    def save(self, *args, **kwargs):
        super(Orcamento, self).save(*args, **kwargs)

        data = {
            'cliente': self.cliente.nome,
            'sala': self.sala,
            'quantidade': self.sala.capacidade,
            'idorcamento': self.id,
            'dataevento': self.dataevento,
            'montagem':self.montagem,
            'valor':self.valor.valor,
        }
        plain_text = render_to_string('orcamento/emails/neworcamento.txt', data)
        html_email = render_to_string('orcamento/emails/neworcamento.html', data)
        dest = self.cliente.email
        send_mail(
                'Orcamento - Conecta',
                plain_text,
                'smartbusinessmanagementnew@gmail.com',
                [dest],
                html_message=html_email,
                fail_silently=False,
        )
        render_to_string(template_name='orcamento/orcamento_list.html')

    def get_absolute_url(self):
        return reverse('orcamento_list')

class Pedido(models.Model):
    orcamento = models.ForeignKey(Orcamento, blank=False, null=False, on_delete=models.CASCADE)


class Pagamento(models.Model):
    datapagamento = models.DateTimeField()
    valor = models.FloatField()
    formapagamento = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, blank=False, null=False, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, blank=False, null=False, on_delete=models.CASCADE)
    boleto = models.ForeignKey(Boleto, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.status
