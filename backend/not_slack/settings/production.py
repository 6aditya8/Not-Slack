from .base import *

DEBUG = False

CORS_ORIGIN_ALLOW_ALL = True

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, STATIC_PATH))
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, MEDIA_PATH))

INSTALLED_APPS += (
)
