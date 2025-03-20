# import celery
from .celery import app as celery_app

__all__ = ['celery_app']
# # Измените импорт celery на celery_app
# from .celery import app as celery_app

# __all__ = ['celery']
