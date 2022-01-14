import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)

FILENAME = 'nginx_logs.txt'

with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write(response.text)

with open(FILENAME, 'r', encoding='utf-8') as f:
    user_requests_amount = {}
    for line in f.readlines():
        ip = line.split(' - - ')[0]

        if ip not in user_requests_amount.keys():
            user_requests_amount[ip] = 1
        else:
            user_requests_amount[ip] += 1

inverse = [(value, key) for key, value in user_requests_amount.items()]
spammer = max(inverse)

print("Spammer's IP is {0} with {1} requests".format(spammer[1], spammer[0]))
