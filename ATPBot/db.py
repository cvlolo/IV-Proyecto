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

def mostrar_jugadores():
	conn = psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
	cursor = conn.cursor()
	cursor.execute("select * from jugadores;")
	conn.commit()
	cursor.close()
	conn.close()
