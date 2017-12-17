from fabric.api import *


def install():
	run('sudo git clone https://github.com/cvlolo/IV-Proyecto')
	run('cd ./IV-Proyecto && sudo pip install -r requirements.txt')

def services():
    run('cd ./IV-Proyecto && sudo chmod +x script.sh', pty=False)
    run('cd ./IV-Proyecto && sudo sh script.sh', pty=False)

def delete():
	run('sudo rm -rf ./IV-Proyecto')

def kill_py():
	run('sudo pkill python')
