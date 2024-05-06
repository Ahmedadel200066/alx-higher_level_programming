#!/bin/usr/python3

"""this method takes an obj as input and"""
def lookup(obj):
    """
    This function takes an object as input and returns a list of all the available attributes and methods of that object.

    Args:
        obj: The object for which to retrieve the attributes and methods.

    Returns:
        A list of strings representing the attributes and methods of the object.

    """
    return dir(obj)
