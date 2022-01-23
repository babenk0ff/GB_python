import os
import shutil

PROJECT_NAME = 'my_project'
PROJECT_PATH = os.path.join(os.curdir, PROJECT_NAME)

if not os.path.exists(PROJECT_PATH):
    print(f'Проект "{PROJECT_NAME}" не найден')
    exit(1)

templates_path = os.path.join(PROJECT_PATH, 'templates')

for root, dirs, files in os.walk('my_project'):
    for _dir in dirs:
        if _dir == 'templates':
            shutil.copytree(os.path.join(root, _dir), templates_path, dirs_exist_ok=True)
