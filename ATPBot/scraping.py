from bs4 import BeautifulSoup
import requests
import html5lib
import re
import db

req = requests.get('http://www.atpworldtour.com/en/rankings/singles')
soup = BeautifulSoup(req.text, "html5lib")

def scrapClasificacion():
	entradas = soup.find_all('td', {'class' : 'player-cell'}, 'a')
	puntos = soup.find_all('td', {'class' : 'points-cell'}, 'a')
	patron = re.compile('data-ga-label="(.*?)"')

	nombres= patron.findall(str(entradas))

	patron = re.compile('singles\">(.*?)<')
	pts = patron.findall(str(puntos))
	if db.consultar_jugador(str(nombres[0])) != -1:
		for x in range(len(nombres)):
			db.insertar_jugador(nombres[x],str(pts[x]))

def mostrarClasificacion():
	players=db.mostrar_jugadores()
	points=db.mostrar_puntos()
	string=""
	for i in range(len(players)/2,0,-1):
		string= "En la posicion " +str(i)+ " esta "+ players[i-1] + " con: " +points[i-1]+ " puntos" +"\n" + string
	return string
