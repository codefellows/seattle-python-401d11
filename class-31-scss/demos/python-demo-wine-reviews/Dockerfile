FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

RUN apt-get update && \
    apt-get install -y gcc

COPY . /src

RUN pip install -r requirements.txt

