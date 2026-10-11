# L-21 MCS 481 Mon 12 Oct 2026 : voronoi.py
"""
A plot of a Voronoi diagram of 10 random points.
"""
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt

points = np.random.rand(10, 2)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
