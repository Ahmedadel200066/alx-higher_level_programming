#!/usr/bin/python3

"""this is say my name module"""


def say_my_name(first_name, last_name=""):
    """that function tells you your name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(format("My name is"), first_name, last_name)
