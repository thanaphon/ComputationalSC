# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:40:30 2019

@author: computer
"""

from ipywidgets import interactive, fixed

from lorenz import solve_lorenz
w=interactive(solve_lorenz,sigma=(0.0,50.0),rho=(0.0,50.0))
w

from sympy import * 
t , v0 , g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt = diff(y,t)


import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

t = np.linspace(-2*np.pi,2*np.pi,100)
x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2 *np.cos(3*t) - np.cos(4*t)






fn = lambda x : x**2
x = [1,2, 3]

import numpy as np
x = np.linspace(0,100,5)
print(x)
y = fn(x)

#y = map(fn,x)















