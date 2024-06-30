#!/usr/bin/python3

import json
"""
This module provides a function to convert an object to a JSON string representation.
"""


def to_json_string(my_obj):
    """
    Convert the given object to a JSON string representation.

    Args:
        my_obj: The object to be converted.

    Returns:
        A JSON string representation of the object.
    """
    return json.dumps(my_obj)
