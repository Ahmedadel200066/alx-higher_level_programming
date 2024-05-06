#!/usr/bin/python3


"""this is instance module"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or a subclass of it.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the class or a subclass of it, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
