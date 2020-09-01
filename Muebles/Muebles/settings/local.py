from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TestingDB',
        'USER':'Muebles',
        'PASSWORD':'muebles2020',
        'HOST':'localhost'
    }
}