# This Dockerfile was developed for the Technical Challenge to BeenVerified

FROM ubuntu:latest

MAINTAINER Jason David Espinoza Siles v1.0

RUN apt-get clean
RUN apt-get update

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

WORKDIR /home/api
RUN mkdir /db


ADD api/songsearchapi.py /home/api
ADD api/__init__.py /home/api
ADD api/db /home/api/
ADD api/db /home/api/db

RUN mv bvde.db /db

RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install flask flask-jsonpify flask-sqlalchemy flask-restful

EXPOSE 5000

CMD python songsearchapi.py