#!/usr/bin/python3

"""
This module defines the Rectangle class, which represents a rectangle.
"""

rectangle_8 = __import__('8-rectangle.py').Rectangle


class Rectangle(rectangle_8):
    """
    Represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

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
