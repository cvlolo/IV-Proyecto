import telebot 
from telebot import types 
from telebot import util
import time 
import os
import db
import scraping

TOKEN = os.environ['TOKEN'] 
bot = telebot.TeleBot(TOKEN)

def listener(messages):
	for m in messages: 
        	if m.content_type == 'text': 
			cid = m.chat.id 
		    	print ("[" + str(cid) + "]: " + m.text) 

bot.set_update_listener(listener)

@bot.message_handler(commands=['clasificacion']) 
def clasificacion(m): 
	cid = m.chat.id 
	scraping.scrapClasificacion()
	mensaje=scraping.mostrarClasificacion()
	bot.send_message( cid, mensaje)
	


bot.set_update_listener(listener)

bot.polling(none_stop=True)
