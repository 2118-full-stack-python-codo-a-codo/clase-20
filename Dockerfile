FROM python:3.10.5-slim-buster

WORKDIR /app

COPY requierements.txt /app/

RUN pip install -r requierements.txt