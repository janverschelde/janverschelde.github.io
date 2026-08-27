# L-3 MCS 481 Fri 17 Jan 2025 : convex2dcgal.py
"""
Copied from
https://github.com/CGAL/cgal-swig-bindings/blob/main/examples/python/test_convex_hull_2.py
with modifications.
"""
from __future__ import print_function
from CGAL.CGAL_Kernel import Point_2
from CGAL import CGAL_Convex_hull_2

L = []
L.append(Point_2(0, 0))
L.append(Point_2(1, 0))
L.append(Point_2(0, 1))
L.append(Point_2(1, 1))
L.append(Point_2(0.5, 0.5))
L.append(Point_2(0.25, 0.25))
print('the input points :')
for p in L:
    print(p)
result = []
CGAL_Convex_hull_2.convex_hull_2(L, result)
print('the vertices :')
for p in result:
    print(p)
print('adding (2,2) ...')
L.append(Point_2(2, 2))
newpt = Point_2()
CGAL_Convex_hull_2.ch_n_point(L, newpt)
print(newpt)
