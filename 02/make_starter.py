import os

CONFIG_NAME = 'config.yaml'

try:
    with open(CONFIG_NAME) as f:
        for line in f.readlines():
            line_is_dir = False
            full_path = os.path.join(os.curdir, line.strip())
            if len(line.rsplit('.')) > 1:
                dir_path = os.path.split(full_path)[0]
            else:
                dir_path = full_path
                line_is_dir = True

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            if not line_is_dir:
                with open(full_path, 'w'):
                    pass
except FileNotFoundError:
    print(f'Файл {CONFIG_NAME} не найден')
    exit(1)

