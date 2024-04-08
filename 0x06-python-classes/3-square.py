#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        """ if statement """
        isinstance2 = isinstance(size, int)
        if isinstance2:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        
    def area(self):
        """ this function returns the current square area"""
        return self.__size ** 2

