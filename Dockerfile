FROM python:3.6

MAINTAINER aurelien beliard (email@domain.com)

RUN apt update
COPY . /usr/flask_min

WORKDIR /usr/flask_min
RUN useradd -r -u 20979 -ms /bin/bash aurelien.beliard


RUN pip3 install -r requirements.txt


CMD gunicorn -w 3 -b :8008 app:app