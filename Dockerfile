FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /Capstone

COPY requirements.txt /Capstone/

WORKDIR /Capstone

RUN pip install -r requirements.txt

COPY . /Capstone/