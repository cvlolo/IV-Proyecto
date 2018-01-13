from fabric.api import *


def install():
	run('sudo git clone https://github.com/cvlolo/IV-Proyecto')
	run('pip install -r /home/ubuntu/IV-Proyecto/requirements.txt')

def web():
    run('cd ./Proyecto-IV && sudo chmod +x script.sh && sudo sh script.sh' )

def atpbot():
    run('sudo python home/ubuntu/IV-Proyecto/ATPBot/ATPbot.py')

def remove():
	run('sudo rm -rf ./IV-Proyecto')

