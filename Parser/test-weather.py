import parserweatherAPI
import sys, traceback
import requests

def test_tempcity():
    min_temp = -70
    max_temp = 70
    kZero=273
    try:
        t1, t2 = parserweatherAPI.weather('London')
        t1 = t1 - kZero
        t2 = t2 - kZero
        if t1 > min_temp and t1 < max_temp and t2 > min_temp and t2 < max_temp:
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


test_tempcity()



