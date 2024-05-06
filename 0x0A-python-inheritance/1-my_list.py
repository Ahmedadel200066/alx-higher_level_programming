#!/usr/bin/python3

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Returns:
            list: The sorted list.
        """
        x= list(sorted(self))
        return x
