
FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt || true

COPY . /code/

RUN chmod +x /code/mysite/manage.py
RUN chmod +x /code/mysite/db.sqlite3



# # Взять официальный базовый образ Python платформы Docker
# FROM python:3.10.6

# # Задать переменные среды
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Задать рабочий каталог
# WORKDIR /code

# # Установить зависимости
# RUN pip install --upgrade pip
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt

# # Copy the Django project
# COPY . /code/

# # Копировать bash-скрипт wait-for-it.sh и предоставить ему права на выполнение
# COPY wait-for-it.sh /code/wait-for-it.sh
# RUN chmod +x /code/wait-for-it.sh
# RUN chmod +x /code/mysite/manage.py
# # RUN chmod -R 755 /code/mysite/django_error

# # Задать команду для запуска сервера Django
# # CMD ["./wait-for-it.sh", "db:5432", "--", "python3", "/code/mysite/manage.py", "runserver", "0.0.0.0:8000"]
# # CMD ["celery", "-A", "mysite.config", "-l", "info"]