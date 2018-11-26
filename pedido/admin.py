from django.contrib import admin
from .models import *

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('orcamento', )

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('datapagamento', 'valor', 'formapagamento', 'status', 'cliente', 'pedido', 'boleto', )

class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'dataevento', 'sala', 'montagem', 'valor',)

class TabelaprecoAdmin(admin.ModelAdmin):
    list_display = ('tipovalor', 'valor', 'sala',)

admin.site.register(Pedido, PedidoAdmin ),
admin.site.register(Pagamento, PagamentoAdmin),
admin.site.register(Orcamento, OrcamentoAdmin),
admin.site.register(Tabelapreco, TabelaprecoAdmin),