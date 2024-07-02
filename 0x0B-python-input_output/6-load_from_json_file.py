#!/usr/bin/python3
"""this module about this json file"""
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return the deserialized object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The deserialized object from the JSON file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If the JSON file is not valid.

    """
    with open(filename, "r") as f:
        return json.load(f)
