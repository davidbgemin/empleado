from pathlib import Path

#  !* importando código del archivo base
from .base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# !* unipath: Modificando la configuración de la base de datos
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR.child('db.sqlite3'),
#     }
# }

# !* 1. configuración de base de datos para mysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'pruebadjango', # nombre de la bd
#         'USER': 'root',
#         'PASSWORD': '', # si no hay contraseña, dejar vacío
#         'HOST': 'localhost',
#         'PORT': '3306'
#     }
# }

# !* 2. configuración de base de datos para postgresql:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'davidbaila',
        'PASSWORD': 'davidbaila123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# !* 3. Configuración de la carpeta de archivos estáticos:
STATICFILES_DIRS = [BASE_DIR.child('static')]

# !* 4. Configuración de la carpeta de archivos multimedia:
# crear la carpeta media en la raíz del proyecto
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')