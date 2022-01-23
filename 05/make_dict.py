import os
import json
import sys
from pprint import pprint


folder_to_inspect = os.curdir

# Определение заданной папки в виде аргумента при запуске скрипта из консоли
if len(sys.argv) > 1:
    if not os.path.exists(sys.argv[1]):
        print('Папка не найдена')
        exit(1)
    else:
        folder_to_inspect = sys.argv[1]

cur_folder_name = os.path.split(os.getcwd())[-1]
result = {}

ext_100 = set()
ext_1000 = set()
ext_10000 = set()
ext_100000 = set()

n_100 = 0
n_1000 = 0
n_10000 = 0
n_100000 = 0

for root, dirs, files in os.walk(os.path.join(os.curdir, folder_to_inspect)):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        file_ext = os.path.splitext(file)[-1].strip('.')

        if file_size <= 100:
            n_100 += 1
            ext_100.add(file_ext)
            result[100] = (n_100, list(ext_100))
        elif 100 < file_size <= 1000:
            n_1000 += 1
            ext_1000.add(file_ext)
            result[1000] = (n_1000, list(ext_1000))
        elif 1000 < file_size <= 10000:
            n_10000 += 1
            ext_10000.add(file_ext)
            result[10000] = (n_10000, list(ext_10000))
        elif 10000 < file_size <= 100000:
            n_100000 += 1
            ext_100000.add(file_ext)
            result[100000] = (n_100000, list(ext_100000))

pprint(dict(result))

with open(f'{cur_folder_name}_summary.json', 'w') as f:
    json.dump(result, f)
