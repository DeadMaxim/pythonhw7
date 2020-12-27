my_matr = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


class Matrix:
    def __init__(self, list_1, list_2):
        self.my_matr = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                my_matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in my_matr]))


my_matrix = Matrix([[1, 3, 7],
                    [2, 6, 12],
                    [16, 22, 8]],
                   [[13, 25, 62],
                    [15, 66, 31],
                    [18, 51, 64]])

print(my_matrix)
