# L-3 MCS 481 Fri 17 Jan 2025 : random2dhull.py
"""
The ConvexHull of scipy.spatial for the planar convex hull problem.
"""
import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from matplotlib import pyplot as plt

points = np.random.rand(20, 2)
hull = ConvexHull(points)
print('The vertices :')
print(hull.vertices)
print('The edges :')
for simplex in hull.simplices:
    print(simplex)
print('The equations :')
print(hull.equations)
convex_hull_plot_2d(hull)
plt.show()
