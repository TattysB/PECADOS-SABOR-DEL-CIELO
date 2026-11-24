"""Vistas para autenticación y perfiles de usuarios."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def perfil_usuario(request: HttpRequest) -> HttpResponse:
    """Muestra la vista inicial del módulo de usuarios."""
    return render(request, 'usuarios/perfil.html')
