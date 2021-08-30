# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:51:33 2021

@author: jphei
"""

from enum import Enum

class Color(Enum):
    WHITE = 0
    YELLOW = 2
    ORANGE = 4
    RED = 6
    GREEN = 8
    BACK = 10

class Layer(Enum):
    UP = 0
    DOWN = 2
    LEFT = 4
    RIGHT = 6
    FRONT = 8
    BACK = 10

class Turn(Enum):
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
    
    def toLayer(turn):
        """
        converts a Turn to the Layer the turn happens on

        Parameters
        ----------
        turn : Turn
            The turn to be converted

        Returns
        -------
        Layer
            The layer that would be turned.

        """
        if turn.value % 2 == 0:
            return Layer(turn.value)
        else:
            return Layer(turn.value - 1)