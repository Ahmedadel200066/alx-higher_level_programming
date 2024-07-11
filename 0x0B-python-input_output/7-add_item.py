#!/usr/bin/python3
""" adds all arguments to a Python
    list, and then save them to a file:
"""
import sys
import os
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":

if os.path.exists("add_item.json"):
    New_save = load_from_json("add_item.json")
else:
    New_save = []
    args = sys.argv[1:]
    New_save.extend(args)
    save_to_json(New_save, "add_item.json")
   