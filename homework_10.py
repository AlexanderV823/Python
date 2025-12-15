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

# Эталон

import requests
def get_smart_superhero(names):
    top_intelligence = -1
    top_name = ''
    for name in names:
        r = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{name}')
        data = r.json()
        intelligence = int(data['results'][0]['powerstats']['intelligence'])
        print(name, intelligence)
        if intelligence > top_intelligence:
            top_intelligence = intelligence
            top_name = name

    print(f'{top_name} - самый умный, его интеллект равен {top_intelligence}.')


get_smart_superhero(['Hulk', 'Captain America', 'Thanos'])

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

    # Эталон

    import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        my_headers = {'Authorization': self.token}
        fname = os.path.split(file_path)[1]
        my_params = {'path': '/' + fname, 'overwrite': 'true'}
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        r = requests.get(url, headers=my_headers, params=my_params)

        if r.status_code != requests.codes.ok:
            return f'При получении ссылки для загрузки произошла ошибка (код: {r.status_code})'

        href = r.json()['href']
        with open(file_path, 'rb') as fh:
            r = requests.put(href, data=fh.read())

        if r.status_code not in (requests.codes.created, requests.codes.accepted):
            return f'При загрузке файла произошла ошибка (код: {r.status_code})'
        return f'Файл {fname} успешно загружен на Яндекс.Диск'


if __name__ == '__main__':
    my_file_path = 'result.txt'
    auth_token = ''
    uploader = YaUploader(auth_token)
    result = uploader.upload(my_file_path)
    print(result)