#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry():
    """represents the base class for geometrical shapes."""

    def area(self):
        """
        This method raises an exception to indicate that the 
        area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """given value is an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
