import numpy as np


class Matrix:

    def __init__(self, row: int, column: int):
        self._row = row
        self._column = column
        self.matrix = None

        self.__init_matrix(row, column)

    def __init_matrix(self, row, column):
        self.matrix = np.zeros((row, column))

    def add_matrix(self, add_matrix):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = self.matrix[x][y] + add_matrix[x][y]

    def multiply_by_number(self, number):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = self.matrix[x][y] * number

    def print_matrix(self):
        print(self.matrix)

    # def multiply_matrix(self, multi_matrix):

    def __getitem__(self, item):
        return self.matrix[item]


if __name__ == '__main__':
    matrix_1 = Matrix(3, 3)
    matrix_2 = Matrix(3, 3)
    matrix_1.print_matrix()
    matrix_2.print_matrix()

    matrix_1.add_matrix(matrix_2)
    matrix_1.print_matrix()

    matrix_1.multiply_by_number(10)
    matrix_1.print_matrix()

    matrix_1.multiply_matrix(matrix_2)
    matrix_1.print_matrix()
