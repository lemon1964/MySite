import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Создайте экземпляр Celery и укажите пространство имен для настроек.
app = Celery('mysite')

# Загрузите настройки из объекта настроек Django.
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object(settings, namespace='CELERY')

# Исключаем приложение courses из загружаемых приложений для Celery
# app.conf.exclude_modules = ('courses', 'chat', 'students')

# Автоматически обнаруживаем и загружаем задачи из приложений Django
app.autodiscover_tasks()

