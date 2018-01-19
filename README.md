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

Enlace del repositorio en Docker Hub: https://hub.docker.com/r/cvlolox/iv-proyecto/

Una vez tenemos el contenedor, lo desplegamos en Zeit. Para ello tenemos que instalar now con npm install -g now , importante haber instalado previamente npm y node.js con apt-get. 
Ejecutamos now -e "TOKEN=MI_TOKEN" -e "DATABASE_URL=MI_DATABASE" en el directorio donde se encuentra el Dockerfile y autoámticamente se desplegará el contenedor y obtenedremos la url.

Contenedor https://iv-proyecto-nhuhtlpcmv.now.sh/

## Despliegue en AWS

Lo primero que tenemos que hacer una vez nos hemos decidido por realizar el despliegue utilizando AWS nos registramos en su [página](https://aws.amazon.com/es/). Seleccionamos el tipo de cuenta gratuita y rellenamos con nuestros datos. Cabe destacar que necesitaremos una tarjeta de cŕedito válida para registrarnos aunque la cuenta sea de tipo gratuito. Hay que tener cuidado con el uso que hacemos de las máquinas pues hay un límite de horas de uso totales de 750, 30 GB y 20000 peticiones al mes, a partir de cual empezarán a hacer cargos en la tarjeta. En el apartado [Billing](https://console.aws.amazon.com/billing/) podemos ver el uso hasta ahora de las máquinas y una previsión del uso total al final de mes. 

Una vez tenemos la cuenta creada, empezamos a trabajar en el despliegue. En primer lugar, es recomendable instalar la cli de AWS. Para ello basta con hacer *pip install awscli --upgrade --user*. La documentación de dicha herramienta podemos verla [aquí](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html). 

También deberemos instalar VirtualBox y Vagrant, simplemente ejecutando *sudo apt-get install virtualbox* , *sudo apt-get install vagrant* y el plugin de aws para vagrant *vagrant plugin install vagrant-aws* . Una vez instalados, nos vamos a la raiz del proyecto a desplegar y ejecutamos *vagrant init* para que se genere el fichero Vagrantfile a modificar. 

Antes de seguir con vagrant, vamos a crear la instancia de la máquina (y la máquina) en AWS con todo lo necesario. Lo primero que tenemos que hacer, es elegir la región en la que vamos a trabajar. Recomiendo elegir las de US ya que algunas de las otras no funcionan correctamente.En mi caso, trabajo sobre US WEST 2 (Oregon). Ahora pasamos a crear la instancia eligiendo el apartado de EC2 y Launch Instance, se puede ir directamente desde este [enlace](https://us-west-2.console.aws.amazon.com/ec2/v2/) (revisar si se está en la región correcta). 

Lo primero que tenemos que elegir es la imagen de la máquina. Yo voy a utilizar la que tiene Ubuntu-Server 16.04 pero tenemos multitud de imágenes diferentes donde elegir, incluso algunas personalizadas por Amazon con diferentes herramientas ya instaladas. Es importante destacar que la mayoría de las máquinas son accesibles a los usuarios con cuenta gratuita, las únicas sin acceso son algunas más avanzadas de Windows Server. El siguiente paso es elegir las propiedas de las instancias, eligiendo aquí t2.micro (varían en memoria RAM, CPU y tal). La siguiente página nos deja personalizar varias cosas de la instancia pero nada que haya usado yo en mi despliegue. Después elegimos cuantos GB de memoria vamos a necesitar, a gusto de cada uno(sin olvidar el límite de los 30 GB). Por último, creamos el grupo de seguridad donde permitiremos el tráfico en los puertos 22 (SSH) y 80 (servicio web), esenciales para este despliegue. Por último, AWS nos creará una clave en formato pem para acceder por SSH a esa instancia. Importante no perderla y tenerla en un lugar seguro. 

Por último, queda crear un usuario con permisos para poder realizar el despliegue. Podemos ir al [IAM](https://console.aws.amazon.com/iam), crear nuestro usuario y darle los permisos necesarios.

Una vez configurada la máquina en aws, toca personalizar el Vagrantfile. Mi fichero puede encontrarse en el siguiente [enlace](https://github.com/cvlolo/IV-Proyecto/blob/master/Vagrantfile). Vamos a explicarlo un poco las cosas más destacables:


     aws.access_key_id = ENV['ACCES_KEY']
     aws.secret_access_key = ENV['SECRET_ACCES_KEY']
     aws.session_token = ENV['TOKEN']

Estas líneas representan nuestras credenciales de acceso. Para obtenerlas, basta con usar la cli y ejecutar *aws sts get-session-token* y obtendremos la información en formato Json. Se puede apreciar como esta información se introduce despúes mediante variables de entorno. 

    aws.keypair_name = "Secure"
    aws.region= "us-west-2"
    aws.security_groups ='Secure'
    aws.instance_type= 't2.micro'
    aws.ami = "ami-1ee65166"
    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "Secure.pem"
    
Estas líneas se explican por sí mismas. El usuario ssh depende de la imagen de la máquina. El ami lo encontramos en la informacion de la instancia y también al seleccionar la imagen de la máquina. Básicamente, se encarga de identificar la imagen.

    config.vm.provision :puppet do |puppet|
	puppet.manifests_path= 'puppet/manifests/'
	puppet.manifest_file = 'recursos.pp'
	puppet.options = [
	'--verbose',
	'--debug',
    	]
     end
     
Este bloque se utiliza para el aprovisionamiento de la máquina utilizando puppet, se explicará en el siguiente apartado.


## Aprovisionamiento con Puppet

Puppet pede resultar un tanto complejo y extraño al principio, por lo que aconsejo mirar en primer lugar la documentación de [Vagrant](https://www.vagrantup.com/docs/provisioning/puppet_apply.html) al respecto y este  [tutorial básico](https://www.vagrantup.com/docs/provisioning/puppet_apply.html) para empezar a trabajar con Puppet. Puppet utiliza una estructura maestro/esclavo para trabajar lo que aumenta su complejidad, teniendo un servidor de maestro y varios nodos como esclavos. Sin embargo, voy a utilizar puppet apply que es una versión "masterless", es decir, no tenemos maestro si no una serie de esclavos (uno en este caso).  Lo primero que tenemos que hacer es crear la estructura de carpetas. En la raíz del proyecto creamos la carpeta puppet, dentro de ella la carpeta manifests y, por último, un fichero .pp donde estarán nuestras instraucciones. 

Es importante aclarar que Puppet no lee estos archivos de forma secuencial, por lo que habrá que señalar las dependencias manualmente si es que existen. Puppet también nos proporciona muchas herramientas para crear nuestros aprovisionamientos utilizando su sintaxis, podemos utilizar clases como cualquier otro lenguaje, crear diversos modulos e incluso importar modulos ya creados por otras personas. En mi caso, para generar la infraestructura necesaria para el despliegue, me basta con el siguiente [archivo](https://github.com/cvlolo/IV-Proyecto/blob/master/puppet/manifests/recursos.pp). Primero se hará el update y que esto se haya realizado satisfactoriamente es condición para las dos siguientes instalaciones, como forma de controlar un poco el orden de ejecución. Puppet elegirá cual de los dos siguientes instalar, puesto que como hemos dicho, no se hace de forma secuencial. En caso de que se necesiten crear manifests más complejos, podemos echar un vistazo al siguiente [artículo](https://www.digitalocean.com/community/tutorials/configuration-management-101-writing-puppet-manifests). 

Volviendo al bloque anterior en el Vagrantfile:

    config.vm.provision :puppet do |puppet|
	puppet.manifests_path= 'puppet/manifests/'
	puppet.manifest_file = 'recursos.pp'
	puppet.options = [
	'--verbose',
	'--debug',
    	]
     end
     
Debemos poner la ruta donde se encuentra la carpeta de manifests así como el archivo .pp. Las opciones utilizadas nos permiten depurar el aprovisionamiento. Una cosa muy importante a tener en cuenta y que no se comenta en muchos tutoriales y guías sobre Puppet y Vagrant, **es que necesitamos instalar Puppet en la máquina si queremos que se aprovisione con él**. No basta solo con poner en el Vagrantfile que vamos a usarlo. Para hacer esto de la forma más automática posible (teniendo en cuenta la documentación de Puppet donde explica su [instalación](https://puppet.com/docs/puppet/5.3/puppet_platform.html#apt-based-systems) ) podemos utilizar el shell provisioning en el Vagrantfile, utilizando algo como esto:

    $script = <<SCRIPT
    wget https://apt.puppetlabs.com/puppet5-release-xenial.deb
    sudo dpkg -i puppet5-release-xenial.deb
    sudo apt update
    SCRIPT
    
    Vagrant.configure("2") do |config|
      config.vm.provision "shell", inline: $script
    end

Como experiencia personal, si Vagrant no encuentra la ruta al bin de Puppet, incluir la línea:

	puppet.binary_path= 'usr/bin/puppet'
	
Recomiendo quitar la línea una vez estemos seguros de que tiene el PATH correctamente, porque puede interferir a la hora de indicar la ruta a los manifests. Es un poco molesta de hacer que empiece a funcionar, pero una vez lo hace, no da más problemas.

Ahora sí, estamos listos para ejecutar *vagrant up --provider=aws* recordando introducir las variables de entorno. No está de más recordar las opciones de reload, provision, halt y destroy que proporciona Vagrant así como de la opción --debug que pueden ahorrarnos muchos quebraderos de cabeza.

## Despliegue final con Fabric

Para finalizar el despliegue, creamos el archivo fabfile.py que se escribirá en python y definiremos las tareas necesarias para que nuestra aplicación se despliegue correctamente. Como siempre, podemos echar un ojo a su [documentación](http://docs.fabfile.org/en/1.14/usage/fabfiles.html). El archivo lo encontramos en el siguiente [enlace](https://github.com/cvlolo/IV-Proyecto/blob/master/despliegue/fabfile.py) y contiene lo siguiente:

    # coding: utf-8
    
    from __future__ import with_statement
    from fabric.api import *
    from fabric.contrib.console import confirm
    
    def Install():
    	with settings(warn_only=True):
    		if run("test -d ~/IV-Proyecto").failed:
    				run("git clone https://github.com/cvlolo/IV-Proyecto.git")
    
    	run("sudo apt-get update")
    	run('sudo apt-get install -y python')
    	run('sudo apt-get install -y python-pip')
    	run('sudo apt-get install -y gunicorn')
    	run('sudo apt-get install -y libpq-dev')
    	run('pip install -r ~/IV-Proyecto/requirements.txt')
    
    def Uninstall():
    	with settings(warn_only=False):
    		if run("test -d ~/IV-Proyecto").succeeded:	
    			run('sudo rm -rfv ./IV-Proyecto')
    
    def TestDjango():
        with settings(warn_only=True):
            result = local('cd ~/IV-Proyecto/servicioWeb && ./manage.py test atpbot', capture=True)
        if result.failed and not confirm("Parece que algo anda mal con la aplicacion.¿Seguro que desea realizar el despliegue?"):
            abort("Abortando despliegue")
    
    def DjangoUp():
    	TestDjango()
    	run('cd ~/IV-Proyecto/servicioWeb/ && sudo gunicorn servicioWeb.wsgi -b 0.0.0.0:80')
    
    def botUp():
    	run('cd ~/IV-Proyecto/ATPBot/ && python ATPbot.py')
    
    def RunDosRun():
    	botUp()
    	DjangoUp()
    
    def killGunicorn():
    	run('ps ax|grep gunicorn')
        run('sudo pkill gunicorn')
        
La sintaxis es la típica de python y cada tarea se coloca como una función. En la función Install, primero se hace un test por si existe el directorio para no volverlo a clonar. Lo que indicamos con *with settings(warn_only=True)* es que los errores encontrados solo se tomarán como warning y no harán abortar la ejecución. Su uso aquí es obligatorio puesto que si la orden test devuelve fallo, no seguimos ejecutando y no es lo que se busca. Mucho cuidado utilizando esto libremente puesto que podemos hacer que no se tengan en cuenta muchos fallos. El bloque de la instalación de bibliotecas se saca fuera de esa opción, para que podamos ver si algo ha fallado e interrumpir la ejecución.

En la función Uninstall hacemos lo mismo para solo eliminar el directorio si existe, utilizamos rm con -r para borrar todo de forma recursiva, -f para forzar el borrado y -v para poder visualizar todo lo que se ha borrado. 

La función TestDjango nos permite ejecutar los test que hemos creado en Django para saber de antemano si hay algún problema con él. Una funcionalidad bastante curiosa y útil de Fabric.

Las siguientes funciones nos permiten levantar los diferentes servicios tanto juntos como por separado y, finalmente, una función para matar el proceso de gunicorn si hiciera falta. No es la forma más ortodoxa de realizar esta tarea, pero es bastante funcional. 

El uso de estas funciones podemos verlas aprovechando el script de despliegue encontrado [aquí](https://github.com/cvlolo/IV-Proyecto/blob/master/provision/ScriptAutomatizacion.sh). Aquí simplemente se indican los pasos para realizar el despliegue de una vez, y encontramos las funciones auxiliares comentadas.

Despliegue final: 54.186.108.111

    











