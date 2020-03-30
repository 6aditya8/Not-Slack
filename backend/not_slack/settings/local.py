from .base import *

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

MEDIA_URL = 'http://127.0.0.1:8000/{}'.format(MEDIA_PATH)

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, STATIC_PATH))
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, MEDIA_PATH))

ALLOWED_HOSTS = (
    'localhost:8000'
)

SERVER_DOMAIN = "localhost:8000"

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
)
