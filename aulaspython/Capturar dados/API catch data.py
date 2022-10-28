import requests

from pprint import pprint

API_key= 'fb77393f2df9c7d3867f446935fda937'

city = input('Enter a city: ')

base_url = "http://api.openweathermap.org/data/2.5/weather?APPID="+API_key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)