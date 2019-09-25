import telebot
token = "905673763:AAFotqo8dPqOrL_A-ceZoxpsKe_Pd6JnkhQ"
bot=telebot.TeleBot(token)
import requests
import pyowm
import time
from telebot import types 
from pyowm import timeutils

cur_ans = False
city = '' 

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message , 'Hello, Wassup! We are going to check the weather')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message , 'Write /city to choose location; after that write /tempe; you can also write /wind')	
	
@bot.message_handler(commands=['city'])
def write_city(message):
        global cur_ans
        bot.send_message(message.chat.id ,  " Write your city in English: ")
        cur_ans = True     
@bot.message_handler(commands=['tempe'])
def temp(message):
        global city
        owm = pyowm.OWM('96fb61a7fc9d793426449650896e6caf')
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        temperature =w.get_temperature('celsius')['temp']
        bot.send_message(message.chat.id ,  " Temperature in" + city + " is " + str(temperature) + " centigrade!")
        bot.send_message(message.chat.id , "Also in current city was considered " +w.get_detailed_status())

@bot.message_handler(commands=['wind'])
def wind(message):
        global city
        owm = pyowm.OWM('96fb61a7fc9d793426449650896e6caf')
        obs = owm.weather_at_place(city)
        w = obs.get_weather()
        wspeed = w.get_wind()['speed']
        bot.send_message(message.chat.id ,  " Wind speed in" + city + " is " + str(wspeed) + " meteres per second")

@bot.message_handler(content_types=['text'])
def get_answer(message: types.Message):
        global cur_ans, city
        if cur_ans == True:
                city = message.text
                cur_ans = False
                
       
while True:
    try:
        bot.polling()
    except Exception:
            time.sleep(15)
