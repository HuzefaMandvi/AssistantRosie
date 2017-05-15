import json
import urllib.request
import datetime
import time
import pyttsx
import calendar
import feedparser

from weather import *
from voice import *

engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

quit = 0

city_id = input('Enter city ID: ')

#concat today's  date into a handy lil string
my_date = str(datetime.date.today().strftime("%A") + ', ' + datetime.date.today().strftime("%B") + ' ' + datetime.date.today().strftime("%d"))

#greet user
greet(engine)
#today's date
engine.say('Today is ')
engine.say(my_date)
engine.runAndWait()

while(quit == 0):
	command_key = input('Enter a command: ')
	
	if (command_key == 'weather'):
		current_weather(engine, city_id)
	elif (command_key == 'news'):
		headlines(engine)
	elif(command_key == 'joke'):
		tell_joke(engine)
	elif(command_key == 'quit'):
		quit = 1