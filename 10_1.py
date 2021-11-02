# Task_1

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f'{itm:03}' for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            mtx = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                   for line in range(len(self.data))]
            return Matrix(mtx)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[1, 0, 1], [0, 0, 1], [1, 0, 1]]
m_2 = [['0', '0', '1'], ['1', '1', '1'], ['1', '0', '1']]

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
new_matrix = matrix_1 + matrix_2

lines = int(input('Введите количество строк и столбцов матрицы: '))
columns = lines

matrix_11 = Matrix([[a * x for x in range(lines)] for a in range(columns)])
matrix_12 = Matrix([[a * x for x in range(lines)] for a in range(columns)])

print('First matrix:\n', matrix_11, end='\n\n')
print('Second matrix:\n', matrix_12, end='\n\n')
print('Sum of first and second matrix:\n', matrix_11 + matrix_12)
