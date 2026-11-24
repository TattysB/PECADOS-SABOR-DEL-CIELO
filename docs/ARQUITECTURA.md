# Arquitectura del Proyecto — Pecados Sabor del Cielo

Este documento describe la organización de carpetas, módulos y configuraciones base del proyecto Django.

---

## 1. Estructura de directorios

```text
PECADOS SABOR DEL CIELO/
├── .env                         # Variables de entorno locales (ignorado por Git)
├── .env.example                 # Plantilla de variables de entorno
├── .gitignore                   # Reglas de exclusión para Git
├── README.md                    # Guía rápida de instalación y uso
├── requirements.txt             # Dependencias Python del proyecto
├── manage.py                    # Utilidad de línea de comandos de Django
├── config/                      # Configuración global del proyecto Django
│   ├── settings.py              # Ajustes generales (apps, BD, estáticos, .env)
│   ├── urls.py                  # Enrutamiento raíz y servicio de media en DEBUG
│   ├── wsgi.py                  # Punto de entrada WSGI
│   └── asgi.py                  # Punto de entrada ASGI
├── core/                        # App principal (inicio, vistas generales)
│   ├── templates/core/          # Plantillas propias de core
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── productos/                   # App de catálogo (productos, categorías, fotos)
│   ├── templates/productos/
│   ├── urls.py
│   └── views.py
├── pedidos/                     # App de pedidos (carrito, órdenes, estados)
│   ├── templates/pedidos/
│   ├── urls.py
│   └── views.py
├── usuarios/                    # App de usuarios (registro, login, perfiles)
│   ├── templates/usuarios/
│   ├── urls.py
│   └── views.py
├── templates/                   # Plantillas HTML compartidas por todo el sitio
│   ├── base.html                # Layout base HTML5
│   └── partials/
│       ├── _navbar.html         # Barra de navegación principal
│       └── _footer.html         # Pie de página global
├── static/                      # Archivos estáticos propios
│   ├── css/styles.css           # Hoja de estilos base
│   ├── js/main.js               # Script global base
│   └── img/                     # Imágenes estáticas del sitio (logos, iconos)
├── media/                       # Archivos subidos dinámicamente (fotos de productos)
└── docs/                        # Documentación técnica y bitácora de cambios
    ├── ARQUITECTURA.md
    └── BITACORA.md
```

---

## 2. Responsabilidad de cada aplicación

- **`config`**: Centraliza la configuración del proyecto (`settings.py`), las rutas raíz (`urls.py`) y los puntos de entrada de despliegue (`wsgi.py` / `asgi.py`). No contiene modelos de negocio.
- **`core`**: Páginas transversales del sitio (inicio, acerca de, contacto) y pruebas de humo globales.
- **`productos`**: Gestión del catálogo (categorías, productos, precios, disponibilidad e imágenes con `Pillow`).
- **`pedidos`**: Flujo de compra, carrito, registro de órdenes y seguimiento de estados.
- **`usuarios`**: Autenticación, registro, perfiles de cliente y permisos específicos.

---

## 3. Convenciones configuradas

### Variables de entorno (`.env`)
Se utiliza `python-dotenv` en `config/settings.py` para leer:
- `SECRET_KEY`: clave secreta de Django.
- `DEBUG`: modo de depuración (`True` en local, `False` en producción).
- `ALLOWED_HOSTS`: lista de hosts permitidos separados por coma.
- `LANGUAGE_CODE`: idioma por defecto (`es-co`).
- `TIME_ZONE`: zona horaria por defecto (`America/Bogota`).

### Plantillas (`templates/`)
- Las plantillas globales (layout base y parciales reutilizables) viven en `templates/`.
- Las plantillas específicas de cada app viven en `<app>/templates/<app>/` para evitar colisiones de nombres entre aplicaciones.

### Archivos estáticos (`static/`) y medios (`media/`)
- `STATICFILES_DIRS` apunta a `static/` durante el desarrollo.
- `STATIC_ROOT` apunta a `staticfiles/` para `collectstatic` en despliegue.
- `MEDIA_ROOT` apunta a `media/` y se sirve automáticamente en modo `DEBUG=True` desde `config/urls.py`.

### Control de versiones (`.gitignore`)
Se excluyen del repositorio entornos virtuales (`venv/`, `PECADOS-SABOR-DEL-CIELO/venv/`), secretos (`.env`), archivos compilados (`__pycache__/`), la base de datos local (`db.sqlite3`), `staticfiles/` y los archivos subidos en `media/` (conservando solo `media/.gitkeep`).
