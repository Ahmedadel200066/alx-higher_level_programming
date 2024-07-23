#!/usr/bin/python3
"""
module Base
"""
import json


class Base:
    """
    The Base class serves as the base class for other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The ID of the instance. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a Python object.

        Args:
            json_string (str): The JSON string to be converted.

        Returns:
            list: The Python object representation of the JSON string.

        """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            None
        """
        filename = f"{cls.__name__}" + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                list_dicts = []
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
            file.write(Base.to_json_string(list_dicts))
