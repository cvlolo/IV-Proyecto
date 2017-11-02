import telebot 
from telebot import types 
from telebot import util
import time 
import os


bot = telebot.TeleBot("457546213:AAF4iC8ZhhKQuTnLNrz1GGT1lh2SRtpxs64")

def listener(messages):
	for m in messages: 
        	if m.content_type == 'text': 
			cid = m.chat.id 
		    	print ("[" + str(cid) + "]: " + m.text) 

bot.set_update_listener(listener)

@bot.message_handler(commands=['clasificacion']) 
def clasificacion(m): 
	cid = m.chat.id 
	mensaje="Bienvenido al bot de la ATP"
	bot.send_message( cid, mensaje)


bot.set_update_listener(listener)

bot.polling(none_stop=True)
