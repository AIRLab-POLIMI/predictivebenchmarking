#include "ros/ros.h"
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <list>
#include <vector>
#include <math.h>

#include <ctime>

#include <ipa_room_segmentation/room_class.h>
#include <ipa_room_segmentation/abstract_voronoi_segmentation.h>

#define HAVE_INT64_T_64  # Prevents conflict with OpenCV typedef of int64
 #include <geos/geom/Polygon.h>
 #include <geos/geom/Point.h>
 #include <geos/geom/LinearRing.h>
 #include <geos/geom/CoordinateSequenceFactory.h>
 #include <geos/geom/GeometryFactory.h>
 #include <geos/opBuffer.h>
#undef HAVE_INT64_T_64


class VoronoiGraph : public AbstractVoronoiSegmentation
{
protected:

public:

	VoronoiGraph();

	//the segmentation-algorithm
	void segmentMap(const cv::Mat& map_to_be_labeled, cv::Mat& segmented_map, cv::Mat& voronoi_map, geos::geom::Geometry* floorPolygon, double map_resolution_from_subscription,
			double room_area_factor_lower_limit, double room_area_factor_upper_limit, int neighborhood_index, int max_iterations,
			double min_critical_point_distance_factor, double max_area_for_merging, std::vector<Room>& rooms, bool display_map=false);
};
