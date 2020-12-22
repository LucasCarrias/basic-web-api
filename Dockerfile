FROM python:3.8-alpine

LABEL Author="lucascarrias@outlook.com"

ENV PYTHONBUFFERED 1

RUN apk update \
    && python -m pip install -U --force-reinstall pip \
    && apk add --no-cache libffi-dev openssl-dev python3-dev\
    && apk add --no-cache gcc libc-dev zlib zlib-dev postgresql-dev

RUN mkdir app
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic -c --no-input