import requests
import os
from pprint import pprint

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
FILENAME = 'nginx_logs.txt'

if not os.path.isfile(FILENAME):
    with requests.get(URL, stream=True) as r:
        with open(FILENAME, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

with open(FILENAME, 'r', encoding='utf-8') as f:
    result = []
    for line in f.readlines():
        remote_addr, tmp = line.split(' - - ')
        tmp_2 = tmp.split('"')[1]
        request_type, requested_resource = tmp_2.split(' ')[0], tmp_2.split(' ')[1]
        result.append((remote_addr, request_type, requested_resource))

pprint(result)
