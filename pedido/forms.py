from django.forms import ModelForm
from .models import *

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = [

            'status', 'datapedido', 'daraagenda', 'cliente', 'sala',

        ]

class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento
        fields = [

            'datapagamento', 'valor', 'formapagamento', 'status', 'cliente', 'pedido', 'boleto',

        ]

class OrcamentoForm(ModelForm):
    class Meta:
        model = Orcamento
        fields = [

            'valor', 'datageracao', 'pedido',

        ]