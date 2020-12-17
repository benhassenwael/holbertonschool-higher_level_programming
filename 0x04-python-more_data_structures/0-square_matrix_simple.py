#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda row: [el**2 for el in row], matrix))
