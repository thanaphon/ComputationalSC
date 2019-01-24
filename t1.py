# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:40:55 2018

@author: computer
"""

from scitools.std import *
try:
    k = eval(sys.argv[1])
    omega = eval(sys.argv[2])
    t = eval(sys.argv[3])
    x_min = eval(sys.argv[4])
    x_max = eval(sys.argv[5])
    n = eval(sys.argv[6])
except:
    print( 'Usage: {} k omega t x_min x_max n'.format( sys.argv[0]))
    sys.exit(1)
x = linspace(x_min, x_max, n)
f = exp((-k*x - omega*t)**2)*sin(k*x - omega*t)
plot(x, f)