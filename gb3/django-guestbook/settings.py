from djangoappengine.settings_base import *

import os

DIRNAME = os.path.dirname(__file__)

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'
#SECRET_KEY = '1234567'

INSTALLED_APPS = (
    'djangoappengine',
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'guestbook',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

LOGIN_REDIRECT_URL = '/guestbook/'

ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(DIRNAME, 'media')
TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'),)

ROOT_URLCONF = 'urls'
