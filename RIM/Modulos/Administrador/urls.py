from django.contrib import admin
from django.urls import path
from Modulos.Administrador.views import *

app_name = 'Administrador'
urlpatterns = [
    path('administrador/',Administrador.as_view(),name='administrador'),


]