# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:59:10 2019

@author: panho
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


plt.figure(figsize=(6,4),dpi=150)
plt.title("SIR model with different vaccination rate") 
plt.xlabel("time") 
plt.ylabel("number of people") 

N = 10000
i = 1
r = 0
beta = 0.3
gamma = 0.05
col = 10
for x in range(1, 11):
    time = 0
    s = N - i - 1000 * x
    if s > 0:
        I = [1]
        while time < 1000:
            mc = beta * (I[-1]/N)   #probility of infection
            a = np.random.choice(range(2),s,p=[1-mc,mc])
            a = sum(a)
            b = np.random.choice(range(2),i,p=[1-gamma,gamma])
            b = sum(b)
            s = s - a
            i = i + a - b
            r = r + b
            I.append(i)
    
            time = time + 1
    
    else:
        I = [0]
    plt.plot(I,label = str(x*10) +'%',color = cm.viridis(col))
    col = col + 33

plt.savefig("SIR_vaccination",type = "png")
plt.legend()
plt.show()