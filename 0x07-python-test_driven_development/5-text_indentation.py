#!/usr/bin/python3

""" this module for text indentation"""


def text_indentation(text):
    """
    Splits the given text into paragraphs based on the occurrence of certain punctuation marks.

    Args:
        text (str): The input text to be split into paragraphs.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    mark = 0
    for a in text:
        if mark == 0:
            if a == ' ':
                continue
            else:
                mark = 1
        if mark == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                mark = 0
            else:
                print(a, end="")
