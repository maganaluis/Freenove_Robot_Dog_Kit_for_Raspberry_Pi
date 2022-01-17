FROM ubuntu:21.04

WORKDIR /opt
COPY . /opt/app

RUN apt-get install -y libatlas-base-dev libjasper-dev