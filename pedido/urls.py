from django.urls import path
from .views import *

urlpatterns = [

    path('', pedido, name='pedido'),


]