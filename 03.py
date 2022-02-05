class Cell:
    def __init__(self, cells: int):
        if type(cells) is not int:
            raise TypeError('Передано не целое число')
        self.__cells = cells

    def get_cells(self):
        return self.__cells

    @staticmethod
    def check_type(other):
        if type(other) != Cell:
            raise TypeError('Второй объект - не клетка')
        return True

    def __add__(self, other):
        if self.check_type(other):
            return Cell(self.__cells + other.__cells)

    def __sub__(self, other):
        if self.check_type(other):
            result = self.__cells - other.__cells
            if result <= 0:
                raise ValueError('Результат вычитания меньше нуля')
            else:
                return Cell(result)

    def __mul__(self, other):
        if self.check_type(other):
            return Cell(self.__cells * other.__cells)

    def __floordiv__(self, other):
        if self.check_type(other):
            result = self.__cells // other.__cells
            if result == 0:
                raise ValueError('Результат равен нулю')
            else:
                return Cell(result)

    def __truediv__(self, other):
        if self.check_type(other):
            return Cell(round(self.__cells / other.__cells))

    def make_order(self, count):
        result = []
        for i, val in enumerate(self.__cells * '*'):
            if i == count:
                result.append('\n')
                result.append(val)
                count += count
            else:
                result.append(val)
        print(''.join(result))


cell_1 = Cell(10)
cell_2 = Cell(4)

cell_3 = cell_1 + cell_2
print(cell_3.get_cells())

cell_3 = cell_1 - cell_2
print(cell_3.get_cells())

cell_3 = cell_1 * cell_2
print(cell_3.get_cells())

cell_3 = cell_1 / cell_2
print(cell_3.get_cells())

cell_1.make_order(4)
