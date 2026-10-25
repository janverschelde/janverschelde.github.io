# L-27 MCS 481 Mon 26 Oct 2026 : delaunay.py
"""
A plot of a Delaunay triangulation of 10 random points.
"""
import numpy as np
from scipy.spatial import Delaunay, delaunay_plot_2d
from matplotlib import pyplot as plt

points = np.random.rand(10, 2)
tri = Delaunay(points)
delaunay_plot_2d(tri)
plt.show()
