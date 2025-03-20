from .base import *

DEBUG = False

ADMINS = [
    ('Usermhan', 'Usermhan@yandex.ru'),
]

ALLOWED_HOSTS = ['.mysite.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': env('POSTGRES_DB'),
       'USER': env('POSTGRES_USER'),
       'PASSWORD': env('POSTGRES_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
   }
}

# Продакшн настройки Redis
REDIS_HOST = env('REDIS_HOST')  # Имя сервиса Redis из Docker Compose
REDIS_PORT = env
REDIS_DB = env('REDIS_DB')

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
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
