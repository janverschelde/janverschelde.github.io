// L-8 MCS 481 Fri 11 Sep 2026 : partitioning.cpp

// copied from
// https://doc.cgal.org/5.6.3/Partition_2/Partition_2_2y_monotone_partition_2_8cpp-example.html
// added output statements

#include <iostream>

#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Partition_traits_2.h>
#include <CGAL/partition_2.h>
#include <cassert>
#include <list>
 
typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef CGAL::Partition_traits_2<K>                         Traits;
typedef Traits::Point_2                                     Point_2;
typedef Traits::Polygon_2                                   Polygon_2;
typedef std::list<Polygon_2>                                Polygon_list;
typedef Polygon_2::Vertex_iterator VertexIterator;
 
void make_polygon(Polygon_2& polygon)
{
   polygon.push_back(Point_2(391, 374));
   polygon.push_back(Point_2(240, 431));
   polygon.push_back(Point_2(252, 340));
   polygon.push_back(Point_2(374, 320));
   polygon.push_back(Point_2(289, 214));
   polygon.push_back(Point_2(134, 390));
   polygon.push_back(Point_2( 68, 186));
   polygon.push_back(Point_2(154, 259));
   polygon.push_back(Point_2(161, 107));
   polygon.push_back(Point_2(435, 108));
   polygon.push_back(Point_2(208, 148));
   polygon.push_back(Point_2(295, 160));
   polygon.push_back(Point_2(421, 212));
   polygon.push_back(Point_2(441, 303));
}
 
int main( )
{
   Polygon_2    polygon;
   Polygon_list partition_polys;

   std::cout << "making a polygon ..." << std::endl;
 
   make_polygon(polygon);

   // traverse the vertices
   int nbr=0;
   for (VertexIterator vi = polygon.vertices_begin();
       vi != polygon.vertices_end(); ++vi)
   {
       std::cout << "-> vertex " << nbr++ << " = " << *vi << std::endl;
   }

   std::cout << "partitioning the polygon ..." << std::endl;

   CGAL::y_monotone_partition_2(polygon.vertices_begin(),
                                polygon.vertices_end(),
                                std::back_inserter(partition_polys));
 
   std::cout << "running through the polygons in the partition ..." << std::endl;

   int cnt=0;
   std::list<Polygon_2>::const_iterator   poly_it;
   for (poly_it = partition_polys.begin(); poly_it != partition_polys.end();
        poly_it++)
   {
      std::cout << "polygon " << cnt++ << std::endl;
      nbr=0;
      for (VertexIterator vi = (*poly_it).vertices_begin();
          vi != (*poly_it).vertices_end(); ++vi)
      {
          std::cout << "-> vertex " << nbr++ << " = " << *vi << std::endl;
      }

      assert(CGAL::is_y_monotone_2((*poly_it).vertices_begin(),
                                   (*poly_it).vertices_end()));
   }
 
   assert(CGAL::partition_is_valid_2(polygon.vertices_begin(),
                                     polygon.vertices_end(),
                                     partition_polys.begin(),
                                     partition_polys.end()));
 
   return 0;
}
