#!/usr/bin/python3

"""this module prints a square using # """


def print_square(size):
    """this function print a square shape using any letter or mark"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise ValueError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
