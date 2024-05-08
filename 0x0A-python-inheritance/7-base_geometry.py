#!/usr/bin/python3


"""This module defines the BaseGeometry class."""

class BaseGeometry():
    """ 
    BaseGeometry class 
    represents the base class for geometrical shapes.

    Methods:
        - area(): Raises an exception indicating 
                  that the method is not implemented.
        - integer_validator(name, value): 
        Validates if a given value is an integer and greater than 0

    """

    def area(self):
        """
        This method raises an exception to indicate that the 
        area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a given value is an integer and greater than 0

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
