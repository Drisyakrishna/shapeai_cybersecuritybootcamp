# -*- coding: utf-8 -*-
"""Weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SCR7iMcz2b5oHrNmNQ_DkbhMzIlk1V9I
"""

import requests
from datetime import datetime
api_key ='b1b57d9af514a3484d3d527977c9b417'
location = input("enter the  city name")
complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link =requests.get(complete_api_link)
api_data= api_link.json()
temp_city=((api_data['main']['temp'])-273.15)
weather_desc =api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd =api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y | %I:%M:%S%P")
print("........................")
print("weather states for - {} || {}".format(location.upper(), date_time))
print("...................................")
print("current temperature is :{:2f} deg C".format(temp_city))
print("current weather desc :",weather_desc)
print("current humidity :",hmdt, '%')
print("current wind speed:" ,wind_spd,'kmph')

