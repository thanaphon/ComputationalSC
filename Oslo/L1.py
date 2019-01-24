# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 09:30:24 2019

@author: computer
"""

import numpy as num
import matplotlib.pyplot as plt



x  = num.linspace(0,10,100)
fn = lambda x :(x**2)
plt.plot(x,fn(x))





