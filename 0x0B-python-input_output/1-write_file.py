#!/usr/bin/python3

"""
This module provides a function to write a string to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
