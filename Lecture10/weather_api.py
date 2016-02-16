import requests
from datetime import datetime

city = input("Въведете град: ")

response = requests.get('http://api.openweathermap.org/data/2.5/weather', params={
    'q': city,
    'appid': '965acdac1ae64cf06761bb563ad34d96'})

try:
    info = response.json()
    update_date = datetime.fromtimestamp(int(info['dt'])).strftime('%Y-%m-%d %H:%M:%S')
    print(update_date)
    print("""
            Информация към: {}
            Температура: {}
            Налягане: {}
            Влажност: {}%
            Вятър: {} м/с
            """.format(update_date,
                       float(info['main']['temp']) - 273.15,
                       info['main']['pressure'],
                       info['main']['humidity'],
                       info['wind']['speed']))
except:
    print("Грешка!")



