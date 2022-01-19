import sys
import fileinput

FILENAME = 'bakery.csv'

if len(sys.argv) <= 2:
    print('Недостаточно параметров')
    exit(1)
elif len(sys.argv) >= 3:
    try:
        position = int(sys.argv[1])
        new_value = float(sys.argv[2].replace(',', '.'))
        with fileinput.FileInput(FILENAME, inplace=True) as f:
            edited = False
            for index, line in enumerate(f, 1):
                if index == position:
                    old_value = line
                    print(line.replace(old_value, str(new_value) + '\n'), end='')
                    edited = True
                else:
                    print(line, end='')
        if not edited:
            print(f'Указанный номер записи ({position}) не найден')
            exit(1)

    except ValueError:
        print('Указано неверное значение')
        exit(1)
    except FileNotFoundError:
        print('Не найден файл bakery.csv')
        exit(1)
