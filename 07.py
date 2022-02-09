import re


class ComplexError(Exception):
    def __init__(self):
        self.message = None
        self.string = None

    def __str__(self):
        return f'Объект "{self.string}" типа {str(type(self.string)).split(" ")[1][:-1]} -> {self.message}'


class InvalidNumberFormat(ComplexError):
    def __init__(self, string, message='Неверный формат числа'):
        self.message = message
        self.string = string


class NotStrError(ComplexError):
    def __init__(self, string, message='Не является типом str'):
        self.message = message
        self.string = string


class NotComplexError(ComplexError):
    def __init__(self, string, message='Не является типом Complex'):
        self.message = message
        self.string = string


class Complex:
    def __init__(self, string):
        self.check_if_str(string)
        pattern = re.compile('^([-+]?)([0-9]*)([-+]?)([0-9]*)(i?)$')
        if not pattern.fullmatch(string):
            raise InvalidNumberFormat(string)
        parsed = pattern.findall(string)

        self.real_sign = parsed[0][0]
        self.real = parsed[0][1]
        self.image_sign = parsed[0][2]
        self.image = parsed[0][3]
        self.image_one = parsed[0][4]

    @staticmethod
    def check_if_str(obj):
        if type(obj) != str:
            raise NotStrError(obj)

    @staticmethod
    def check_if_complex(obj):
        if type(obj) != Complex:
            raise NotComplexError(obj)

    def __str__(self):
        return f'{self.real_sign}{self.real}{self.image_sign}{self.image}{self.image_one}'

    def __add__(self, other):
        self.check_if_complex(other)
        new_real = self.build_real() + other.build_real()
        new_image = self.build_image() + other.build_image()
        return Complex(self.build_string(new_real, new_image))

    def __mul__(self, other):
        self.check_if_complex(other)

        self_real = self.build_real()
        self_image = self.build_image()
        other_real = other.build_real()
        other_image = other.build_image()

        new_real = self_real * other_real - self_image * other_image
        new_image = self_real * other_image + self_image * other_real

        return Complex(self.build_string(new_real, new_image))

    def build_real(self):
        if self.real == '':
            return 0
        return int(self.real_sign + self.real)

    def build_image(self):
        if self.image == '':
            if self.image_one == '':
                return 0
            return int(f'{self.image_sign}1')
        return int(self.image_sign + self.image)

    @staticmethod
    def build_string(real, image):
        i = 'i'
        image_sign = '+'

        if real == 0:
            real = ''
            if image > 0 or image < 0:
                image_sign = ''
        else:
            if image < 0:
                image_sign = ''
            elif image == 0:
                image_sign = ''
                image = ''
                i = ''

        return f'{real}{image_sign}{str(image).replace("1", "")}{i}'


a = Complex('2-i')
v = Complex('1+3i')
w = Complex('i')
x = Complex('2+i')
y = Complex('-2')
z = Complex('-2+3i')

print(a + v)
print(v + w)
print(w + x)
print(x + y)
print(y + z)
print(x + a)

print('-' * 15)

print(a * v)
print(v * w)
print(w * x)
print(x * y)
print(y * z)
print(x * a)
