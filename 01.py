import requests
from pprint import pprint

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)

FILENAME = 'nginx_logs.txt'

with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write(response.text)

with open(FILENAME, 'r', encoding='utf-8') as f:
    result = []
    for line in f.readlines():
        ip, tmp = line.split(' - - ')
        tmp_2 = tmp.split('"')[1]
        request, path = tmp_2.split(' ')[0], tmp_2.split(' ')[1]
        result.append((ip, request, path))

pprint(result)
