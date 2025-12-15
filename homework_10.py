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