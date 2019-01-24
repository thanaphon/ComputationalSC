# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:09:14 2019

@author: computer
"""

def foo(x,y):
    return (x*y)

def test_foo():
    error = 1E-10
    xs = [-1.8, -1 , 0 , 1.8 , 5.2, 1000]
    ys = [-1.9, 1 , 0 , 1.8, 3 , 2000]
    expected = [ 3.42, -1, 0 , 3.24, 15.6, 2000001 ]
    
    for x , y ,e in zip(xs,ys, expected):
        comp = foo(x,y)
        txt = ' {} not eq {}'.format(e,comp)
        assert abs(comp - e) < error , txt
        