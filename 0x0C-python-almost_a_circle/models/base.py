#!/usr/bin/python3
"""
module Base
"""


class Base:
    """
    The Base class serves as the base class for other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The ID of the instance. Defaults to None.
        """
        if id is None:
            Base.__nb_objects = + 1
            self.id = Base.__nb_objects
        else:
            self.id = id
