# Dockerfile

# PULL BASE IMAGE
FROM python:3.10.4

#Set Enviironment Variable

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /dockerize-dj

# Install dependencies
COPY  requirements.txt /dockerize-dj/
RUN pip install -r requirements.txt

# Copy project
COPY . /dockerize-dj/