# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:52:59 2019

@author: panho
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
s = 9999
i = 1
r = 0

S = [9999]
I = [1]
R = [0]
N = 10000
beta = 0.3
gamma = 0.05

# need a loop to model the process of infection
# need to consider the the infection rate upon contact (beta), and the probability of making contact with an infected individual.
# need to consider changes of S, I and R after infection
time = 0
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
    S.append(s)
    R.append(r)
    time = time + 1


plt.figure(figsize=(6,4),dpi=150)
plt.title("SIR model") 
plt.xlabel("time") 
plt.ylabel("number of people") 
plt.plot(S, label = 'susceptible')
plt.plot(I, label = 'infected')
plt.plot(R, label = 'recovered')

plt.savefig("SIR",type = "png")
plt.legend()
plt.show()
