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
	run('sudo apt-get install -y libpq-dev')
	run('sudo apt-get install -y gunicorn')
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
