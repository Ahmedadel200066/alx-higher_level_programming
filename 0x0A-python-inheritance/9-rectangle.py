#!/usr/bin/python3

"""This module defines the Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if type(width) is int :
            self.integer_validator("width", width)
            self.__width = width
        if type(height) is int :
            self.integer_validator("height", height)
            self.__height = height

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
