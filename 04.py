staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for element in staff:
    name = element.split(' ')[-1].capitalize()
    print(f'Привет, {name}!')
