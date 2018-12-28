import parserweatherAPI
import traceback
import requests


def test_temp():
    min_temp = -70
    max_temp = 70
    k = 273
    try:
        t1, t2 = parserweatherAPI.weather(55.755826, 37.6172999)
        t1 = t1 - k
        t2 = t2 - k
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


test_temp()





