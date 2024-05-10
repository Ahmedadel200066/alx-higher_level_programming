#!/usr/bin/python3


Rectangle = __import__("9-rectangle.py").Rectange


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        if type(size) is int:
            if size >= 0:
                self.integer_validator("size", size)
                self.__size = size
