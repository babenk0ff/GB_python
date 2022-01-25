from functools import wraps
from math import sqrt


def val_checker(check_func):
    def decorator_val_checker(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(*args)
            if check_func(*args):
                result = func(*args, **kwargs)
                return result
            else:
                msg = f'Wrong value {args[0]}'
                raise ValueError(msg)

        return wrapper

    return decorator_val_checker


@val_checker(lambda x: x > 0)
def calc_sqrt(y):
    return round(sqrt(y))


a = calc_sqrt
print(a.__name__)

a = calc_sqrt(16)
print(a)

b = calc_sqrt(-3)
print(b)
