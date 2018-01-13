from fabric.api import *


def install():
	run('sudo git clone https://github.com/cvlolo/IV-Proyecto')
	run('pip install -r /home/ubuntu/IV-Proyecto/requirements.txt')

def web():
    run('sudo python home/ubuntu/IV-Proyecto/web.py' )

def atpbot():
    run('sudo python home/ubuntu/IV-Proyecto/ATPBot/ATbot.py')

def remove():
	run('sudo rm -rf ./IV-Proyecto')

