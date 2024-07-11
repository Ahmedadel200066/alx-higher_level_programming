#!/usr/bin/python3
"""This module is about managing a JSON file.

Functions:
- save_to_json_file: Saves Python objects to a JSON file.
- load_from_json_file: Loads Python objects from a JSON file.
"""

import os
import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

if (os.path.exists("add_item.json")):
    new_save = load_from_json_file("add_item.json")
else:
    new_save = []
    new_save.extend(sys.argv[1:])
    save_to_json_file(new_save, "add_item.json")
