# L-4 MCS 481 Mon 31 Aug 2026 : line_segments.py
"""
Consider three line segments defined by the tuples
((0, 0), (2, 2)), ((1, 0), (0, 2)), ((2, 0), (1, 1))
and compute their intersections.
"""
from CGAL.CGAL_Kernel import Point_2
from CGAL.CGAL_Kernel import Segment_2
from CGAL.CGAL_Kernel import intersection

segments = []
segments.append(Segment_2(Point_2(0, 0), Point_2(2, 2)))
segments.append(Segment_2(Point_2(1, 0), Point_2(0, 2)))
segments.append(Segment_2(Point_2(2, 0), Point_2(1, 2)))
for i in range(len(segments)):
    for j in range(i+1, len(segments)):
        intsisj = intersection(segments[i], segments[j])
        print('segments', i, 'and', j, end=' ')
        if intsisj.empty():
            print('do not intersect')
        elif not intsisj.is_Point_2():
            print('do not intersect in a point')
        else:
            iptsisj = intsisj.get_Point_2()
            print('intersect :', end=' ')
            print(iptsisj.x(), ',', iptsisj.y())
