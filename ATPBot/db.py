import telebot 
import time 
import datetime
import psycopg2
import os
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def insertar_jugador(nombre,puntos):
	conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	cursor = conn.cursor()
	cursor.execute("Insert into jugadores(nombre, puntos) values (%s, %s);", (nombre, puntos))
	conn.commit()
	cursor.close()
	conn.close()

def consultar_jugador(name):
	conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	cursor = conn.cursor()
	try:
		cursor.execute("select nombre from jugadores where nombre=%s);", [name])
	except psycopg2.Error as e:
		conn.commit()
		cursor.close()
		conn.close()
		return -1
	conn.commit()
	cursor.close()
	conn.close()


def mostrar_jugadores():
	lista = []
	conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	cursor = conn.cursor()
	cursor.execute("select * from jugadores;")
	for jugador in cursor:
		lista.append(jugador[0])
	cursor.close()
	conn.close()
	return lista

def mostrar_puntos():
	lista = []
	conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	cursor = conn.cursor()
	cursor.execute("select puntos from jugadores;")
	for punto in cursor:
		lista.append(punto[1])
	cursor.close()
	conn.close()
	return lista
