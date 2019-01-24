# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 16:21:34 2019

@author: computer
"""

def f(u, t):
    """2x2 system for a van der Pool oscillator."""
    return [u[1], 3.*(1. - u[0]*u[0])*u[1] - u[0]]

import odespy, numpy
solver = odespy.Vode(f, rtol=0.0, atol=1e-6,
                     adams_or_bdf='adams', order=10)
solver.set_initial_condition([2.0, 0.0])
t_points = numpy.linspace(0, 30, 150)
u, t = solver.solve(t_points)

u0 = u[:,0]
from matplotlib.pyplot import *
plot(t, u0)
show()