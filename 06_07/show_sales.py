import sys

FILENAME = 'bakery.csv'

if len(sys.argv) == 1:  # Вызов скрипта без аргументов
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                print(line.strip().replace('.', ','))
            exit(0)
    except FileNotFoundError:
        print('Не найден файл bakery.csv')
        exit(1)

elif len(sys.argv) == 2:  # Вызов скрипта с одним аргументом
    try:
        start_position = int(sys.argv[1])
        with open(FILENAME, 'r', encoding='utf-8') as f:
            for index, line in enumerate(f, 1):
                if index >= start_position:
                    print(line.strip().replace('.', ','))
        exit(0)
    except ValueError:
        print('Введено неверное значение')
        exit(1)
    except FileNotFoundError:
        print('Не найден файл bakery.csv')
        exit(1)

else:  # Вызов скрипта с двумя и более аргументами
    try:
        start_position = int(sys.argv[1])
        end_position = int(sys.argv[2])
        with open(FILENAME, 'r', encoding='utf-8') as f:
            for index, line in enumerate(f, 1):
                if start_position <= index <= end_position:
                    print(line.strip().replace('.', ','))
    except ValueError:
        print('Введено неверное значение')
        exit(1)
    except FileNotFoundError:
        print('Не найден файл bakery.csv')
        exit(1)
