import copy


class Matrix:
    def __init__(self, list_of_rows):
        self.__rows = list_of_rows

    def __str__(self):
        tmp_list = copy.deepcopy(self.__rows)
        for row in tmp_list:
            row.insert(0, '|')
            row.append('|')
        return '\n'.join([' '.join(map(str, row)) for row in tmp_list])

    def __add__(self, other):
        if list(map(len, self.__rows)) != list(map(len, other.__rows)):
            raise ValueError('Матрицы разных размеров')
        else:
            return Matrix(
                [list(map(sum, zip(*tmp))) for tmp in zip(self.__rows, other.__rows)]
            )


rows_1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
matrix_1 = Matrix(rows_1)
print(matrix_1)

rows_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = Matrix(rows_2)
print(matrix_2)

matrix_3 = matrix_1 + matrix_2
print(matrix_3)
