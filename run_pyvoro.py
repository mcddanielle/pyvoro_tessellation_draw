#!/usr/bin/python -tt

#import matplotlib
#from matplotlib import rc
#rc('font', family='sans-serif')
#rc('font', size=24.0)
#rc('text', usetex=True)

import numpy as np
import matplotlib.pyplot as plt

#functions written by D.M. to get and plot specific data files
import data_importerDM as di

import pyvoro

def plotvor(cells,particles,radii1):
    fig1 = plt.figure(figsize=(20,20))
    plt.xlim((0,60))
    plt.ylim((0,60))
    plt.xlabel("X",fontsize=32)
    plt.ylabel("Y",fontsize=32)
    plt.axes().set_aspect('equal') #, 'datalim')
    plt.hold(True)
    plt.tick_params(labelsize=26)
    
    plt.scatter(particles[2],particles[3],s=radii1*200,
                marker='o',c=particles[1],cmap=plt.cm.Set1)
    
    for cell in cells:

        #plot from voronoi tessellation
        #plt.scatter(cell["original"][0], cell["original"][1])
        
        vertices = np.array(cell["vertices"])
        
        #---------------------------------------------------------
        #to draw a closed cell (i.e. connect the first/last vertices)
        tag_on = np.array(cell["vertices"])[0]  #to be tagged
        tag_on = tag_on.reshape((1,2))          #to fit onto longer array 
        vertices = np.concatenate((vertices,tag_on),axis=0)
        #----------------------------------------------------------
        
        plt.plot(vertices[:,0], vertices[:,1], 'b-')
        
    plt.savefig('voro.png')

def vor_stats(cells):

    pN = np.array([0,0,0,0])
    
    for cell in cells:
        n_sides = len(cell["adjacency"])
        index1 = n_sides - 4
        
        if index1 < 4:            
            pN[index1] += 1

    norm_factor = float(sum(pN))
    
    return pN/norm_factor
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
if __name__ == "__main__":

    all_data = di.get_data("test_data.txt",7,sep=" ")

    id1 = all_data[0]
    type1 = all_data[1]
    x = all_data[2]
    y = all_data[3]

    radii1 = np.zeros(len(type1))
    
    for (i,value1) in zip(range(len(type1)),type1):
        if value1 == 1:
            radii1[i] = 0.7
        else:
            radii1[i] = 0.5

    cells = pyvoro.compute_2d_voronoi(
        zip(x,y), # point positions, 2D vectors this time.
        [[0.0, 60.0], [0.0, 60.0]], # box size, again only 2D this time.
        2.0, # block size; same as before.
        radii=radii1, # particle radii -- optional and keyword-compatible.
        periodic=[1,1] #periodic boundary conditions
    )

    #plotvor(cells,all_data,radii1)

    print cells[0]

    print vor_stats(cells)
