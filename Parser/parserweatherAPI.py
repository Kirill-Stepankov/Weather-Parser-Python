import requests
import datetime
import traceback


#
# Parser accepts cities in Russian and English.
# To add the ability to enter a city in Russian, I had to add a geocoding API.
# The weather parser is based on the Openweather API.
#


def geocoor(city):
    param = {'address': city, 
            'key': 'AIzaSyCqRl7suPEuPPJC8-qyU9sYp4WI2xg6aq0',
            'language': 'en', 
             }

    t = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params = param)
    r = t.json()
       

    if 'error_message' in r:
        print('City not found')
    else:        
        return r['results'][0]['geometry']['location']['lat'], r['results'][0]['geometry']['location']['lng']

def weather(lat,lng):
    sett = {'APPID': '5b0b407d31e708c9d526008c893bbd2b',
            'lat': lat,
            'lon': lng,
            }
    weatherfile = requests.get('http://api.openweathermap.org/data/2.5/weather', params=sett)
    k = weatherfile.json()    
    if k == {'cod': '400', 'message': str(lat)+' is not a float'}:
        print('invalid coordinates')
    else:
        return k['main']['temp_min'], k['main']['temp_max']


try:
    city = input('Название вашего города: ')
    lat, lng = geocoor(city)
    min, max = weather(lat, lng)
    date = datetime.date.today()
    print('Погода в ' + city,
          'на',
          str(date) + ' :',
          str(int(min) - 273) + '°',
          '~',
          str(int(max) - 273) + '°',
          )
except TypeError as e:
    print(str(e))
except requests.exceptions.RequestException as e:
    print("connection error " + str(e))
except Exception as e:
    print("error " + str(e) + traceback.format_exc())

