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
#include <utility>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <ipa_room_segmentation/tinydir.h>
#include <ipa_room_segmentation/abstract_voronoi_segmentation.h>

#define HAVE_INT64_T_64  # Prevents conflict with OpenCV typedef of int64
 #include <geos/geom/Polygon.h>
 #include <geos/geom/Point.h>
 #include <geos/geom/LinearRing.h>
 #include <geos/geom/CoordinateSequenceFactory.h>
 #include <geos/geom/GeometryFactory.h>
 #include <geos/opBuffer.h>
#undef HAVE_INT64_T_64
#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

// prototypes
geos::geom::Polygon* makePolygon(const std::vector<cv::Point>& points);
std::vector<std::string> scanInputFolder(char* inputFolder);
bool compareContourAreas (std::vector<cv::Point> contour1, std::vector<cv::Point> contour2);

int main(int argc, char **argv)
{
	// map names
	std::vector< std::string > map_names = scanInputFolder(argv[1]);
	bool plotMap = (strcmp(argv[3],"true")==0?true:false);
	for (size_t image_index = 0; image_index<map_names.size(); ++image_index)
	{
		// define input and output filenames
		std::string image_filename = argv[1] + map_names[image_index].substr(0,map_names[image_index].find(".world")) + ".png";
		std::string output_filename = argv[2] + map_names[image_index].substr(0,map_names[image_index].find(".world")) + "_voronoi.png";
		std::string noisy_output_filename = argv[2] + map_names[image_index].substr(0,map_names[image_index].find(".world")) + "_voronoi_noise.png";
		std::cout << image_filename << std::endl;
		// load the image and perform resizing (if enabled) and thresholding
		cv::Mat src_map, thr_map, res_map, thr_map_contours;
		double fx = 1.0, fy = 1.0;
		src_map = cv::imread(image_filename.c_str(), cv::IMREAD_GRAYSCALE);
		cv::resize(src_map, res_map, cv::Size(), fx, fy, cv::INTER_LINEAR);
		cv::threshold(res_map, thr_map, 250, 255, cv::THRESH_BINARY);
		// find contours to identify the floor polygon
  		std::vector<std::vector<cv::Point> > contours;
  		std::vector<cv::Vec4i> hierarchy;
		int threshold_value = 253;
		int max_binary_value = 255;
		cv::threshold(res_map, thr_map_contours, threshold_value, max_binary_value,cv::THRESH_BINARY_INV);
		cv::findContours(thr_map_contours, contours, hierarchy,CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, cv::Point(0,0));
		// the biggest contour is the contour of the floor polygon
		std::sort(contours.begin(), contours.end(), compareContourAreas);
		std::vector<cv::Point> biggestContour = contours[contours.size()-1];
		// needs approximation to be turned into a polygon
		std::vector<cv::Point> approx;
		double peri = cv::arcLength(biggestContour, true);
		cv::approxPolyDP(biggestContour, approx, 0.0002*peri, true);
		geos::geom::Geometry* floorPolygon = geos::operation::buffer::BufferOp::bufferOp(makePolygon(approx),0.0);
		// apply voronoi
		AbstractVoronoiSegmentation abs_voronoi;
		cv::Mat voronoi_map = res_map;
		// build the entire voronoi graph
		abs_voronoi.createVoronoiGraph(voronoi_map);
		std::set<cv::Point, cv_Point_comp> node_points;
		// perform leaves pruning
		abs_voronoi.pruneVoronoiGraph(voronoi_map, node_points);
		// remove the portion of the graph that is outside the floor polygon
		const geos::geom::GeometryFactory *factory = geos::geom::GeometryFactory::getDefaultInstance();
		int npixels = 0;
		if (floorPolygon!=NULL)
			for (int v = 0; v < voronoi_map.rows; v++)
				for (int u = 0; u < voronoi_map.cols; u++)
					if (voronoi_map.at<unsigned char>(v, u) == 127)
					{
						// this is a candidate point, but is it within the dataset boundaries?
						geos::geom::Point *point = factory->createPoint(geos::geom::Coordinate(u,v));
						if (!floorPolygon->contains(point))
							voronoi_map.at<unsigned char>(v, u) = 255;
						else{
							voronoi_map.at<unsigned char>(v, u) = 0;
							npixels += 1;
						}
					}
					// simultaneously, remove the dataset boundaries to leave only the graph
					else if (voronoi_map.at<unsigned char>(v, u) == 0 && !plotMap)
						voronoi_map.at<unsigned char>(v, u) = 255;
		cv::imwrite(output_filename, voronoi_map);
		/* if we want to also try to add some random noise, uncomment this */
		/* voronoi_map = res_map;
		int sizeX = voronoi_map.size().width;
		int sizeY = voronoi_map.size().height;
  		int numPoints = 10 + sizeX*sizeY*0.0005;
  		for (int frame=0; frame<2; frame++) {
   			for (int i=0; i<numPoints; i++) {
      			int x = 2+rand()/(double)RAND_MAX*(sizeX-4);
      			int y = 2+rand()/(double)RAND_MAX*(sizeY-4);
				voronoi_map.at<unsigned char>(y,x) = 0;
    		}
		}
		std::cout << "Ready to compute noisy voronoi." << std::endl;
		abs_voronoi.createVoronoiGraph(voronoi_map);
		abs_voronoi.pruneVoronoiGraph(voronoi_map, node_points);
		npixels = 0;
		if (floorPolygon!=NULL)
			for (int v = 0; v < voronoi_map.rows; v++)
				for (int u = 0; u < voronoi_map.cols; u++)
					if (voronoi_map.at<unsigned char>(v, u) == 127)
					{
						geos::geom::Point *point = factory->createPoint(geos::geom::Coordinate(u,v));
						if (!floorPolygon->contains(point))
							voronoi_map.at<unsigned char>(v, u) = 255;
						else{
							voronoi_map.at<unsigned char>(v, u) = 0;
							npixels += 1;
						}
					}
					else if (voronoi_map.at<unsigned char>(v, u) == 0 && !plotMap)
						voronoi_map.at<unsigned char>(v, u) = 255;
		cv::imwrite(noisy_output_filename, voronoi_map);*/
	}
	return 0;
}

// comparison function object
bool compareContourAreas ( std::vector<cv::Point> contour1, std::vector<cv::Point> contour2 ) {
    double i = fabs( contourArea(cv::Mat(contour1)) );
    double j = fabs( contourArea(cv::Mat(contour2)) );
    return ( i < j );
}

std::vector<std::string> scanInputFolder(char* inputFolder){
	tinydir_dir dir;
	std::vector<std::string> map_names;
	tinydir_open(&dir, inputFolder);

	while (dir.has_next)
	{
		tinydir_file file;
		tinydir_readfile(&dir, &file);
		if (!file.is_dir && strstr(file.name,".world")!=NULL){
			map_names.push_back(file.name);
		}
		tinydir_next(&dir);
	}
	tinydir_close(&dir);
	return map_names;
}

geos::geom::Polygon* makePolygon(const std::vector<cv::Point>& points){
	const geos::geom::GeometryFactory *factory = geos::geom::GeometryFactory::getDefaultInstance();
	geos::geom::CoordinateSequence* temp = factory->getCoordinateSequenceFactory()->create((std::size_t) 0, 0);
	for (int c = 0; c < points.size(); c++)
		temp->add(geos::geom::Coordinate(points.at(c).x, points.at(c).y));
	temp->add(geos::geom::Coordinate(points.at(0).x, points.at(0).y));
	geos::geom::LinearRing *shell = factory->createLinearRing(temp);
	return factory->createPolygon(shell, NULL);
}
