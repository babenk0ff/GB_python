import re


class Date:
    def __init__(self, date_string):
        self.day, self.month, self.year = self.parse_date_string(date_string)
        pass

    @classmethod
    def parse_date_string(cls, date_string):
        pattern = r'^([0-9]{1,2})-([0-9]{1,2})-([0-9]{1,4})$'
        if not re.fullmatch(pattern, date_string):
            raise ValueError('Неверный формат даты')
        day, month, year = map(int, date_string.split('-'))

        if not cls.check_date(day, month, year):
            raise ValueError('Неверная дата')
        return day, month, year

    @staticmethod
    def check_date(day, month, year):
        if not (1 <= day <= 31
                and 1 <= month <= 12
                and 1 <= year <= 9999):
            return False
        return True


date_1 = Date('07-02-2022')
print(type(date_1.day), date_1.day)
print(type(date_1.month), date_1.month)
print(type(date_1.year), date_1.year)
