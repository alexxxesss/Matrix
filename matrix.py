class Matrix:

    def __init__(self, matrix: list):
        self._row = len(matrix)
        self._column = len(matrix[0])
        self.__matrix = matrix

    def add_matrix(self, add_matrix):
        if self.__check_equality_matrix(self.__matrix, add_matrix):
            for x in range(len(self.__matrix)):
                for y in range(len(self.__matrix[x])):
                    self.__matrix[x][y] = self.__matrix[x][y] + add_matrix[x][y]

    def multiply_by_number(self, number):
        for x in range(len(self.__matrix)):
            for y in range(len(self.__matrix[x])):
                self.__matrix[x][y] = self.__matrix[x][y] * number

    def print_matrix(self):
        print(self.__matrix)

    def multiply_matrix(self, multi_matrix):
        if self.__check_agreed_matrix(self.__matrix, multi_matrix):
            m = len(self.__matrix)
            n = len(multi_matrix)
            k = len(multi_matrix[0])

            new_matrix = [[None for _ in range(m)] for _ in range(k)]

            for i in range(m):
                for j in range(k):
                    new_matrix[i][j] = sum(self.__matrix[i][kk] * multi_matrix[kk][j] for kk in range(n))
            self.__matrix = new_matrix
            return self.__matrix

    @staticmethod
    def __check_equality_matrix(matrix1, matrix2):
        if len(matrix1) == len(matrix2):
            if len(matrix1[0]) == len(matrix2[0]):
                return True
        raise ValueError("Матрицы разного размера. Операция сложения и вычитания не может быть выполнена.")

    @staticmethod
    def __check_agreed_matrix(matrix1, matrix2):
        if len(matrix1[0]) == len(matrix2):
            return True
        raise ValueError("Матрицы не являются согласованными, попробуйте заново")

    def __len__(self):
        return len(self.__matrix)

    def __getitem__(self, item):
        return self.__matrix[item]


if __name__ == '__main__':

    list_of_lists_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list_of_lists_2 = [[11, 22, 33], [44, 55, 66]]
    list_of_lists_3 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    matrix_1 = Matrix(list_of_lists_1)
    matrix_2 = Matrix(list_of_lists_2)
    matrix_3 = Matrix(list_of_lists_3)

    matrix_1.print_matrix()
    matrix_2.print_matrix()
    matrix_3.print_matrix()

    print("--------")

    matrix_1.add_matrix(matrix_3)
    matrix_1.print_matrix()

    print("--------")

    matrix_2.multiply_by_number(10)
    matrix_2.print_matrix()

    print("--------")

    matrix_1.multiply_matrix(matrix_3)
    matrix_1.print_matrix()
