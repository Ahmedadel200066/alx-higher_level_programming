#!/usr/bin/python3


Rectangle = __import__("9-rectangle.py").Rectange


"""
This module defines a Square class that represents a square shape.
"""


class Square(Rectangle):
    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        if type(size) is int:
            if size >= 0:
                self.integer_validator("size", size)
                self.__size = size
