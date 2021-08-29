# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:51:33 2021

@author: jphei
"""

from enum import Enum

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