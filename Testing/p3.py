# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:46:16 2019

@author: computer
"""
import numpy as np
import matplotlib.pyplot as plt

# 
P = 2      # NeedGPA
Gc = 1.39  # Cumulative Grade
Tc = 81   # Total Credit 

#Gc = 1  # Cumulative Grade
#Tc = 100   # Total Credit 


calTn = lambda Tc, Gc , Ge : (P*Tc - Tc*Gc) / (Ge -P)
ls = np.linspace(3,4)
l = len(ls)

Cn = list(map(calTn, Tc*np.ones(l), Gc*np.ones(l) , ls))
plt.plot(ls,list(map(lambda x: x/3.0 ,Cn)))