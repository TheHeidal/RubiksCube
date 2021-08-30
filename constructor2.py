# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:53:28 2021

@author: jphei
"""

from vpython import compound,quad,color,vec,vertex,radians
from layer import Layer, Turn

class CubeRender():

    ORIGIN = vec(0,0,0)

    def __init__(self):
        """
        Constructs a solved rubick's cube, with green as F and yellow and U

        Returns
        -------
        None.

        """
        # D layer
        brw = make_piece_wrapper([color.blue, color.red, color.white])
        rw = make_piece_wrapper([color.red, color.white])
        grw = make_piece_wrapper([color.green, color.red, color.white])
        gw = make_piece_wrapper([color.green, color.white])
        gow = make_piece_wrapper([color.green, color.orange, color.white])
        ow = make_piece_wrapper([color.orange, color.white])
        bow = make_piece_wrapper([color.blue, color.orange, color.white])
        bw = make_piece_wrapper([color.blue, color.white])
        w = make_piece_wrapper([color.white])
        # H layer
        br = make_piece_wrapper([color.blue, color.red])
        r = make_piece_wrapper([color.red])
        rg = make_piece_wrapper([color.red, color.green])
        g = make_piece_wrapper([color.green])
        go = make_piece_wrapper([color.green, color.orange])
        o = make_piece_wrapper([color.orange])
        bo = make_piece_wrapper([color.blue, color.orange])
        b = make_piece_wrapper([color.blue])
        # U layer
        bry = make_piece_wrapper([color.blue, color.red, color.yellow])
        ry = make_piece_wrapper([color.red, color.yellow])
        gry = make_piece_wrapper([color.green, color.red, color.yellow])
        gy = make_piece_wrapper([color.green, color.yellow])
        goy = make_piece_wrapper([color.green, color.orange, color.yellow])
        oy = make_piece_wrapper([color.orange, color.yellow])
        boy = make_piece_wrapper([color.blue, color.orange, color.yellow])
        by = make_piece_wrapper([color.blue, color.yellow])
        y = make_piece_wrapper([color.yellow])
        
        self.pieces_list = [brw, rw, grw, gw, gow, ow, bow, bw, w,
                  br, r, rg, g, go, o, bo, b,
                  bry, ry, gry, gy, goy, oy, boy, by, y]


    def doTurn(self, turn):
        """
        rotates a layer of the cube around the origin

        Parameters
        ----------
        turn : layer.Turn
            what layer should be rotated and in which direction

        Returns
        -------
        None.

        """
        layer = Turn.toLayer(turn)
        turning_pieces = [piece for piece in self.pieces_list
                          if CubeRender._isOnLayer(piece, layer)]
        self._turn_rotate(turning_pieces, turn)
    
    # !!!
    def _isOnLayer(piece, layer):
        """
        returns True if the piece is currently on the layer

        Parameters
        ----------
        piece : vpython.vpython.compound
            A piece of the rubik's cube
        layer : layer.Layer
            The layer the piece should be on

        Returns
        -------
        Boolean

        """
        if layer == Layer.UP:
            return piece.pos.y > 0.5
        elif layer == Layer.DOWN:
            return piece.pos.y < -0.5
        elif layer == Layer.LEFT:
            return piece.pos.x < -0.5
        elif layer == Layer.RIGHT:
            return piece.pos.x > 0.5
        elif layer == Layer.FRONT:
            return piece.pos.z > 0.5
        elif layer == Layer.BACK:
            return piece.pos.z < -0.5
        else: raise NotImplementedError(layer.name + ' is not implemented')
    
    # !!!
    def _turn_rotate(self, turn_pieces, turn):
        """
        rotates turn_pieces around the origin 

        Parameters
        ----------
        turn_pieces : [vpthon.vpython.compound]
            the pieces to be turned
        turn: layer.Turn
            What layer to turn, and in what direction

        Returns
        -------
        None.

        """
        layer = Turn.toLayer(turn)
        if layer == Layer.UP:
            axis = vec(0,1,0)
        elif layer == Layer.DOWN:
            axis = vec(0,-1,0)
        elif layer == Layer.LEFT:
            axis = vec(-1,0,0)
        elif layer == Layer.RIGHT:
            axis = vec(1,0,0)
        elif layer == Layer.FRONT:
            axis = vec(0,0,1)
        elif layer == Layer.BACK:
            axis = vec(0,0,-1)
        else: raise NotImplementedError(layer.name + ' is not implemented')
        angle = radians(90 - (180 * (turn.value % 2))) # should mean turns are 90deg and prime turns are -90 deg
        for x in turn_pieces:
            x.rotate(angle, axis, self.ORIGIN)
            
            
    

# !!! should probably move this into the class
U_Vs = (vec(-.5,.5,-.5),vec(.5,.5,-.5),vec(.5,.5,.5),vec(-.5,.5,.5))
D_Vs = tuple(x + vec(0,-1,0) for x in U_Vs)
L_Vs = (vec(-.5,.5,-.5),vec(-.5,.5,.5),vec(-.5,-.5,.5),vec(-.5,-.5,-.5))
R_Vs = tuple(x + vec(1,0,0) for x in L_Vs)
F_Vs = (vec(-.5,.5,.5),vec(.5,.5,.5),vec(.5,-.5,.5),vec(-.5,-.5,.5))
B_Vs = tuple(x + vec(0,0,-1) for x in F_Vs)

def make_quad(vectors, color):
    return quad(vs=[vertex(pos=vector,color=color) for vector in vectors])

# !!! make sure doc mentions it positions piece
def make_piece(colors, sides):
    piece = compound([make_quad(vectors, color) for (vectors, color) in zip(sides, colors)])
    # should probably rewrite into a for statement to stop going over sides 6 times
    for x in sides:
        if x is U_Vs: piece.pos += vec(0,1,0)
        elif x is D_Vs: piece.pos += vec(0,-1,0)
        elif x is L_Vs: piece.pos += vec(-1,0,0)
        elif x is R_Vs: piece.pos += vec(1,0,0)
        elif x is F_Vs: piece.pos += vec(0,0,1)
        elif x is B_Vs: piece.pos += vec(0,0,-1)
    return piece

def make_piece_wrapper(colors):
    return make_piece(colors, list(map(_color2vectors, colors)))

def _color2vectors(c):
    if c == color.yellow: return U_Vs
    if c == color.white: return D_Vs
    if c == color.red: return L_Vs
    if c == color.orange: return R_Vs
    if c == color.green: return F_Vs
    if c == color.blue: return B_Vs


cubeRender = CubeRender()
