from msilib.schema import Media
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'pedro',
        'PASSWORD': 'root1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
