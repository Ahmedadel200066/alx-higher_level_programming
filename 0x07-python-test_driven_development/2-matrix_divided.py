#!/usr/bin/python3

def matrix_divided(matrix, div):
    if type(matrix) is not list:
        for row in matrix:
            if type(row) in matrix is not list:
                for j in row :
                    if type(j) is not int and type(j) is not float:   
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TabError("div must be a number")
    if div == 0 :
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(j / div, 2) for j in i] for i in matrix]
