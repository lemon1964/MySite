import os
import dj_database_url
from .base import *

DEBUG = False

ADMINS = [
    ('Usermhan', 'Usermhan@yandex.ru'),
]

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'mysite.com']с
ALLOWED_HOSTS = ['.mysite.com']

# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),  # Название базы данных
        'USER': os.getenv('POSTGRES_USER'),  # Имя пользователя
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),  # Пароль
        'HOST': os.getenv('DB_HOST', 'db'),  # Указываем хост базы данных (или 'db' для локальных контейнеров)
        'PORT': os.getenv('DB_PORT', 5432),  # Порт базы данных (по умолчанию 5432)
    }
}

# Продакшн настройки Redis
REDIS_HOST = config('REDIS_HOST')  # Имя сервиса Redis из Docker Compose
REDIS_PORT = config('REDIS_PORT')
REDIS_DB = config('REDIS_DB')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(REDIS_HOST, REDIS_PORT)],
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}',
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# Добавьте конфигурацию для Celery
CELERY_BROKER_URL = config('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
