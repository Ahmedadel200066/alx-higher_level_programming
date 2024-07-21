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
            Specifies whether to perform additional checks.
            Defaults to True.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not within the specified range.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if check:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle by printing '#' characters
        in the shape of the rectangle.
        """
        for z in range(self.y):
            print()
        for a in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for b in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args):
        """Update the attributes of the rectangle.

        Args:
            *args: Variable length argument
            list containing the new values for the attributes.
                   The order of the arguments
                   should match the order of the attributes:
                   id, width, height, x, y.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        The string includes the class name, object ID, coordinates (x, y),
        and dimensions (width, height) of the Rectangle.

        Returns:
            A string representation of the Rectangle object.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"
