"""Rutas de la aplicación core (páginas generales del sitio)."""

from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
]
