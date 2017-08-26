/*!
 *****************************************************************
 * \file
 *
 * \note
 * Copyright (c) 2015 \n
 * Fraunhofer Institute for Manufacturing Engineering
 * and Automation (IPA) \n\n
 *
 *****************************************************************
 *
 * \note
 * Project name: Care-O-bot
 * \note
 * ROS stack name: autopnp
 * \note
 * ROS package name: ipa_room_segmentation
 *
 * \author
 * Author: Florian Jordan
 * \author
 * Supervised by: Richard Bormann
 *
 * \date Date of creation: 08.2015
 *
 * \brief
 *
 *
 *****************************************************************
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * - Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer. \n
 * - Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution. \n
 * - Neither the name of the Fraunhofer Institute for Manufacturing
 * Engineering and Automation (IPA) nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission. \n
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License LGPL as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License LGPL for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License LGPL along with this program.
 * If not, see <http://www.gnu.org/licenses/>.
 *
 ****************************************************************/

#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <utility>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <cv_bridge/cv_bridge.h>

#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <ipa_building_msgs/MapSegmentationAction.h>

//#include <ipa_room_segmentation/RoomSegmentationConfig.h>
#include <ipa_room_segmentation/dynamic_reconfigure_client.h>
#include <ipa_room_segmentation/room_segmentation_server.h>
#include <ipa_room_segmentation/meanshift2d.h>
#include <ipa_room_segmentation/tinydir.h>

#include <boost/algorithm/string.hpp>

#define HAVE_INT64_T_64  # Prevents conflict with OpenCV typedef of int64
 #include <geos/geom/Polygon.h>
 #include <geos/geom/LinearRing.h>
 #include <geos/geom/CoordinateSequenceFactory.h>
 #include <geos/geom/GeometryFactory.h>
 #include <geos/opBuffer.h>
#undef HAVE_INT64_T_64


	double convert_pixel_to_meter_for_x_coordinate(const int pixel_valued_object_x, const float map_resolution, const cv::Point2d map_origin);

	double convert_pixel_to_meter_for_y_coordinate(int pixel_valued_object_y, const float map_resolution, const cv::Point2d map_origin);

	geos::geom::Polygon* makePolygon(const std::vector<cv::Point>& points);

std::vector<std::string> scanInputFolder(char* inputFolder){
	tinydir_dir dir;
	std::vector<std::string> map_names;
	tinydir_open(&dir, inputFolder);

	while (dir.has_next)
	{
		tinydir_file file;
		tinydir_readfile(&dir, &file);
		if (!file.is_dir && strstr(file.name,".world")!=NULL){
			std::cout << file.name << std::endl;
			map_names.push_back(file.name);
		}
		tinydir_next(&dir);
	}
	tinydir_close(&dir);
	return map_names;
}

// comparison function object
bool compareContourAreas ( std::vector<cv::Point> contour1, std::vector<cv::Point> contour2 ) {
    double i = fabs( contourArea(cv::Mat(contour1)) );
    double j = fabs( contourArea(cv::Mat(contour2)) );
    return ( i < j );
}

int main(int argc, char **argv)
{
	// map names
	std::vector< std::string > map_names = scanInputFolder(argv[1]);
	for (size_t image_index = 0; image_index<map_names.size(); ++image_index)
	{
		// import maps
		std::string image_filename = argv[1] + map_names[image_index].substr(0,map_names[image_index].find(".world")) + ".png";
		std::cout << image_filename << std::endl;
		cv::Mat src_map, thr_map, res_map, thr_map_contours;
		double fx = 0.5, fy = 0.5;
		src_map = cv::imread(image_filename.c_str(), cv::IMREAD_GRAYSCALE);
		cv::resize(src_map, res_map, cv::Size(), fx, fy, cv::INTER_LINEAR);
		cv::threshold(res_map, thr_map, 250, 255, cv::THRESH_BINARY);


  		std::vector<std::vector<cv::Point> > contours;
  		std::vector<cv::Vec4i> hierarchy;

	    // faccio diventare tutto cio che e' bianco nero, quindi tutto cio' che era grigio diventa bianco
		int threshold_value = 253;
		int max_binary_value = 255;
		cv::threshold(res_map, thr_map_contours, threshold_value, max_binary_value,cv::THRESH_BINARY_INV);
		cv::findContours(thr_map_contours, contours, hierarchy,CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0,0));
		std::sort(contours.begin(), contours.end(), compareContourAreas);
		std::vector<cv::Point> biggestContour = contours[contours.size()-1];
		std::vector<cv::Point> approx;
		double peri = cv::arcLength(biggestContour, true);
		cv::approxPolyDP(biggestContour, approx, 0.0002*peri, true);
		geos::geom::Geometry* floorPolygon = geos::operation::buffer::BufferOp::bufferOp(makePolygon(approx),0.0);
 		cv::Mat drawing = cv::Mat::zeros(thr_map_contours.size(), CV_8UC1);
  		for( int i = 0; i< contours.size(); i++ )
       		cv::drawContours( drawing, contours, i, 150, 2, 8, hierarchy, 0, cv::Point());
  		/*for( int i = 0; i< contours.size(); i++ )
     	{
			for (int j = 0; j < contours.at(i).size()-1; j++)
				cv::line(drawing,contours.at(i).at(j),contours.at(i).at(j+1),150,5);
     	}*/



  /// Show in a window
  		//cv::namedWindow( "Contours", CV_WINDOW_AUTOSIZE );
		std::cout << "Contour area " << floorPolygon->getArea() << std::endl;
  		cv::imshow( "Contours", drawing );
		cv::waitKey();

		//make non-white pixels black
		/*for (int y = 0; y < map.rows; y++)
		{
			for (int x = 0; x < map.cols; x++)
			{
				//find not reachable regions and make them black
				if (map.at<unsigned char>(y, x) < 250)
				{
					map.at<unsigned char>(y, x) = 0;
				}
				//else make it white
				else
				{
					map.at<unsigned char>(y, x) = 255;
				}
			}
		}*/
		//cv::imshow("map", map);
		//cv::waitKey();
		sensor_msgs::Image labeling;
		cv_bridge::CvImage cv_image;
	//	cv_image.header.stamp = ros::Time::now();
		cv_image.encoding = "mono8";
		cv_image.image = res_map;
		cv_image.toImageMsg(labeling);

		ipa_building_msgs::MapSegmentationGoal goal;
		goal.input_map = labeling;
		goal.map_origin.position.x = 0;
		goal.map_origin.position.y = 0;
		goal.map_resolution = 0.03/(fx*fy);
		goal.return_format_in_meter = false;
		goal.return_format_in_pixel = true;
		goal.robot_radius = 0.4;
		//ac.sendGoal(goal);
		//converting the map msg in cv format
		cv_bridge::CvImagePtr cv_ptr_obj;
		cv_ptr_obj = cv_bridge::toCvCopy(goal.input_map, sensor_msgs::image_encodings::MONO8);
		cv::Mat original_img = cv_ptr_obj->image;
		// set voronoi parameters
		double room_upper_limit_voronoi_ = 1000000;//120.0;
		std::cout << "room_segmentation/room_area_factor_upper_limit = " << room_upper_limit_voronoi_ << std::endl;
		double room_lower_limit_voronoi_ = 0.1;//1.53;
		std::cout << "room_segmentation/room_area_factor_lower_limit = " << room_lower_limit_voronoi_ << std::endl;
		int voronoi_neighborhood_index_ = 280;
		std::cout << "room_segmentation/voronoi_neighborhood_index = " << voronoi_neighborhood_index_ << std::endl;
		int max_iterations_ = 150;
		std::cout << "room_segmentation/max_iterations = " << max_iterations_ << std::endl;
		double min_critical_point_distance_factor_ = 0.1;//1.6;
		std::cout << "room_segmentation/min_critical_point_distance_factor = " << min_critical_point_distance_factor_ << std::endl;
		double max_area_for_merging_ = 2;//12.5;
		std::cout << "room_segmentation/max_area_for_merging = " << max_area_for_merging_ << std::endl;
		bool display_segmented_map_ = false;
		//set the resolution and the limits for the actual goal and the Map origin
		const float map_resolution = goal.map_resolution;
		const cv::Point2d map_origin(goal.map_origin.position.x, goal.map_origin.position.y);
		//segment the given map
		cv::Mat segmented_map;
		VoronoiSegmentation voronoi_segmentation; //voronoi segmentation method
		// apply voronoi
		std::vector<Room> rooms;
		std::vector<geos::geom::Geometry*> roomPolygons;
		voronoi_segmentation.segmentMap(original_img, segmented_map, map_resolution, room_lower_limit_voronoi_, room_upper_limit_voronoi_,
			voronoi_neighborhood_index_, max_iterations_, min_critical_point_distance_factor_, max_area_for_merging_, rooms, display_segmented_map_);
		std::cout << "Received " << rooms.size() << " rooms.\n";
		// create polygons from cv2 image
		int room_color = 255;
 		cv::Mat room_drawing;
		cv::Mat thr_room;
  		std::vector<std::vector<cv::Point> > room_contours;
  		std::vector<cv::Vec4i> room_hierarchy;
		std::map<int, size_t> label_vector_index_codebook; // maps each room label to a position in the rooms vector
		size_t vector_index = 0;
		// for each room
		for (std::vector<Room>::iterator room = rooms.begin(); room != rooms.end(); room++){
			// get its contained points
			const std::vector<cv::Point>& points = room->getMembers();
			room_drawing = cv::Mat::zeros(thr_map_contours.size(), CV_8UC1);
       		std::vector<std::vector<cv::Point> > tmp_contour;
			tmp_contour.push_back(points);
			cv::drawContours(room_drawing, tmp_contour, 0, 255, 1, 8, hierarchy, 0, cv::Point());
  			//cv::imshow( "Contours", room_drawing );
			//cv::waitKey();
			cv::findContours(room_drawing, room_contours, room_hierarchy,CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0,0));
			std::sort(room_contours.begin(), room_contours.end(), compareContourAreas);
			biggestContour = room_contours[room_contours.size()-1];
			peri = cv::arcLength(biggestContour, true);
			cv::approxPolyDP(biggestContour, approx, 0.0002*peri, true);
			geos::geom::Geometry* roomPolygon = geos::operation::buffer::BufferOp::bufferOp(makePolygon(approx),0.0);
			//geos::geom::Polygon* roomPolygon = makePolygon(approx);
			drawing = cv::Mat::zeros(thr_map_contours.size(), CV_8UC1);
  			for( int i = 0; i< room_contours.size(); i++ )
       			cv::drawContours( drawing, room_contours, i, 150, 2, 8, hierarchy, 0, cv::Point());
			// get the color of the room
			int label = segmented_map.at<int>(points.at(0));
			label_vector_index_codebook[label] = vector_index;
			vector_index++;
  		/*for( int i = 0; i< points.size()-1; i++ )
     	{
			cv::line(drawing,points.at(i),points.at(i+1),(150,150,150),5);
     	}
		cv::line(drawing, points.at(points.size()-1), points.at(0), (150,150,150),5);*/

  /// Show in a window
  		//cv::namedWindow( "Contours", CV_WINDOW_AUTOSIZE );
		std::cout << "Room area " << roomPolygon->getArea() << std::endl;
  		//cv::imshow( "Contours", drawing );
		//cv::waitKey();
			roomPolygons.push_back(roomPolygon);
		}
		std::cout << "RoomPolygons size: " << roomPolygons.size() << std::endl;
		std::cout << "Test " << roomPolygons.at(0)->getArea() << std::endl;
// TODO: bisogna cambiare il modo in cui viene popolato il label_vector_index_codebook, che deve avere come
// label sempre il colore (recuperato da segmented_map con uno qualsiasi dei member points) ma come idx
// la posizione della stanza in rooms
// get the min/max-values and the room-centers
// compute room label codebook
	std::cout << "Finished computing voronoi segmentation." << std::endl;
	std::cout << "Finished mapping labels." << std::endl;
	//min/max y/x-values vector for each room. Initialized with extreme values
	std::vector<int> min_x_value_of_the_room(label_vector_index_codebook.size(), 100000000);
	std::vector<int> max_x_value_of_the_room(label_vector_index_codebook.size(), 0);
	std::vector<int> min_y_value_of_the_room(label_vector_index_codebook.size(), 100000000);
	std::vector<int> max_y_value_of_the_room(label_vector_index_codebook.size(), 0);
	//vector of the central Point for each room, initially filled with Points out of the map
	std::vector<int> room_centers_x_values(label_vector_index_codebook.size(), -1);
	std::vector<int> room_centers_y_values(label_vector_index_codebook.size(), -1);
	//***********************Find min/max x and y coordinate and center of each found room********************
	//check y/x-value for every Pixel and make the larger/smaller value to the current value of the room
	for (int y = 0; y < segmented_map.rows; ++y)
	{
		for (int x = 0; x < segmented_map.cols; ++x)
		{
			const int label = segmented_map.at<int>(y, x);
			if (label > 0 && label < 65280) //if Pixel is white or black it is no room --> doesn't need to be checked
			{
				const int index = label_vector_index_codebook[label];
				min_x_value_of_the_room[index] = std::min(x, min_x_value_of_the_room[index]);
				max_x_value_of_the_room[index] = std::max(x, max_x_value_of_the_room[index]);
				max_y_value_of_the_room[index] = std::max(y, max_y_value_of_the_room[index]);
				min_y_value_of_the_room[index] = std::min(y, min_y_value_of_the_room[index]);
			}
		}
	}
	std::cout << "Finished assignining min/max values." << std::endl;
	//get centers for each room
//	for (size_t idx = 0; idx < room_centers_x_values.size(); ++idx)
//	{
//		if (max_x_value_of_the_room[idx] != 0 && max_y_value_of_the_room[idx] != 0 && min_x_value_of_the_room[idx] != 100000000 && min_y_value_of_the_room[idx] != 100000000)
//		{
//			room_centers_x_values[idx] = (min_x_value_of_the_room[idx] + max_x_value_of_the_room[idx]) / 2;
//			room_centers_y_values[idx] = (min_y_value_of_the_room[idx] + max_y_value_of_the_room[idx]) / 2;
//			cv::circle(segmented_map, cv::Point(room_centers_x_values[idx], room_centers_y_values[idx]), 2, cv::Scalar(200*256), CV_FILLED);
//		}
//	}
	// use distance transform and mean shift to find good room centers that are reachable by the robot
	// first check whether a robot radius shall be applied to obstacles in order to exclude room center points that are not reachable by the robot
	cv::Mat segmented_map_copy = segmented_map;
	cv::Mat connection_to_other_rooms = cv::Mat::zeros(segmented_map.rows, segmented_map.cols, CV_8UC1);	// stores for each pixel whether a path to another rooms exists for a robot of size robot_radius
	std::set< std::pair<int, int> > bordering_rooms_idx;
	std::set<int> bordering_rooms;
	if (goal.robot_radius > 0.0)
	{
		// consider robot radius for exclusion of non-reachable points
		segmented_map_copy = segmented_map.clone();
		cv::Mat map_8u, eroded_map;
		segmented_map_copy.convertTo(map_8u, CV_8UC1, 1., 0.);
		int number_of_erosions = (goal.robot_radius / goal.map_resolution);
		cv::erode(map_8u, eroded_map, cv::Mat(), cv::Point(-1, -1), number_of_erosions);
		for (int v=0; v<segmented_map_copy.rows; ++v)
			for (int u=0; u<segmented_map_copy.cols; ++u)
				if (eroded_map.at<uchar>(v,u) == 0)
					segmented_map_copy.at<int>(v,u) = 0;

		// compute connectivity to other rooms
		bool stop = false;
		while (stop == false)
		{
			stop = true;
			for (int v=1; v<segmented_map_copy.rows-1; ++v)
			{
				for (int u=1; u<segmented_map_copy.cols-1; ++u)
				{
					// skip already identified cells
					if (connection_to_other_rooms.at<uchar>(v,u) != 0)
						continue;

					// only consider cells labeled as a room
					const int label = segmented_map_copy.at<int>(v,u);
					if (label <= 0 || label >= 65280)
						continue;

					for (int dv=-1; dv<=1; ++dv)
					{
						for (int du=-1; du<=1; ++du)
						{
							if (dv==0 && du==0)
								continue;
							const int neighbor_label = segmented_map_copy.at<int>(v+dv,u+du);
							if (neighbor_label>0 && neighbor_label<65280 && (neighbor_label!=label || (neighbor_label==label && connection_to_other_rooms.at<uchar>(v+dv,u+du)==255)))
							{
								// either the room cell has a direct border to a different room or the room cell has a neighbor from the same room label with a connecting path to another room
								connection_to_other_rooms.at<uchar>(v,u) = 255;
								int first_room = label_vector_index_codebook[label];
								int second_room = label_vector_index_codebook[neighbor_label];
								bordering_rooms_idx.insert(std::pair<int,int>(first_room, second_room));
								bordering_rooms.insert(first_room);
								bordering_rooms.insert(second_room);
								stop = false;
							}
						}
					}
				}
			}
		}
	}
	for (std::set< std::pair<int,int> >::iterator it = bordering_rooms_idx.begin(); it != bordering_rooms_idx.end(); it++)
		std::cout << it->first << " - " << it->second << std::endl;
	MeanShift2D ms;
	for (std::map<int, size_t>::iterator it = label_vector_index_codebook.begin(); it != label_vector_index_codebook.end(); ++it)
	{
		int trial = 1; 	// use robot_radius to avoid room centers that are not accessible by a robot with a given radius
		if (goal.robot_radius <= 0.)
			trial = 2;

		for (; trial <= 2; ++trial)
		{
			// compute distance transform for each room
			const int label = it->first;
			int number_room_pixels = 0;
			cv::Mat room = cv::Mat::zeros(segmented_map_copy.rows, segmented_map_copy.cols, CV_8UC1);
			for (int v = 0; v < segmented_map_copy.rows; ++v)
				for (int u = 0; u < segmented_map_copy.cols; ++u)
					if (segmented_map_copy.at<int>(v, u) == label && (trial==2 || connection_to_other_rooms.at<uchar>(v,u)==255))
					{
						room.at<uchar>(v, u) = 255;
						++number_room_pixels;
					}
			if (number_room_pixels == 0)
				continue;
			cv::Mat distance_map; //variable for the distance-transformed map, type: CV_32FC1
			cv::distanceTransform(room, distance_map, CV_DIST_L2, 5);
			// find point set with largest distance to obstacles
			double min_val = 0., max_val = 0.;
			cv::minMaxLoc(distance_map, &min_val, &max_val);
			std::vector<cv::Vec2d> room_cells;
			for (int v = 0; v < distance_map.rows; ++v)
				for (int u = 0; u < distance_map.cols; ++u)
					if (distance_map.at<float>(v, u) > max_val * 0.95f)
						room_cells.push_back(cv::Vec2d(u, v));
			if (room_cells.size()==0)
				continue;
			// use meanshift to find the modes in that set
			cv::Vec2d room_center = ms.findRoomCenter(room, room_cells, map_resolution);
			const int index = it->second;
			room_centers_x_values[index] = room_center[0];
			room_centers_y_values[index] = room_center[1];

			if (room_cells.size() > 0)
				break;
		}
	}

	cv::Mat indexed_map = segmented_map.clone();
	for (int y = 0; y < segmented_map.rows; ++y)
	{
		for (int x = 0; x < segmented_map.cols; ++x)
		{
			const int label = segmented_map.at<int>(y,x);
			if (label > 0 && label < 65280)
				indexed_map.at<int>(y,x) = label_vector_index_codebook[label]+1;//start value from 1 --> 0 is reserved for obstacles
		}
	}
	std::cout << "Finished assigning centers." << std::endl;
	std::cout << "Centers: " << room_centers_x_values.size() << std::endl;
	std::cout << "Rooms: " << rooms.size() << std::endl;
	std::cout << "Polygons: " << roomPolygons.size() << std::endl;

	if (true)
	{
		// colorize the segmented map with the indices of the room_center vector
		cv::Mat color_segmented_map = indexed_map.clone();
		color_segmented_map.convertTo(color_segmented_map, CV_8U);
		cv::cvtColor(color_segmented_map, color_segmented_map, CV_GRAY2BGR);
		for(size_t i = 0; i < room_centers_x_values.size(); ++i)
		{
			//choose random color for each room
			cv::Vec3b color((rand() % 250) + 1, (rand() % 250) + 1, (rand() % 250) + 1);
			std::set<int>::iterator it = bordering_rooms.find(i);

			std::cout << "FloorTest: " << floorPolygon->getArea() << std::endl;
			std::cout << "RoomTest: " << roomPolygons.at(i)->getArea() << std::endl;
			if (!floorPolygon->intersects(roomPolygons.at(i)) || (floorPolygon->intersection(roomPolygons.at(i))==NULL) || (floorPolygon->intersection(roomPolygons.at(i))!=NULL && floorPolygon->intersection(roomPolygons.at(i))->getArea() < roomPolygons.at(i)->getArea()/5)){
				color = cv::Vec3b(255,255,255);
				std::cout << "OUT!!!" << std::endl;
			}
			for(size_t v = 0; v < indexed_map.rows; ++v)
				for(size_t u = 0; u < indexed_map.cols; ++u)
					if(indexed_map.at<int>(v,u) == i+1)
						color_segmented_map.at<cv::Vec3b>(v,u) = color;
		}
//		cv::Mat disp = segmented_map.clone();
		for (size_t index = 0; index < room_centers_x_values.size(); ++index)
			cv::circle(color_segmented_map, cv::Point(room_centers_x_values[index], room_centers_y_values[index]), 2, cv::Scalar(256), CV_FILLED);
		cv::imshow("segmentation", color_segmented_map);
		cv::waitKey();
	}
	}

	//exit
	return 0;
}




	geos::geom::Polygon* makePolygon(const std::vector<cv::Point>& points){
		const geos::geom::GeometryFactory *factory = geos::geom::GeometryFactory::getDefaultInstance();
		std::cout << "Creating polygon" << std::endl;
		if (factory->getPrecisionModel()==NULL)
			std::cout << "PROBLEM!" << std::endl;
		else
			std::cout << "Tutto ok" << std::endl;
		geos::geom::CoordinateSequence* temp = factory->getCoordinateSequenceFactory()->create((std::size_t) 0, 0);
		for (int c = 0; c < points.size(); c++){
			temp->add(geos::geom::Coordinate(points.at(c).x, points.at(c).y));
			std::cout << "Added " << points.at(c).x << " " << points.at(c).y << std::endl;
		}
		temp->add(geos::geom::Coordinate(points.at(0).x, points.at(0).y));
		std::cout << "Added " << points.at(0).x << " " << points.at(0).y << std::endl;
		geos::geom::LinearRing *shell = factory->createLinearRing(temp);
		return factory->createPolygon(shell, NULL);
	}

	geos::geom::Polygon* MakeBox(double xmin, double ymin, double xmax, double ymax){
  geos::geom::GeometryFactory factory;
  geos::geom::CoordinateSequence* temp = factory.getCoordinateSequenceFactory()->create((std::size_t) 0, 0);

  temp->add(geos::geom::Coordinate(xmin, ymin));
  temp->add(geos::geom::Coordinate(xmin, ymax));
  temp->add(geos::geom::Coordinate(xmax, ymax));
  temp->add(geos::geom::Coordinate(xmax, ymin));
  //Must close the linear ring or we will get an error:
  //"Points of LinearRing do not form a closed linestring"
  temp->add(geos::geom::Coordinate(xmin, ymin));

  geos::geom::LinearRing *shell=factory.createLinearRing(temp);

  //NULL in this case could instead be a collection of one or more holes
  //in the interior of the polygon
  return factory.createPolygon(shell,NULL);
}
	//bool are_rooms_connected()

	double convert_pixel_to_meter_for_x_coordinate(const int pixel_valued_object_x, const float map_resolution, const cv::Point2d map_origin)
	{
		double meter_value_obj_x = (pixel_valued_object_x * map_resolution) + map_origin.x;
		return meter_value_obj_x;
	}
	//converter-> Pixel to meter for Y coordinate
	double convert_pixel_to_meter_for_y_coordinate(int pixel_valued_object_y, const float map_resolution, const cv::Point2d map_origin)
	{
		double meter_value_obj_y = (pixel_valued_object_y * map_resolution) + map_origin.y;
		return meter_value_obj_y;
	}
