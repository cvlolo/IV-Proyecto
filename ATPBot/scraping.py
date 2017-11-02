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
	if db.consultar_jugador(nombres[0]) != -1:
		for x in range(len(nombres)):
			db.insertar_jugador(nombres[x],str(pts[x]))

	
