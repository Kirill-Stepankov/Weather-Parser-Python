import parserweatherAPI
import traceback
import requests


def test_temp():
    min_temp = -70
    max_temp = 70
    k = 273
    try:
        t1, t2 = parserweatherAPI.weather('London')
        t1 = t1 - k
        t2 = t2 - k
        if min_temp < t1 < max_temp and min_temp < t2 < max_temp:
            print('Pass')
        else:
            print('Fail - Temperature is abnormal ' + str(t1) + " " + str(t2))
    except TypeError as e:
        print('Fail - TypeError exception')
        print(str(e))
    except requests.exceptions.RequestException as e:
        print('Fail - RequestException exception')
        print("connection error " + str(e))
    except Exception as e:
        print('Fail - Exception ')
        print("error " + str(e) + traceback.format_exc())


test_temp()



