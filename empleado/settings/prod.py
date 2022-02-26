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