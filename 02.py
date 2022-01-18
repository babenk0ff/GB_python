import requests
import os

URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
FILENAME = 'nginx_logs.txt'

if not os.path.isfile(FILENAME):
    with requests.get(URL, stream=True) as r:
        with open(FILENAME, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

with open(FILENAME, 'r', encoding='utf-8') as f:
    user_requests_amount = {}
    for line in f.readlines():
        remote_addr = line.split(' - - ')[0]

        if remote_addr not in user_requests_amount.keys():
            user_requests_amount[remote_addr] = 1
        else:
            user_requests_amount[remote_addr] += 1

inverse = [(value, key) for key, value in user_requests_amount.items()]
spammer = max(inverse)

print("Spammer's IP is {0} with {1} requests".format(spammer[1], spammer[0]))
