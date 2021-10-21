FROM python:rc-slim-buster

WORKDIR /app

COPY requierements.txt /app/

RUN pip install -r requierements.txt