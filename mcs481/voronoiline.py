# L-23 MCS 481 Fri 16 Oct 2026 : voronoiline.py
"""
A plot of a Voronoi diagram of 10 points (k, noise[k]),
where the y-coordinate is randomly generated.
As the bounding box is computed based on the coordinates
of the sites, many vertices of the Voronoi diagram are
not shown, as they then lie outside the box.
"""
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt

noise = np.random.random(10)*1.75
line = [(k, noise[k]) for k in range(10)]
points = np.matrix(line)
vor = Voronoi(points)
voronoi_plot_2d(vor)
plt.show()
