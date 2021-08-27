# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:15:46 2021

@author: jphei
"""

from enum import Enum
import vpython
import renderConstructor

class RubiksCube():
    """A representation of a Rubik's Cube"""
    # The cube is represented by a collection of pieces
    
    # !!! TODO
    def __init__(self):
        # draw the cube
        # associate rendered objects with the cube
        pass
    
    # !!!
    def shuffle(self):
        pass
    
    # !!!
    def turn(self, layer):
        pass
    
class RubiksPiece(vpython.vpython.compound):
    
    def __init__(self, compound):
        pass
    
class Layer(Enum):
    UP = 0
    UP_PRIME = 1
    DOWN = 2
    DOWN_PRIME = 3
    LEFT = 4
    LEFT_PRIME = 5
    RIGHT = 6
    RIGHT_PRIME = 7
    FRONT = 8
    FRONT_PRIME = 9
    BACK = 10
    BACK_PRIME = 11