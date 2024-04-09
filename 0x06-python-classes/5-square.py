#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """

    def __init__(self, size=0):
        self.__size = size
        """ defines area function """
    """ getter """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        isinstance2 = isinstance(value, int)
        if isinstance2:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ this function returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ this function prints in stdout the square with the character # """
        if self._size == 0:
            print("/n")
        else:
            for x in range(self.__size)
            for y in range(self.__size)
            print("#", "")
            print()
