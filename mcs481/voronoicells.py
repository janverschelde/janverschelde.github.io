# L-21 MCS 481 Mon 12 Oct 2026 : voronoicells.py
"""
We examine the attributes of a Voronoi diagram.
"""
import numpy as np
from scipy.spatial import Voronoi

points = np.random.rand(10, 2)
vor = Voronoi(points)
print('the input points :')
print(vor.points)
print('the vertices :')
print(vor.vertices)
print('the ridge vertices :')
print(vor.ridge_vertices)
print('the ridge points :')
print(vor.ridge_points)
print('the cells :')
for region in vor.regions:
    print(region)
print('the point_region :')
print(vor.point_region)
