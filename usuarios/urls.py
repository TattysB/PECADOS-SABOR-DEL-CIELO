"""Rutas de la aplicación usuarios."""

from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.perfil_usuario, name='perfil'),
]
