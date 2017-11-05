from bs4 import BeautifulSoup
import requests
import html5lib
import re 

ATP_datos = {"Nada": 1020 , "Federer" : 980, "Djokovik": 650}


def ObtenerPuntosJugador(jugador):
        return ATP_datos.get(jugador)

def insertarJugador(nombre,puntos):
	ATP_datos[nombre]=puntos

def borrarJugador(nombre):
	del ATP_datos[nombre]


def ATPClas():
	req = requests.get('http://www.atpworldtour.com/en/rankings/singles')

	soup = BeautifulSoup(req.text, "html5lib")

        entradas = soup.find_all('td', {'class' : 'player-cell'}, 'a')
	puntos = soup.find_all('td', {'class' : 'points-cell'}, 'a')
	patron = re.compile('data-ga-label="(.*?)"')

	nombres= patron.findall(str(entradas))

	patron = re.compile('singles\">(.*?)<')
	pts = patron.findall(str(puntos))
        string = ""
        for x in range(len(nombres)):
                 string="En la posicion " +str(x+1)+ " esta "+ nombres[x] + " con: " +pts[x]+ " puntos" +"\n" + string
        return string

