FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt || true
RUN echo "Installing dependencies..." && pip install -r requirements.txt

COPY . /code/

COPY wait-for-it.sh /code/wait-for-it.sh
RUN chmod +x /code/wait-for-it.sh
RUN chmod +x /code/mysite/manage.py


CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:10000"]
# CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]

# # Использование gunicorn для продакшн
# ENV PYTHONPATH="/code"
# CMD ["gunicorn", "mysite.mysite.wsgi:application", "--bind", "0.0.0.0:8000"]






# # Используем внешний образ из Docker Hub
# FROM lemon1964/mysite:latest

# # Устанавливаем рабочую директорию
# WORKDIR /code

# # Порты, которые будут слушать контейнер
# EXPOSE 8000

# CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]

