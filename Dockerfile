FROM python:3.5
MAINTAINER jcgh582@gmail.com

RUN pip install nose
RUN pip install python-dateutil

COPY . /root/src/
RUN pip install -e /root/src/

WORKDIR /root/src/
