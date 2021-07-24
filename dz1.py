""" Посмотреть документацию к API GitHub,
разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json. """

import requests
import json
username = input("Enter the github username:")
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
with open('dz1.json', 'w') as f:
    for i in range(0,len(json)):
        print("Project Number:",i+1, file=f)
        print("Project Name:",json[i]['name'], file=f)
        print("Project URL:",json[i]['svn_url'],"\n", file=f)

"""Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."""
import requests
import time
import json
def get_data(service, appid,city):
    while True:
        time.sleep(1)
        url = f'{service}?q={city}&appid={appid}'
        response = requests.get(url)
        if response.status_code == 200:
            print(url)
            break
    return response.json()

appid = 'b6907d289e10d714a6e88b30761fae22'
service = 'https://samples.openweathermap.org/data/2.5/weather'
city ='London, UK'
response = get_data(service, appid, city)

print('Done!')
print(response)

with open('1_2_weather.json', 'w') as f:
    json_repo = json.dump(response, f)

# НЕ УВЕРЕН, ЧТО СМОГ ПРАВИЛЬНО СДЕЛАТЬ 2 ЗАДАНИЕ