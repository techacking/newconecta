from django.contrib import admin
from .models import *

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('status', 'datapedido', 'dataagenda', 'cliente', 'sala', )

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('datapagamento', 'valor', 'formapagamento', 'status', 'cliente', 'pedido', 'boleto', )

class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('valor', 'datageracao', 'pedido', )

admin.site.register(Pedido, PedidoAdmin ),
admin.site.register(Pagamento, PagamentoAdmin),
admin.site.register(Orcamento, OrcamentoAdmin),