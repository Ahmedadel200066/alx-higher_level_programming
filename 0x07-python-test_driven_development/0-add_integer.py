#!/usr/bin/python3

"""this is awesome"""
def add_integer(a, b=98):
    """this function like this sympol +"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    x = int(a)
    y = int(b)
    return x + y
