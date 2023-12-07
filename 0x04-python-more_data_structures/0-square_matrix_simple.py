#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i, _i in matrix:
        for j, _j in i:
            new_matrix[_i][_j] = j**2

    return new_matrix
