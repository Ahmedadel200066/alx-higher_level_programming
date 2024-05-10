#!/usr/bin/python3

"""
This module defines a Square class that represents a square shape.
"""
Rectangle = __import__("9-rectangle").Rectangle


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
        if size >= 0:
                self.integer_validator("size", size)
                self.__size = size
