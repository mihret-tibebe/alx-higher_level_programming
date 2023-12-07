#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j]= matrix[i][j]**2

    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
