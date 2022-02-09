class IsNotIntError(Exception):
    def __init__(self, message='Введено не целое число'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


result = []

while True:
    try:
        user_input = input('Введите число для добавления в список: ')
        if user_input == 'stop':
            print('Список введенных чисел', result)
            break
        elif not user_input.isdigit():
            raise IsNotIntError
    except IsNotIntError as e:
        print(e)
        # continue
    else:
        result.append(int(user_input))
