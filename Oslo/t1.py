# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 15:41:49 2018

@author: computer
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy
import ODESolver
sympy.init_printing()
# save plots in both png (raster graphics) and pdf (vector graphics)
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('png', 'pdf')

# render plots with double dpi (for nice viewing on high DPI displays)
#%config InlineBackend.figure_format = 'retina'
#from IPython.display import set_matplotlib_formats
#set_matplotlib_formats('retina')

a, t = sympy.symbols('a t')

u = sympy.exp(-a*t)
u

du = u.diff(t)
du

du.integrate(t)

factor = du/u
factor

u_func = sympy.lambdify((a, t), u, 'numpy')


a_value = 2
n = 20
x = np.linspace(0, 1, n)
y = u_func(a_value, x)
y



plt.plot(x, y)
plt.title('$u(t) = %s $' % sympy.latex(u))
plt.xlabel('t')
plt.ylabel('u')
plt.savefig('plot_exact.pdf')
plt.show()




class Decay:
    def __init__(self, a):
        self.a = a
        
    def __call__(self, u, t):
        return -self.a*u
    
    
u0 = u.subs(a, a_value).subs(t, 0)
u0    
    
    
f = Decay(2)
solver = ODESolver.ForwardEuler(f)
solver.set_initial_condition(u0)
u_FE, t_FE = solver.solve(x)

solver = ODESolver.RungeKutta4(f)
solver.set_initial_condition(u0)
u_RK4, t_RK4 = solver.solve(x)

plt.plot(x, y, label='exact')
plt.plot(t_FE, u_FE, label='Forward Euler')
plt.plot(t_RK4, u_RK4, label='RungeKutta4')
plt.title('$u(t) = %s $' % sympy.latex(u)) # 
plt.xlabel('t')
plt.ylabel('u')
plt.legend(loc='best')
plt.show()

