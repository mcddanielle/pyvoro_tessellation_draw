#SOURCE: https://pastebin.com/wNaYAPvN
# install requirements
# sudo pip install numpy matplotlib pyvoro

#g            ax.set_aspect('equal')

import pyvoro
import numpy as np
import matplotlib.pyplot as plt
 
N = 30                              # number of points to generate
points = np.random.rand(N, 2) * 10  # point locations
radii = np.ones((N,)) * 0.01        # point radii ("weights")
 
def plotvor(cells):
    plt.figure(figsize=(20,20))
    plt.xlim((0,10))
    plt.ylim((0,10))
    plt.axes().set_aspect('equal', 'datalim')
    
    plt.hold(True)
    for cell in cells:
        plt.scatter(cell["original"][0], cell["original"][1])
        vertices = np.array(cell["vertices"])
        vertices = np.concatenate((vertices,
            cell["vertices"][0].reshape((1,2))))
        plt.plot(vertices[:,0], vertices[:,1], 'b-')
    plt.show()
 
cells = pyvoro.compute_2d_voronoi(
    points,
    [[0.0, 10.0], [0.0, 10.0]], # box size
    0.5,                        # block size
    radii = radii)
 
plotvor(cells)
