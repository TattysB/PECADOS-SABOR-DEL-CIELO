"""Vistas para la gestión de pedidos."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def lista_pedidos(request: HttpRequest) -> HttpResponse:
    """Muestra la vista inicial del módulo de pedidos."""
    return render(request, 'pedidos/lista.html')
