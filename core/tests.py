"""Pruebas de humo para verificar las rutas base y la landing page."""

from django.test import TestCase
from django.urls import reverse


class BaseRoutesSmokeTests(TestCase):
    """Comprueba que las vistas iniciales y la landing respondan correctamente."""

    def test_base_pages_return_200(self) -> None:
        url_names = [
            'core:home',
            'productos:lista',
            'pedidos:lista',
            'usuarios:perfil',
        ]
        for url_name in url_names:
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)

    def test_landing_page_contains_expected_sections(self) -> None:
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Favoritos de temporada.')
        self.assertContains(response, 'Un espacio para buena compañía.')
        self.assertContains(response, 'Latte Clásico')
        self.assertContains(response, 'Pecado de Chocolate')
        self.assertContains(response, 'img/logo-pecados.png')
        self.assertEqual(len(response.context['featured_products']), 4)
