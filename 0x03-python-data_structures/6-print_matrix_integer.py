#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        print(" ".join("{}".format(elem) for elem in line))
