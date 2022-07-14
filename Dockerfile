FROM python:3.11.0b3-slim-buster

WORKDIR /app

COPY requierements.txt /app/

RUN pip install -r requierements.txt