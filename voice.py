import datetime
import time
import pyttsx
import feedparser

from weather import *

#greet user based on current time
def greet(engine):
	hour = int(datetime.datetime.now().strftime('%H'))
	if (hour < 12):
		engine.say('Good morning, hoozayfa')
	elif (hour < 17):
		engine.say('Good afternoon, hoozayfa')
	else:
		engine.say('Good evening, hoozayfa')
	engine.runAndWait()

#punbearable.
# TODO: add more jokes, randomly choose one
def tell_joke(engine):
    engine.say('Why was the robot angry?')
    engine.say('Because someone kept pushing her buttons!')
    engine.runAndWait()

#get weather from weather module, read out to user
def current_weather(engine, city_id):
	#uses weather.py
	weather_data = data_organizer(data_fetch(url_builder(city_id)))
	
	engine.say('Current weather in {}:'.format(weather_data['city']))
	engine.say('It is {} degrees, with {}'.format(int(round(weather_data['temp'], 0)), weather_data['sky']))
	engine.runAndWait()

#read top 4 headlines from nbc boston rss feed
def headlines(engine):
	url1 = "http://www.nbcboston.com/news/top-stories/?rss=y&embedThumb=y&summary=y"
	engine.say('Top headlines for today from NBC Boston: ')
	for i in feedparser.parse(url1).entries[:4]:
		engine.say(i.title)
	engine.runAndWait()