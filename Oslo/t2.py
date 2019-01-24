# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:07:06 2018

@author: computer
"""

import sympy as sm
x, a, b = sm.symbols ('x a b')
equation = a * x + b
root = sm.solve (equation, x) # solve equation wrt x
# Solution in root [0]


#use numpy version of all mathematics:
from numpy import *
import matplotlib.pyplot as plt

#factorial is not in numpy, need import from math:
from math import factorial

#a)
def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):
    #compute x values and reference solution
    x = linspace(xmin, xmax, n)
    y_exact = exact(x)
    s = zeros_like(x)

    #initialize plot with axes, and call plot first time
    plt.plot(x,y_exact)
    lines = plt.plot(x,s)
    plt.axes([xmin, xmax, ymin, ymax])

    #update data and redraw in a for loop
    for k in range(M,N+1):
        s = s + fk(x,k)
        lines[0].set_ydata(s)
        plt.draw()
        plt.pause(0.25)

#call the function with the correct arguments

#b)
def f_sin(x,k):
    return (-1)**k*x**(2*k+1)/factorial(2*k+1)

animate_series(f_sin,0,40,0,13*pi,-2,2,1000,sin)

#c)
def exp_inv(x):
    return exp(-x)

def f_exp(x,k):
    return (-x)**k/factorial(k)

#animate_series(f_exp,0,30,0,15,-0.5,1.4,100,exp_inv)