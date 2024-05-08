#!/usr/bin/python3

"""the function to make sure that instance of a class"""


def inherits_from(obj, a_class):
    """this inherited (directly or indirectly) from the specified class """
    return isinstance(obj, a_class) and \
        obj.__class__ is not a_class
