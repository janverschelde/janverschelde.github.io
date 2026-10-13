# L-22 MCS 481 Wed 14 Oct 2026 : voronoicgal.py

"""
Code adjusted from 
https://github.com/CGAL/cgal-swig-bindings/blob/main/examples/python/vd_2_point_location.py
"""

from __future__ import print_function
from CGAL.CGAL_Kernel import Point_2
from CGAL.CGAL_Voronoi_diagram_2 import Voronoi_diagram_2
from CGAL.CGAL_Voronoi_diagram_2 import Voronoi_diagram_2_Halfedge_handle

sites = []
sites.append(Point_2(0, 0))
sites.append(Point_2(100, 0))
sites.append(Point_2(100, 100))
sites.append(Point_2(0, 100))
sites.append(Point_2(200, 100))
sites.append(Point_2(100, 200))

print('the sites :')
for site in sites:
    print(site)

vd = Voronoi_diagram_2(sites)

query_point0 = sites[0]

print('The query point', query_point0, end='')

def print_query_type(vd, query_point):
    """
    Prints the type of the query point.
    """
    lr = vd.locate(query_point)
    if lr.is_vertex_handle():
        print(" is on a vertex.")
    elif lr.is_halfedge_handle():
        print(" is on an edge.")
    elif lr.is_face_handle():
        print(" is in a face.")
    else:
        print(" could not be located?")

print_query_type(vd, query_point0)

def print_endpoint(e, is_src):
    """
    Prints the end point of an edge e
    of the Voronoi diagram.
    If is_src, then also the start point of e
    is printed.
    """
    print("\t", end='')
    if is_src:
        if e.has_source():
            print(e.source().point())
        else:
            print("point at infinity")
    else:
        if e.has_target():
            print(e.target().point())
        else:
            print("point at infinity")

def print_vertices(vd, query_point):
    """
    Prints the vertices of a query point
    that is in a face of the Voronoi diagram vd.
    """
    lr = vd.locate(query_point)
    if not lr.is_face_handle():
        print("The query point is not in a face.")
    else:
        f = lr.get_face_handle()
        print("The vertices of the Voronoi face are (in counterclockwise order):")
        ec_start = f.outer_ccb()
        if ec_start.hasNext():
            done = ec_start.next()
            iter = Voronoi_diagram_2_Halfedge_handle()
            while True:
                iter = ec_start.next()
                print_endpoint(iter, False)
                if iter == done:
                    break

print_vertices(vd, query_point0)

query_point2 = sites[2]
print('The query point', query_point2, end='')
print_query_type(vd, query_point2)
print_vertices(vd, query_point2)
