#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle object.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
            Defaults to 0.
            id (int, optional): The unique identifier of the rectangle.
            Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle.

        Args:
            width (int): The new width of the rectangle.
        """
        self.Validate("width", width)
        self.__width = width

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle.

        Args:
            height (int): The new height of the rectangle.
        """
        self.Validate("height", height)
        self.__height = height

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
            x (int): The new x-coordinate of the rectangle's position.
        """
        self.Validate("x", x, check=False)
        self.__x = x

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
            y (int): The new y-coordinate of the rectangle's position.
        """
        self.Validate("y", y, check=False)
        self.__y = y

    def Validate(self, name, value, check=True):
        """
        Validates the value of a given attribute.

        Args:
            name (str): The name of the attribute.
            value (int): The value to be validated.
            check (bool, optional): 
            Specifies whether to perform additional checks. Defaults to True.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not within the specified range.

        """
        if value is not int:
            raise TypeError(f"{name} must be an integer")
        if check:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
