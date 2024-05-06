#!/usr/bin/python3

"""the function to make sure that instance of a class"""


def inherits_from(obj, a_class):
    """this inherited (directly or indirectly) from the specified class """
    if issubclass(obj, a_class):
        return True
    else:
        return False
