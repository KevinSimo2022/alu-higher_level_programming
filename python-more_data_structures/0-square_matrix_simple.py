#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_matrix_simple(matrix=[]):
    lenM = len(matrix)
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(lenM)]
    for i in range(len(matrix)):
        for l in range(len(matrix[i])):
            new_matrix[i][l] = matrix[i][l]*matrix[i][l]
    return new_matrix
