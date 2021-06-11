FROM python:3

WORKDIR /app

COPY requierements.txt /app/

RUN pip install -r requierements.txt