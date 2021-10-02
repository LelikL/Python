from itertools import islice, zip_longest


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join([' '.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])


m1 = [[1, 2], [3, 4]]
m2 = [[0, 1], [0, 2]]

matrix_1 = Matrix(m1)
matrix_2 = Matrix(m2)
print(f'Матрица 1\n{matrix_1}')
print(f'Матрица 2\n{matrix_2}')
print(f'Сумма матриц\n{matrix_2 + matrix_1}')