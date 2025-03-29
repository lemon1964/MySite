from .base import *

DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'mysite-web-vubo.onrender.com', 'localhost', '127.0.0.1']


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         'NAME': 'site',
#         'USER': 'posts',
#         'PASSWORD': '12345',
#     }
# }

# Локальные настройки Redis для mysite Educa
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Используйте нужную базу данных Redis
    }
}

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

