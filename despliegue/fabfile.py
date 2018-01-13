from fabric.api import *


def install():
	run('sudo git clone https://github.com/cvlolo/IV-Proyecto')
	run('pip install -r /home/ubuntu/IV-Proyecto/requirements.txt')

def web():
    run('sudo gunicorn --config=config_gunicorn.py web:app -D' )

def atpbot():
    run('sudo python home/ubuntu/IV-Proyecto/ATPBot/ATPbot.py')

def remove():
	run('sudo rm -rf ./IV-Proyecto')

