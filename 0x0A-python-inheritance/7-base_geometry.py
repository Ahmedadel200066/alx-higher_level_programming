#!/usr/bin/python3


class BaseGeometry():
    """ 
    BaseGeometry class represents the base class for geometrical shapes.

    Methods:
        - area(): Raises an exception indicating that the method is not implemented.
        - integer_validator(name, value): Validates if a given value is an integer and greater than 0.

    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int :
            raise TypeError("{} mast be an integer".format(name))
        elif value <= 0 :
            raise ValueError("{} must be greater than 0".format(name))
