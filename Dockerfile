FROM python:3.10-slim
# FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

COPY wait-for-it.sh /code/wait-for-it.sh
RUN chmod +x /code/wait-for-it.sh
RUN chmod +x /code/mysite/manage.py



# # Используем внешний образ, который вы запушили в Docker Hub
# FROM lemon1964/mysite:latest

# # Устанавливаем рабочую директорию
# WORKDIR /code

# # Порты, которые будут слушать контейнер
# EXPOSE 8000

