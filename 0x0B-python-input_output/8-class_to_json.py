#!/usr/bin/python3

"""this module for converts a python object to a dictionary rep"""


def class_to_json(obj):
    """
    Converts a Python object to a dictionary representation.

    Args:
        obj: The object to be converted.

    Returns:
        A dictionary representation of the object, where the keys are the attribute names
        and the values are the attribute values.

    """
    return {key: value for key, value in obj.__dict__.items() \
            if isinstance(value, (list, dict, str, int, bool))}
