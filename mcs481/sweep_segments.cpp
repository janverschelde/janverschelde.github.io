// L-4 MCS 481 Mon 31 Aug 2026 : sweep_segments.cpp

// Modification of examples/Surface_sweep_2/plane_sweep.cpp
// to compute the intersection points of three line segments.
// Writing the executable to sweep, compile with the command
// g++ sweep_segments.cpp -lgmp -lmpfr -o sweep

#include <CGAL/Exact_predicates_exact_constructions_kernel.h>
#include <CGAL/Arr_segment_traits_2.h>
#include <CGAL/Surface_sweep_2_algorithms.h>

typedef CGAL::Exact_predicates_exact_constructions_kernel Kernel;
typedef Kernel::Point_2                                   Point_2;
typedef CGAL::Arr_segment_traits_2<Kernel>                Traits_2;
typedef Traits_2::Curve_2                                 Segment_2;

int main()
{
  // construct the input segments
  Segment_2 segments[] = {Segment_2(Point_2(0, 0), Point_2(2, 2)),
                          Segment_2(Point_2(1, 0), Point_2(0, 2)),
                          Segment_2(Point_2(2, 0), Point_2(1, 2))};

  // compute all intersection points
  std::list<Point_2> pts;

  CGAL::compute_intersection_points(segments, segments + 3,
                                    std::back_inserter(pts));

  // print the result
  std::cout << "Found " << pts.size() << " intersection points: " << std::endl;
  std::copy(pts.begin(), pts.end(),
            std::ostream_iterator<Point_2>(std::cout, "\n"));

  return 0;
}
