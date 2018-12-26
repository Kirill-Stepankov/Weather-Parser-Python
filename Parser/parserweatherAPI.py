import requests
import datetime
import sys, traceback

def weather(city):
      sett={
            'APPID': '5b0b407d31e708c9d526008c893bbd2b',
      }
      sett['q'] = city
      weatherfile = requests.get('http://api.openweathermap.org/data/2.5/weather', params=sett)
      k = weatherfile.json()
      if k == {'cod': '404', 'message': 'city not found'}:
            print('City not found')
      else:
            return k['main']['temp_min'], k['main']['temp_max']

try:
      city = input('Название вашего города(на английском): ')
      min,max=weather(city)
      datee = datetime.date.today()
      print('Погода в ' + city,
            'на',
            str(datee) + ' :',
            str(int(min) - 273) + '°',
            '~',
            str(int(max) - 273) + '°',
            )
except TypeError as e:
      print(str(e))
except requests.exceptions.RequestException as e:
      print("connection error " + str(e))
except Exception as e:
      print("error " + str(e) + traceback.format_exc() )

