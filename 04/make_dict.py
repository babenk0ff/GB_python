import os
import sys
from collections import defaultdict
from pprint import pprint


folder_to_inspect = os.curdir

# Определение заданной папки в виде аргумента при запуске скрипта из консоли
if len(sys.argv) > 1:
    if not os.path.exists(sys.argv[1]):
        print('Папка не найдена')
        exit(1)
    else:
        folder_to_inspect = sys.argv[1]

result = defaultdict(int)

for root, dirs, files in os.walk(os.path.join(os.curdir, folder_to_inspect)):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size

        if file_size <= 100:
            result[100] += 1
        elif 100 < file_size <= 1000:
            result[1000] += 1
        elif 1000 < file_size <= 10000:
            result[10000] += 1
        elif 10000 < file_size <= 100000:
            result[100000] += 1

pprint(dict(result), width=1)
