# L-23 MCS 481 Fri 16 Oct 2026 : voronoicircle.py
"""
A plot of a Voronoi diagram of 10 points equally spaced
on a circle, which creates a vertex of degree 10.
"""
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt

nbr = 10
angle = 2*np.pi/nbr
circle = [(np.cos(k*angle), np.sin(k*angle)) for k in range(nbr)]
points = np.matrix(circle)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
