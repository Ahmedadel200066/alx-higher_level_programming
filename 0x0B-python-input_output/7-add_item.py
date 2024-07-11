#!/usr/bin/python3
"""This module is about managing a JSON file.

This script allows you to add items to a JSON file. It checks if the file
"add_item.json" exists. If it does, it loads the existing data from the file.
If it doesn't exist, it creates an empty list and saves it to the file. Then,
it appends the command line arguments to the list and saves the updated list
back to the file.

Functions:
- save_to_json_file: Saves Python objects to a JSON file.
- load_from_json_file: Loads Python objects from a JSON file.
"""

import os
import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__(
    "6-load_from_json_file.py").load_from_json_file

if (os.path.exists("add_item.json")):
    new_save = load_from_json_file("add_item.json")
else:
    new_save = []
    save_to_json_file([], "add_itme.json")
    new_save.extend(sys.argv[1:])
    save_to_json_file(new_save, "add_item.json")
