#!/usr/bin/python3
""" define a class Square """


class Square:
    """ define __init__ function """
    def __init__(self, size=0,position=(0, 0)):
        """ initializes size and position of self with size """
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """ returns __size of self """
        return self.__size
    def position(self):
        """ returns position of self """
        return self.__position
    
    @position.setter
    def position(self, value): 
        if type (value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            """ initialize """
            self.__position = value
            
    @size.setter
    def size(self, value):
        """ if statement """
        if type(value) is not int:
            """ raise error """
            raise TypeError("size must be an integer")
        elif value < 0:
            """ raise error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize """
            self.__size = value
    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
    """ defines my_print function """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            maxx = self.__size
            for i in range(maxx):
                for j in range(self.__size):
                    print("#", end="")
                print()
