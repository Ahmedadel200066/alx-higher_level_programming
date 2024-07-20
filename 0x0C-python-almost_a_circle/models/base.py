#!/usr/bin/python3
"""
module Base
"""
class Base:
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        
        if id in None :
            __nb_objects = __nb_objects + 1
        else:
            self.id = id
