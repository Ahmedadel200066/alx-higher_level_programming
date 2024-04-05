#!/usr/bin/python3
""" Defines a class named Square """


class Square:
    """ defines a function called __init__ """
    def __init__(self, size=0):
        """if statement"""
        if type(size) != int:
            """if statment type checker"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """if size less than 0"""
            raise ValueError("size must be >=0")
        else:
            """ initializes __size of self with size """
            self.__size = size