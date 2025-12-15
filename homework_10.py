# Задача 1

import requests
from pprint import pprint

heroes_list_ids = [332, 149, 655]

for id in heroes_list_ids:
    url = f'https://superheroapi.com/api/2619421814940190/{id}/powerstats'
    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception("Ответ не 200")
    
    intelligence = resp.json()['intelligence']
    name = resp.json()['name']

    heroes_dict = dict()
    heroes_dict.setdefault(name, intelligence)

max_intelligence_hero = max(heroes_dict, key=heroes_dict.get)
max_intelligence = max(heroes_dict.values())

print(f'Супергерой с максимальным интеллектом: {max_intelligence_hero} {max_intelligence}')

# Задача 2

import requests
import os
from pprint import pprint

full_path  = input("Укажите полный путь к файлу для загрузки: ")
file_name = os.path.basename(full_path)

token = input("Введите ваш токен: ")
overwrite = input("Перезаписать существующий файл?: ")

with open(full_path, 'rb') as f:

    params = {'path': file_name, 'overwrite': overwrite}
    headers = {"Authorization": token}

    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    resp = requests.get(url, params=params, headers=headers)

    if resp.status_code != 200:
        raise Exception("Ответ не 200!")

    href = resp.json()['href']

    resp = requests.put(href, data=f.read())

    if resp.status_code != 201:
        raise Exception("Ответ не 201!")
            
    print('Файл загружен!')