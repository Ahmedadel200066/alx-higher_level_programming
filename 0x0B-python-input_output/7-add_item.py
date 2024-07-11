#!/usr/bin/python3
"""this module about this json file"""
import os
import sys
save_to_json_file = __import__("5-save_to_json_file.py").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file

if (os.path.exists("add_item.json")):
   new_save = load_from_json_file("add_item.json")
else:
   new_save = []
   save_to_json_file([],"add_itme.json")
   