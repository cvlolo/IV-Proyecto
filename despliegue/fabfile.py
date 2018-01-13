from fabric.api import *


def install():
	run('sudo git clone https://github.com/cvlolo/IV-Proyecto')
	run('pip install -r /home/ubuntu/IV-Proyecto/requirements.txt')

def web():
    run('cd ./IV-Proyecto && sudo chmod +x script.sh && sudo sh script.sh' )

def atpbot():
    run('sudo python home/ubuntu/IV-Proyecto/ATPBot/ATPbot.py')

def runALL():
	web()
	atpbot()

def remove():
	run('sudo rm -rf ./IV-Proyecto')

