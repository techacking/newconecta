from django.urls import path
from .views import *

urlpatterns = [

    path('', agenda, name='agenda'),

]