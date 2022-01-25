import re

filename = 'nginx_logs.txt'

with open(filename, 'r', encoding='utf-8') as f_in, open('dump.txt', 'w', encoding='utf-8') as f_out:
    for line in f_in.readlines():
        pattern = re.compile(r'(^[a-f0-9:.]+)\s-\s-\s\[(.+)]\s"(\w+)\s([a-z0-9_/]+)\s[\w\d/."]+\s(\d+)\s(\d+)')
        f_out.write(str(*pattern.findall(line.strip())) + '\n')
