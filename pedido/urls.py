from django.urls import path
from .views import *

urlpatterns = [

    path('', pedido, name='pedido'),

    path('orcamento_list/', orcamentoList.as_view(), name='orcamento_list'),
    path('orcamento_create/', orcamentoCreate.as_view(), name='orcamento_create'),
    path('orcamento_update/<int:pk>/', orcamentoUpdate.as_view(), name='orcamento_update'),
    path('orcamento_delete/<int:pk>/', orcamentoDelete.as_view(), name='orcamento_delete'),

    path('pedido_list/', pedidoList.as_view(), name='pedido_list'),
    path('pedido_create/', pedidoCreate.as_view(), name='pedido_create'),
    path('pedido_update/<int:pk>/', pedidoUpdate.as_view(), name='pedido_update'),
    path('pedido_delete/<int:pk>/', pedidoDelete.as_view(), name='pedido_delete'),

]