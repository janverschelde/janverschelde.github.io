# L-28 MCS 481 Wed 28 Oct 2026 : duality.py
"""
A plot of a Voronoi diagram and Delaunay triangulation
of 10 random points illustrates the duality.
"""
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import Delaunay, delaunay_plot_2d
from matplotlib import pyplot as plt

points = np.random.rand(10, 2)
vor = Voronoi(points)
tri = Delaunay(points)
fig, axs = plt.subplots()
voronoi_plot_2d(vor, ax=axs)
delaunay_plot_2d(tri, ax=axs)
plt.show()
