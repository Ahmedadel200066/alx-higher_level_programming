#!/usr/bin/python3

def matrix_divided(matrix, div):
    if type(matrix) is not list[list[union[int, float]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TabError("div must be a number")
    if div == 0 :
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = list[map(div, matrix)]
        return new_matriX
        