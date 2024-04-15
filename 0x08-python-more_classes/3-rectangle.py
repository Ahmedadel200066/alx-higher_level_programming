#!/usr/bin/python3

""" empty class Rectangle that defines a rectangle """


class Rectangle:
    """ this is a rectangle class functions """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width*self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width*2 + self.__height*2

    def print(self):
        if self.__width == 0 or self.__height == 0:
            print()

    def __str__(self):
        shobak = []
        for g in range(self.__width):
            for b in range(self.__height):
                shobak.append("#")
            shobak.append("\n")
