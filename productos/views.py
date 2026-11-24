"""Vistas del catálogo de productos."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def lista_productos(request: HttpRequest) -> HttpResponse:
    """Muestra la vista inicial del catálogo de productos."""
    return render(request, 'productos/lista.html')
