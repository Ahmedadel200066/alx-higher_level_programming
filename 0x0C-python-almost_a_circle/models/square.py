#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: Variable length argument list
            containing the new values for the attributes.
            **kwargs: Keyword arguments containing
            the new values for the attributes.
        """

        collo = ("id", "size", "x", "y")
        for attrr, valuee in zip(collo, args):
            setattr(self, attrr, valuee)

        for atr, value in kwargs.items():
            setattr(self, atr, value)
