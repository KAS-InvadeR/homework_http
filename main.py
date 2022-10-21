import requests
import os
from datetime import datetime, timedelta
import time

from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def upload(self, path_to_file: str):
        file_name = os.path.basename(path_to_file)
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        parametrs = {'path': path_to_file, 'overwrite': 'true'}
        headers = {'Authorization': f'OAuth {self.token}'}
        request_url = requests.get(url, params=parametrs, headers=headers).json()
        response = requests.put(request_url['href'], data=open(file_name, 'rb'))
        if response.status_code == 201:
            print('Success')
        else:
            print('Error')

# ----------------------------------------------
def superhero_intelligence(superheros_list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    superheros = requests.get(url)
    superheros_dict = {}
    for superhero in superheros.json():
        if superhero['name'] in superheros_list:
            superheros_dict[superhero['name']] = superhero['powerstats']['intelligence']
    return max(superheros_dict, key=superheros_dict.get)


def superhero_intelligence_2(superheros_list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    superheros = requests.get(url)
    our_heroes = filter(lambda hero: hero['name'] in superheros_list, superheros.json())
    heroes_res = {hero['name']: hero['powerstats']['intelligence'] for hero in our_heroes}
    return max(heroes_res, key=heroes_res.get)

# ----------------------------------------------
def search_sf(tag):
    questions_list = []
    minus = datetime.now() - timedelta(days=2)
    unixtime_now = int(time.mktime(datetime.now().timetuple()))
    unixtime_ = int(time.mktime(minus.timetuple()))
    url = 'https://api.stackexchange.com/2.3/questions'
    parametrs = {
        'fromdate': unixtime_,
        'todate': unixtime_now,
        'order': 'desc',
        'tagged': tag,
        'site': 'stackoverflow'
    }

    questions = requests.get(url, params=parametrs)
    for question in questions.json()['items']:
        questions_list.append([question['title'], question['link']])
    pprint(questions_list)


if __name__ == '__main__':
# Задача 1
    superheros_list = ['Hulk', 'Captain America', 'Thanos']
# Первый вариант
    # print(f'Cамый умный супергерой: {superhero_intelligence(superheros_list)}')
# Второй вариант
    # print(f'Cамый умный супергерой: {superhero_intelligence_2(superheros_list)}')

# Задача 2
    token = ''
    path_to_file = '/test.txt'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# Задача 3
    search_sf('python')

