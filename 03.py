from functools import wraps


def type_logger(verb=0):

    def type_logger_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            """Декоратор для логирования типов аргументов"""
            result = func(*args, **kwargs)
            args_list = []
            kwargs_list = []

            if len(args) > 0:
                args_list = [', '.join([f'{k}: {v}' for k, v in {arg: type(arg) for arg in args}.items()])]
            if len(kwargs) > 0:
                kwargs_list = [', '.join([f'{k}={v}: {type(v)}' for k, v in kwargs.items()])]
            msg = ', '.join(args_list)

            if verb == 1:
                msg = ', '.join(args_list + kwargs_list)
            elif verb > 1:
                msg = f'{func.__name__}: {type(result)} ({", ".join(args_list + kwargs_list)})'
            print(msg)

            return result
        return wrapper
    return type_logger_decorator


@type_logger(verb=2)
def calc_degree(x, deg=1, is_true=True):
    """Вычисление степени deg числа x"""
    if is_true:
        return x ** deg
    return None


@type_logger()
def multiply(x, mult):
    """Увеличение числа x в mult раз"""
    return x * mult


a = calc_degree
b = multiply

print(a.__name__, a.__doc__, sep=' - ')
print(b.__name__, b.__doc__, sep=' - ')

a = calc_degree(5, deg=3, is_true=True)
b = multiply(2, 3)

print(a)
print(b)
