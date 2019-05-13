# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:02:28 2019

@author: panho
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# set up model parameters
beta = 0.3
gamma = 0.05

# make array of all susceptible population
population = np.zeros((100, 100))

# choose one random person to be infected
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

time = 0
while time < 100:
    # heat maps for different time points
    if time == 0:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    if time == 9:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    if time == 49:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    if time == 99:
        plt.figure(figsize = (6, 4), dpi = 150)
        plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')

    time = time + 1
    
    # find infected points
    infectedIndex = np.where(population==1)    
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours 
        for xNeighbour in range(x-1,x+2):
                for yNeighbour in range(y-1,y+2):
                    # don't infect yourself! 
                    if (xNeighbour,yNeighbour) != (x,y):
                        # make sure I don't fall off an edge
                        if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                            # only infect neighbours that are not already infected!
                            if population[xNeighbour,yNeighbour]==0:
                                population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                            # only recover neighbours that are not already recovered
                            if population[xNeighbour,yNeighbour]==1:
                                population[xNeighbour,yNeighbour]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]


