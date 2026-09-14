# L-9 MCS 481 Mon 14 Sep 2026 : triangulation_2.py
"""
Illustrates the construction of a triangulation
with the cgal-swig-bindings.
"""
from __future__ import print_function
from CGAL.CGAL_Kernel import Point_2
from CGAL.CGAL_Triangulation_2 import Triangulation_2

L = []
L.append(Point_2(-2, 1))
L.append(Point_2(-2, 4))
L.append(Point_2(-1, 3))
L.append(Point_2(0, 5))
L.append(Point_2(0, 0))
L.append(Point_2(2, 1))
L.append(Point_2(2, 4))
L.append(Point_2(1, 3))
print('the points on input :')
for point in L:
    print(point)

T = Triangulation_2()
T.insert(L)

print('number of faces :', T.number_of_faces())
print('number of vertices :', T.number_of_vertices())

print('the edges :')
cnt = 0
for e in T.all_edges():
    if not T.is_infinite(e):
        print(T.segment(e))
        cnt = cnt + 1
print('counted', cnt, 'finite edges')
print('the faces :')
cnt = 0
for f in T.all_faces():
    if not T.is_infinite(f):
         print(T.triangle(f))
         cnt = cnt + 1
print('counted', cnt, 'finite faces')
