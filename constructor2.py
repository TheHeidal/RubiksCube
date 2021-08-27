# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:53:28 2021

@author: jphei
"""

from vpython import compound,quad,color,vec,vertex

U_Vs = [vec(-.5,.5,-.5),vec(.5,.5,-.5),vec(.5,.5,.5),vec(-.5,.5,.5)]
D_Vs = [x + vec(0,-1,0) for x in U_Vs]
L_Vs = [vec(-.5,.5,-.5),vec(-.5,.5,.5),vec(-.5,-.5,.5),vec(-.5,-.5,-.5)]
R_Vs = [x + vec(1,0,0) for x in L_Vs]
F_Vs = [vec(-.5,.5,.5),vec(.5,.5,.5),vec(.5,-.5,.5),vec(-.5,-.5,.5)]
B_Vs = [x + vec(0,0,-1) for x in F_Vs]

def make_quad(vectors, color):
    return quad(vs=[vertex(pos=vector,color=color) for vector in vectors])

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
    return make_piece(colors, map(_color2vectors, colors))

def _color2vectors(c):
    if c == color.yellow: return U_Vs
    if c == color.white: return D_Vs
    if c == color.red: return L_Vs
    if c == color.orange: return R_Vs
    if c == color.green: return F_Vs
    if c == color.blue: return B_Vs

# D layer
brw = make_piece([color.blue, color.red, color.white],
                 [B_Vs, L_Vs, D_Vs])
rw = make_piece([color.red, color.white], [L_Vs, D_Vs])
grw = make_piece([color.green, color.red, color.white],
                 [F_Vs, L_Vs, D_Vs])
gw = make_piece([color.green, color.white], [F_Vs, D_Vs])
gow = make_piece([color.green, color.orange, color.white],
                 [F_Vs, R_Vs, D_Vs])
ow = make_piece([color.orange, color.white], [R_Vs, D_Vs])
bow = make_piece([color.blue, color.orange, color.white],
                 [B_Vs, R_Vs, D_Vs])
bw = make_piece([color.blue, color.white], [B_Vs, D_Vs])
w = make_piece([color.white],[D_Vs])
# H layer
br = make_piece([color.blue, color.red],[B_Vs,L_Vs])
r = make_piece([color.red], [L_Vs])

# y = make_quad(U_Vs, color.yellow)
# w = make_quad(D_Vs, color.white)
# g = make_quad(L_Vs, color.green)
# b = make_quad(R_Vs, color.blue)
# o = make_quad(F_Vs, color.orange)
# r = make_quad(B_Vs, color.red)