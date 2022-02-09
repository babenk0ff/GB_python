class MyCustomZeroDivisionError(Exception):
    def __init__(self, message='На ноль делить нельзя'):
        self.message = message

    def __str__(self):
        return self.message


def division_func(x, y):
    if y == 0:
        raise MyCustomZeroDivisionError
    return x / y


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise MyCustomZeroDivisionError
    print(division_func(a, b))
except MyCustomZeroDivisionError as e:
    print(e)
