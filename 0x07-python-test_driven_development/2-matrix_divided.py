#!/usr/bin/python3
"""this module is dealing with matrix"""


def matrix_divided(matrix, div):
    """this function that divides all elements of a matrix"""
    if type(matrix) is not list:
        for row in matrix:
            if type(row) in matrix is not list:
                for j in row:
                    if type(j) is not int and type(j) is not float:
                        raise TypeError(
                            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TabError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        matrixnew = [list(map(lambda a: round(a/div, 2), num))
                     for num in matrix]
        return matrixnew
