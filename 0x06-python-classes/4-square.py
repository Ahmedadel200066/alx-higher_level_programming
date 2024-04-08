#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ getter """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ setter """
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    
    def area(self):
        """ this function returns the current square area """
        return self.__size ** 2
