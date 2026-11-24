"""
Configuración principal de Django para el proyecto Pecados Sabor del Cielo.

Generado con Django 6.1.3 y adaptado para cargar variables de entorno
desde `.env`, servir plantillas/estáticos/medios globales y registrar
las aplicaciones locales del proyecto.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Directorio raíz del proyecto (donde vive manage.py).
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga variables de entorno desde el archivo .env si existe.
load_dotenv(BASE_DIR / '.env')


# Seguridad y entorno
# ------------------------------------------------------------------------------
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-^i6s2^kgy#x=(9fm^wvmervyij(*!wq*a+=-&@rs+ai2(h9eyy',
)

DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
    if host.strip()
]


# Definición de aplicaciones
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # Agrega aquí paquetes externos (p. ej. rest_framework, crispy_forms).
]

LOCAL_APPS = [
    'core.apps.CoreConfig',
    'productos.apps.ProductosConfig',
    'pedidos.apps.PedidosConfig',
    'usuarios.apps.UsuariosConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Plantillas compartidas globales (base.html, partials, etc.).
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Base de datos
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validación de contraseñas
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# ------------------------------------------------------------------------------
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'es-co')

TIME_ZONE = os.getenv('TIME_ZONE', 'America/Bogota')

USE_I18N = True

USE_TZ = True


# Archivos estáticos (CSS, JavaScript, imágenes del sitio) y medios subidos
# ------------------------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Correo electrónico (consola en desarrollo)
# ------------------------------------------------------------------------------
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
