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

