#!/usr/bin/python3

"""this class is for list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Returns:
            list: The sorted list.
        """
        return sorted(self)
