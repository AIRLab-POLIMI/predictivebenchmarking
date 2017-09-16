#include <ipa_room_segmentation/voronoi_graph.h>

#include <ipa_room_segmentation/wavefront_region_growing.h>
#include <ipa_room_segmentation/contains.h>

#include <ipa_room_segmentation/timer.h>
#include <set>

VoronoiGraph::VoronoiGraph()
{

}

void VoronoiGraph::segmentMap(const cv::Mat& map_to_be_labeled, cv::Mat& segmented_map, cv::Mat& voronoi_map, geos::geom::Geometry* floorPolygon, double map_resolution_from_subscription,
		double room_area_factor_lower_limit, double room_area_factor_upper_limit, int neighborhood_index, int max_iterations,
		double min_critical_point_distance_factor, double max_area_for_merging, std::vector<Room>& rooms, bool display_map)
{
	//****************Create the Generalized Voronoi-Diagram**********************
	//This function takes a given map and segments it with the generalized Voronoi-Diagram. It takes following steps:
	//	I. It calculates the generalized Voronoi-Diagram using the function createVoronoiGraph.
	//	II. It extracts the critical points, which show the border between two segments. This part takes these steps:
	//		1. Extract node-points of the Voronoi-Diagram, which have at least 3 neighbors.
	//		2. Reduce the leave-nodes (Point on graph with only one neighbor) of the graph until the reduction
	//		   hits a node-Point. This is done to reduce the lines along the real voronoi-graph, coming from the discretisation
	//		   of the contour.
	//		3. Find the critical points in the reduced graph by searching in a specified neighborhood for a local minimum
	//		   in distance to the nearest black pixel. The size of the epsilon-neighborhood is dynamic and goes larger
	//		   in small areas, so they are split into lesser regions.
	//	III. It gets the critical lines, which go from the critical point to its two nearest black pixels and separate the
	//		 regions from each other. This part does following steps:
	//			1. Get the discretized contours of the map and the holes, because these are the possible candidates for
	//			   basis-points.
	//			2. Find the basis-points for each critical-point by finding the two nearest neighbors of the vector from 1.
	//			   Also it saves the angle between the two vectors pointing from the critical-point to its two basis-points.
	//			3. Some critical-lines are too close to each other, so the next part eliminates some of them. For this the
	//			   algorithm checks, which critical points are too close to each other. Then it compares the angles of these
	//			   points, which were calculated in 3., and takes the one with the larger angle, because smaller angles
	//			   (like 90 degree) are more likely to be at edges of the map or are too close to the borders. If they have
	//			   the same angle, the point which comes first in the critical-point-vector is chosen (took good results for
	//			   me, but is only subjective).
	//			4. Draw the critical lines, selected by 3. in the map with color 0.
	//	IV. It finds the segments, which are seperated by the critical lines of III. and fills them with a random colour that
	//		hasn't been already used yet. For this it:
	//			1. It erodes the map with critical lines, so small gaps are closed, and finds the contours of the segments.
	//			   Only contours that are large/small enough are chosen to be drawn.
	//			2. It draws the contours from 1. in a map with a random colour. Contours that belong to holes are not drawn
	//			   into the map.
	//			3. Spread the colour-regions to the last white Pixels, using the watershed-region-spreading function.

	//*********************I. Calculate and draw the Voronoi-Diagram in the given map*****************

	voronoi_map = map_to_be_labeled.clone();
	createVoronoiGraph(voronoi_map); //voronoi-map for the segmentation-algorithm

	//cv::imshow("graph", voronoi_map);
	//cv::waitKey(1);

	//***************************II. extract the possible candidates for critical Points****************************
	// 1.extract the node-points that have at least three neighbors on the voronoi diagram
	//	node-points are points on the voronoi-graph that have at least 3 neighbors
	// 2.reduce the side-lines along the voronoi-graph by checking if it has only one neighbor until a node-point is reached
	//	--> make it white
	//	repeat a large enough number of times so the graph converges
	cv::Mat pruned_voronoi_map = voronoi_map;
	std::set<cv::Point, cv_Point_comp> node_points; //variable for node point extraction
	//pruneVoronoiGraph(pruned_voronoi_map, node_points);
	voronoi_map = pruned_voronoi_map.clone();
	const geos::geom::GeometryFactory *factory = geos::geom::GeometryFactory::getDefaultInstance();
	if (floorPolygon!=NULL)
		for (int v = 0; v < voronoi_map.rows; v++)
			for (int u = 0; u < voronoi_map.cols; u++)
				if (voronoi_map.at<unsigned char>(v, u) == 127)
				{
					// this is a candidate point, but is it within the dataset boundaries?
					geos::geom::Point *point = factory->createPoint(geos::geom::Coordinate(u,v));
					if (!floorPolygon->contains(point))
						voronoi_map.at<unsigned char>(v, u) = 255;
				}
	cv::imshow("graph_pruned", voronoi_map);
	cv::waitKey();
	voronoi_map = pruned_voronoi_map;
}
