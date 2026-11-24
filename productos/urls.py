"""Rutas de la aplicación productos (catálogo)."""

from django.urls import path

from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista'),
]
