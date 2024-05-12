#!/usr/bin/python3

"""
This module contains a function to append a string to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
