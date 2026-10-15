# L-23 MCS 481 Fri 16 Oct 2026 : voronoicluster.py
"""
For 10 points equally spaced on a circle, the Voronoi diagram
has a vertex of degree 10.  The script generates 10 such points,
with some noise added to the y-coordinate, 
which creates a cluster of vertices.
"""
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt

nbr = 10
angle = 2*np.pi/nbr
noise = np.random.random(nbr)*0.2
circle = [(np.cos(k*angle), np.sin(k*angle)+noise[k]) for k in range(nbr)]
points = np.matrix(circle)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
