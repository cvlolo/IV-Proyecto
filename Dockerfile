FROM ubuntu:16.04
MAINTAINER Manuel Casado Vergara

#Variables de entorno
ARG token_bot

ARG database

ENV TOKEN=$token_bot

ENV DATABASE_URL=$database

RUN apt-get update
RUN apt-get install -y python-setuptools
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade
RUN apt-get install net-tools

RUN apt-get install -y git
RUN git clone https://github.com/cvlolo/IV-Proyecto.git


RUN pip install -r IV-Proyecto/requirements.txt

EXPOSE 80
WORKDIR Proyecto_IV/
CMD ["gunicorn","--config=config_gunicorn.py","web:app"]



