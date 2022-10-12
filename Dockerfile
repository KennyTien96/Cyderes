#syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

# Project initialization:
RUN pip install -r requirements.txt

# Copy app to Docker image
COPY app.py /code/
COPY templates /code/templates
COPY whois_token.py /code/

CMD gunicorn app:app -w 2 --threads 2 -b 0.0.0.0:${PORT}