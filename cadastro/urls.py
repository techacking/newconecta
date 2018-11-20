from django.urls import path
from .views import *

urlpatterns = [

    path('', cadastro, name='cadastro'),

    path('usuario_list/', usuarioList.as_view(), name='usuario_list'),
    path('usuario_create/', usuarioCreate.as_view(), name='usuario_create'),
    path('usuario_update/<int:pk>/', usuarioUpdate.as_view(), name='usuario_update'),
    path('usuario_delete/<int:pk>/', usuarioDelete.as_view(), name='usuario_delete'),

]