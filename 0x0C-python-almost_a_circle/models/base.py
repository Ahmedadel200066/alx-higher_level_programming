#!/usr/bin/python3
"""
module Base
"""
class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - DG 3mr 7a7a remix
        """
        if id is not None :
            self.id = id
        else :
            Base.__nb_objects += 1
            
  
  






