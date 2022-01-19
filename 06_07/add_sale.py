import sys

FILENAME = 'bakery.csv'

if len(sys.argv) == 1:  # Вызов скрипта без аргументов
    print('Не указано добавляемое значение')
    exit(1)
else:
    try:
        value = float(sys.argv[1].replace(',', '.'))
        with open(FILENAME, 'a', encoding='utf-8') as f:
            f.write(str(value) + '\n')

    except ValueError:
        print('Указано неверное значение')
        exit(1)
