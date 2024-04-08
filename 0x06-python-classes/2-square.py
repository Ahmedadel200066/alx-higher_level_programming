#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        """ if statement """
        checker = isinstance(size, int)
        if checker:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
