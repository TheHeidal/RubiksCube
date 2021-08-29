# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:00:02 2021

@author: jphei
"""

from vpython import vertex,vec,quad,color,compound,radians

ORIGIN = vec(1.5,1.5,1.5)

X_AXIS = vec(1,0,0)
Y_AXIS = vec(0,1,0)
Z_AXIS = vec(0,0,1)

XY_COORDS = [vec(0,0,0), vec(1,0,0), vec(1,1,0), vec(0,1,0)]
YZ_COORDS = [vec(0,0,0), vec(0,1,0), vec(0,1,1), vec(0,0,1)]
ZX_COORDS = [vec(0,0,0), vec(0,0,1), vec(1,0,1), vec(1,0,0)]
COORDS = [XY_COORDS, YZ_COORDS, ZX_COORDS] 

# B = color.blue
# G = color.green
# O = color.orange
# R = color.red
# W = color.white
# Y = color.yellow

def make_quad(vecs, color):
    """
    Makes a quad

    Parameters
    ----------
    vecs : [vpython.cyvector.vector]
        corners of the quad.
        make sure they are in order
    color : vpython.cyvector.vector
        colors of each corner

    Returns
    -------
    vpython.vpython.quad
        a quad with the given vectors

    """
    return quad( vs=[vertex( pos=vector, color=color) for vector in vecs])

def make_corner(colors):
    """
    creates a corner for a rubik's cube

    Parameters
    ----------
    colors : [vpython.cyvector.vector]
        Colors of the sides.
        first is xy, second is yz, third is zx
        only uses the first three vectors

    Returns
    -------
    vpython.vpython.compound
        a corner of a rubik's cube, in the back, down, and left layers
    """
    return compound( [make_quad(vecs,color) for (vecs,color) in zip(COORDS,colors)])

def make_edge(colors):
    """
    creates an edge of a rubik's cube

    Parameters
    ----------
    colors : [vpython.cyvector.vector]
        Colors of the sides.
        first is xy, second is zx
        only uses the first two vectors

    Returns
    -------
    ret : vpython.vpython.compound
        an edge of a rubik's cube, located on the back and down layers

    """
    ret = compound( [make_quad(vecs, color) for (vecs, color) in zip([XY_COORDS,ZX_COORDS], colors)])
    ret.pos = ret.pos + vec(1,0,0)
    return ret

def make_center(color):
    ret = compound([make_quad(XY_COORDS, color)])
    ret.pos = ret.pos + vec(1,1,0)
    return ret

# Corners
# down layer
brw = make_corner( [color.blue, color.red, color.white] )
grw = make_corner( [color.red, color.green, color.white] )
grw.rotate(radians(90), Y_AXIS, ORIGIN)
gow = make_corner( [color.green, color.orange, color.white])
gow.rotate(radians(180), Y_AXIS, ORIGIN)
bow = make_corner( [color.orange, color.blue, color.white])
bow.rotate(radians(270), Y_AXIS, ORIGIN)
# up layer
boy = make_corner([color.blue, color.orange, color.yellow])
boy.rotate(radians(180), Z_AXIS, ORIGIN)
goy = make_corner([color.orange, color.green, color.yellow])
goy.rotate(radians(90), Y_AXIS, ORIGIN)
goy.rotate(radians(180), Z_AXIS, ORIGIN)
gry = make_corner([color.green, color.red, color.yellow])
gry.rotate(radians(180), Y_AXIS, ORIGIN)
gry.rotate(radians(180), Z_AXIS, ORIGIN)
bry = make_corner([color.red, color.blue, color.yellow])
bry.rotate(radians(270), Y_AXIS, ORIGIN)
bry.rotate(radians(180), Z_AXIS, ORIGIN)

# Edges
# down layer
bw = make_edge( [color.blue, color.white])
rw = make_edge( [color.red, color.white])
rw.rotate( radians(90), Y_AXIS, ORIGIN)
gw = make_edge([color.green, color.white])
gw.rotate( radians(180), Y_AXIS, ORIGIN)
ow = make_edge( [color.orange, color.white])
ow.rotate( radians(270), Y_AXIS, ORIGIN)
# horizontal layer
br = make_edge( [color.blue, color.red])
br.rotate( radians(-90), Z_AXIS, ORIGIN)
gr = make_edge( [color.red, color.green])
gr.rotate( radians(-90), Z_AXIS, ORIGIN)
gr.rotate( radians(90), Y_AXIS, ORIGIN)
go = make_edge( [color.green, color.orange])
go.rotate( radians(-90), Z_AXIS, ORIGIN)
# !!! this just does not work if I set it to radians(180)
# or any sequence of rotations adding up to 180
go.rotate( radians(180), Y_AXIS, ORIGIN)


bo = make_edge( [color.orange, color.blue])
bo.rotate( radians(-90), Z_AXIS, ORIGIN)
bo.rotate( radians(270), Y_AXIS, ORIGIN)
# up layer
by = make_edge( [color.blue, color.yellow])
by.rotate( radians(180), Z_AXIS, ORIGIN)
oy = make_edge( [color.orange, color.yellow])
oy.rotate( radians(90), Y_AXIS, ORIGIN)
oy.rotate( radians(180), Z_AXIS, ORIGIN)
gy = make_edge( [color.green, color.yellow])
gy.rotate( radians(180), Y_AXIS, ORIGIN)
gy.rotate( radians(180), Z_AXIS, ORIGIN)
ry = make_edge( [color.red, color.yellow])
ry.rotate( radians(270), Y_AXIS, ORIGIN)
ry.rotate( radians(180), Z_AXIS, ORIGIN)

# Centers
b = make_center(color.blue)
r = make_center(color.red)
r.rotate( radians(90), Y_AXIS, ORIGIN)
g = make_center(color.green)
g.rotate( radians(180), Y_AXIS, ORIGIN)
o = make_center(color.orange)
o.rotate( radians(270), Y_AXIS, ORIGIN)
w = make_center(color.white)
w.rotate( radians(-90), X_AXIS, ORIGIN)
y = make_center(color.yellow)
y.rotate( radians(90), X_AXIS, ORIGIN)
