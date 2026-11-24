# Bitácora de Cambios — Pecados Sabor del Cielo

Registro cronológico y documentado de cada avance técnico realizado en el proyecto.

---

## 2026-11-23 — Configuración inicial de la estructura Django

### Objetivo
Completar y estandarizar la estructura base del proyecto Django aprovechando el proyecto `config/` y las aplicaciones (`core`, `productos`, `pedidos`, `usuarios`) ya creadas.

### Archivos creados y modificados

1. **Control de versiones y entorno**
   - `.gitignore`: reglas para ignorar entornos virtuales, `.env`, `db.sqlite3`, `__pycache__/`, `staticfiles/` y archivos subidos en `media/`.
   - `.env.example` y `.env`: definición de variables de entorno locales (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `LANGUAGE_CODE`, `TIME_ZONE`).

2. **Configuración de Django (`config/`)**
   - `config/settings.py`:
     - Integración de `python-dotenv` para cargar variables desde `.env`.
     - Separación de `INSTALLED_APPS` en `DJANGO_APPS`, `THIRD_PARTY_APPS` y `LOCAL_APPS` (`core`, `productos`, `pedidos`, `usuarios`).
     - Registro de `templates/` en `TEMPLATES[0]['DIRS']`.
     - Configuración de idioma `es-co` y zona horaria `America/Bogota`.
     - Configuración de `STATICFILES_DIRS`, `STATIC_ROOT`, `MEDIA_URL` y `MEDIA_ROOT`.
   - `config/urls.py`: inclusión de rutas de las cuatro apps locales y soporte para archivos `media/` en `DEBUG`.

3. **Plantillas globales y recursos estáticos**
   - `templates/base.html`, `templates/partials/_navbar.html` y `templates/partials/_footer.html`.
   - `static/css/styles.css`, `static/js/main.js`, `static/img/.gitkeep` y `media/.gitkeep`.

4. **Enrutamiento, vistas, plantillas y pruebas iniciales por app**
   - `core/`: `urls.py`, `views.py`, `templates/core/home.html` y pruebas de humo en `core/tests.py`.
   - `productos/`: `urls.py`, `views.py`, `templates/productos/lista.html`.
   - `pedidos/`: `urls.py`, `views.py`, `templates/pedidos/lista.html`.
   - `usuarios/`: `urls.py`, `views.py`, `templates/usuarios/perfil.html`.

5. **Documentación**
   - `README.md`: guía de instalación, activación del entorno, ejecución y rutas.
   - `docs/ARQUITECTURA.md`: documentación completa de estructura, apps y convenciones.
   - `docs/BITACORA.md`: creación de esta bitácora de cambios.

### Verificación ejecutada
- `python manage.py check` — OK (`0 issues`).
- `python manage.py migrate` — OK (18 migraciones iniciales de Django aplicadas).
- `python manage.py test -v 2` — OK (`test_base_pages_return_200` validó HTTP 200 en `/`, `/productos/`, `/pedidos/` y `/usuarios/`).
- `git status -s` — OK (`.env`, `db.sqlite3` y `PECADOS-SABOR-DEL-CIELO/venv/` ignorados correctamente).

---

## 2026-11-23 — Implementación de Landing Page editorial y sistema de diseño

### Objetivo
Diseñar e implementar la landing page principal de **Pecados Sabor del Cielo** siguiendo la referencia visual editorial y aplicando exactamente la paleta de colores oficial (`#291C0E`, `#6E473B`, `#A78D78`, `#BEB5A9`, `#E1D4C2`).

### Archivos creados y modificados

1. **Sistema de diseño y estilos (`static/css/styles.css`)**
   - Definición de tokens CSS con los 5 tonos oficiales y superficies marfil derivadas.
   - Maquetación responsiva (desktop, tablet y móvil) para navbar fija con transición al scroll, Hero editorial con degradado, grilla de 4 tarjetas de menú, banda de Historia en 3 paneles, franja de 4 pilares, footer con boletín y notificación toast.

2. **Plantillas HTML y vistas**
   - `templates/base.html`: carga de tipografías `Playfair Display` y `Plus Jakarta Sans`, soporte `body_class` y `full_content` para páginas a ancho completo, y contenedor de toast.
   - `templates/partials/_navbar.html`: marca tipográfica `PECADOS / SABOR DEL CIELO`, navegación principal, ícono de bolsa con contador y menú móvil.
   - `templates/partials/_footer.html`: footer oscuro `#291C0E` con boletín interactivo, iconos sociales SVG y enlaces legales.
   - `core/templates/core/home.html` y `core/views.py`: estructura completa de la landing page con contexto dinámico para métricas (`hero_stats`) y productos destacados (`featured_products`).

3. **Interactividad (`static/js/main.js`)**
   - Cambio de apariencia de la barra de navegación al hacer scroll.
   - Apertura/cierre accesible del menú móvil.
   - Contador temporal de artículos y notificación toast al pulsar `+` en las tarjetas de favoritos.
   - Validación en cliente del formulario de suscripción al boletín.

4. **Activos fotográficos (`static/img/`)**
   - Generación e integración de 6 fotografías editoriales coherentes con la paleta: `hero-cafe.jpg`, `menu-latte.jpg`, `menu-iced-vanilla.jpg`, `menu-chocolate-cake.jpg`, `menu-croissant.jpg` y `story-table.jpg`.

5. **Pruebas y documentación**
   - `core/tests.py`: ampliación de pruebas para validar las secciones clave y los 4 productos destacados de la landing.
   - `docs/DISENO.md`: documentación completa de la paleta, tipografía, secciones e imágenes.
   - `README.md` y `docs/BITACORA.md`: actualizados con el nuevo documento de diseño y este registro.

### Verificación ejecutada
- `python manage.py check` — OK (`0 issues`).
- `python manage.py test -v 2` — OK (2 pruebas aprobadas: rutas base y secciones/productos destacados de la landing).

---

## 2026-11-23 — Integración del logo oficial en la barra de navegación

### Objetivo
Incorporar el logo oficial de **Pecados Sabor del Cielo** en la esquina superior izquierda junto al nombre de la marca y configurarlo como favicon del sitio.

### Archivos creados y modificados
- `static/img/logo-pecados.png`: copia del logo oficial proporcionado.
- `templates/partials/_navbar.html`: inclusión del logo circular a la izquierda de `PECADOS / SABOR DEL CIELO`.
- `templates/partials/_footer.html`: ajuste de contenedor `.brand__text` para mantener consistencia estructural.
- `templates/base.html`: configuración de `logo-pecados.png` como favicon.
- `static/css/styles.css`: estilos `.brand`, `.brand__logo` (circular `48x48px` con borde caramelo suave) y `.brand__text`.
- `core/tests.py`: validación de renderizado del logo en la landing.
- `docs/DISENO.md` y `docs/BITACORA.md`: documentación actualizada.
