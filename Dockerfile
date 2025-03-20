FROM python:3.10.6

# Установим необходимые системные библиотеки для сборки uwsgi
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libssl-dev \
#     libpq-dev \
#     gcc \
#     && rm -rf /var/lib/apt/lists/*

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
