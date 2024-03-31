FROM python:3.11.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update && \
    apk add --no-cache python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap


RUN pip install --upgrade pip

COPY . /app/

RUN pip install -r requirements.txt

RUN sed -i 's/ugettext_lazy/gettext_lazy/g' /usr/local/lib/python3.11/site-packages/taggit_serializer/serializers.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh