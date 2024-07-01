#!/usr/bin/python3
"""this module to writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename=""):
    """
    Save the given object to a JSON file.

    Args:
        my_obj (any): The object to be saved.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
