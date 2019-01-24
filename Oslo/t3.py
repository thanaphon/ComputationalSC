# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:43:06 2018

@author: computer
"""

def solve_quadratic_equation(a, b, c):
    q = b**2 - 4*a*c
    if q < -1E-14: # q < 0 with tolerance
        raise ValueError('q=%g<0 is not allowed' % q)

    x1 = (-b + sqrt(q))/(2*a)
    x2 = (-b - sqrt(q))/(2*a)
    if q > 1E-14: # q > 0 with tolerance
        return x1, x2
    else:
        return x1, None

from math import sqrt
print (solve_quadratic_equation(1, 3, 1))