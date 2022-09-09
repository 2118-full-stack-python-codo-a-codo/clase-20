FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requierements.txt /app/

RUN pip install -r requierements.txt