# coding:utf-8

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_example',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

REDIS_URL = '127.0.0.1:6379'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'TIMEOUT': 300,
        'OPTIONS': {
            'PASSWORD': '',
            'CLIENT_CLAS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser'

        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool'
    }
}

