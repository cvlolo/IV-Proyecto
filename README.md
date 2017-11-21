[![Build Status](https://travis-ci.org/cvlolo/IV-Proyecto.svg?branch=master)](https://travis-ci.org/cvlolo/IV-Proyecto)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cvlolo/IV-Proyecto)

# IV-Proyecto

Proyecto basado en python para la asignatura de IV

# ATPBot

## Explicación

Se realizará un BOT en Telegram programado en Python que nos proporcionará toda la información relevante del tenis profesional de la ATP 
mostrando información relevante de los diferentes Grand Slam con los resultados de los partidos así como mostrar el top 10 del ranking mundial actualizado al momento.
Se utilizará la técnica del Web Scraping en Python para extraer la información necesaria así como de una base de datos para almacenarla.

El BOT se encargará de satisfacer a todos los amantes del tenis profesional de una forma rápida y cómoda, agrupando la información relevante.

## Requisitos 

* API de Telegram
* Python para el desarrollo del BOT
* Herramienta de Web Scraping en Python (Posiblemente BeautifulSoup)
* Servidor de base de datos(aún por determinar)
* Despliegue en la nube


## TDD e Integración Continua 

Para el desarrollo del proyecto vamos a utilizar la práctica de ingeniería de software denominada TDD o desarrollo guiado por pruebas, en la cuál se crearán una serie de pruebas unitarias (unit test) para asegurarnos de que en todo momento nuestro código es limpio y funcional. Esto nos facilitará llevar a cabo la pŕatica de Integración Continua, en la que estaremos continuamente integrando nuestro código con el del resto del equipo del proyecto y nos permitirá corregir los errores que surjan durante el desarrollo de forma más rápida. 

## Despliegue en Heroku

Despliegue https://atpbot.herokuapp.com/

Para realizar el despliegue de la aplicación he utilizado [Heroku](https://dashboard.heroku.com/) como Paas ya que es gratuito y nos permite realizar el despliegue de forma sencilla, además de que nos proporciona una base de datos (PostgreSQL) de forma gratuita y a la que se accede fácilmente, por lo que puede integrarse con el proyecto de forma inmediata.

En primer lugar, instalamos Heroku CLI en nuestro ordenador utilizando el comando:

		wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

Para conectarnos desde la terminal utilizamos heroku login y ponemos los datos con los que nos hemos registrado. Creamos nuestra aplicación en la página de Heroku y la configuramos para que haga el deploy cada vez que hagamos git push y pase los tests de Travis: 

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/HEroku1.png)

Por otra parte he instalado como addon la base de datos de Postgres para usarla en mi aplicación:

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/Heroku2.png)

Hay que crear el archivo Procfile que contendrá las opciones de despliegue de Heroku:

		worker: cd ATPBot && python ATPbot.py 
		web: gunicorn web:app --log-file=-

Comprobamos que los dos servicios están funcionando:

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/Heroku3.png)

Por último, comprobamos que la aplicación está funcionando correctamente con los logs de Heroku:

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/heroku4.png)

La aplicación desplegada puede verse en Telegram bajo el alias @IV_ATP_bot y cuya funcionalidad actual es mostrar un mensaje de bienvenida y la clasificación actual de la atp, almacenada en
una base de datos. Si entramos en la página https://atpbot.herokuapp.com/ ésta nos devuelve un json con status ok.

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/heroku5.png)

## Despliegue en Docker

Lo primero que tenemos que hacer es registrarnos en la página de [Docker](https://www.docker.com/) e irnos al apartado de Create automated build

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/Docker.png)

Autorizamos a Docker a conectarse a nuestra cuenta de GitHub

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/Docker2.png)

Una vez ahí creamos nuestro repositorio de Docker rellenando los datos 

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/Docker3.png)

Ahora tenemos que crear un fichero Dockerfile que contenga los datos necesarios para que Docker pueda crear el contenedor, siendo mi Dockerfile el siguiente:

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
		WORKDIR IV-Proyecto/
		CMD ./script.sh

Hacemos push del fichero Dockerfile a nuestro repositorio y aumáticamente Docker empezará a hacer la build del contenedor:

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/Docker4.png)

Una vez acabado, se puede hacer pull del repositorio con docker pull cvlolox/iv-proyecto y ejecutarlo con sudo docker run -e "TOKEN=MI_TOKEN" -e "DATABASE_URL=MI_DATABASE" -i -t cvlolox/iv-proyecto

El resultado es el siguiente 

![img](https://github.com/cvlolo/IV-Proyecto/blob/master/img/Docker5.png)

Enlace del repositorio en Docker Hub: [https://hub.docker.com/r/cvlolox/iv-proyecto/](https://hub.docker.com/r/cvlolox/iv-proyecto/)

Una vez tenemos el contenedor, lo desplegamos en Zeit. Para ello tenemos que instalar now con npm install -g now , importante haber instalado previamente npm y node.js con apt-get. 
Ejecutamos now -e "TOKEN=MI_TOKEN" -e "DATABASE_URL=MI_DATABASE" en el directorio donde se encuentra el Dockerfile y autoámticamente se desplegará el contenedor y obtenedremos la url.

Contenedor [https://iv-proyecto-nhuhtlpcmv.now.sh/](https://iv-proyecto-nhuhtlpcmv.now.sh/)




