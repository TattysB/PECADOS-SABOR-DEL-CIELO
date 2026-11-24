"""Vistas principales de la aplicación core."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Renderiza la landing page principal con favoritos destacados y métricas."""
    context = {
        'hero_stats': [
            {'value': '10K+', 'label': 'Clientes Felices'},
            {'value': '4.9 ★', 'label': 'Calificación Promedio'},
            {'value': '100%', 'label': 'Artesanal Cada Día'},
        ],
        'featured_products': [
            {
                'category': 'Café',
                'name': 'Latte Clásico',
                'notes': 'Cremoso. Suave. Irresistible.',
                'price': '$8.500',
                'image': 'img/menu-latte.jpg',
            },
            {
                'category': 'Cold Brew',
                'name': 'Vainilla Helada',
                'notes': 'Fresco. Dulce. Aromático.',
                'price': '$9.500',
                'image': 'img/menu-iced-vanilla.jpg',
            },
            {
                'category': 'Repostería',
                'name': 'Pecado de Chocolate',
                'notes': 'Intensa. Húmeda. Celestial.',
                'price': '$12.000',
                'image': 'img/menu-chocolate-cake.jpg',
            },
            {
                'category': 'Horneados',
                'name': 'Croissant de Almendras',
                'notes': 'Hojaldrado. Dorado. Delicado.',
                'price': '$7.900',
                'image': 'img/menu-croissant.jpg',
            },
        ],
    }
    return render(request, 'core/home.html', context)
