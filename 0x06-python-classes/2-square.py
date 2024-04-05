#!/usr/bin/python3
""" Defines a class named Square """


class Square:
    """ defines a function called __init__ """
    def __init__(self, size = 0):
        if size < 0 :
            print("ValueError")
            
    """ initializes __size of self with size """
    self.__size = size
        