/**********************************************************************
 *
 * This source code is part of metricEvaluator.
 *
 * metricEvaluator Copyright (c) 2009 Christian Dornhege, Bastian Steder, 
 *                    Rainer Kümmerle, Michael Ruhnke, Giorgio Grisetti, 
 *                    Cyrill Stachniss, and Alexander Kleiner
 *
 * metricEvaluator is licenced under the Common Creative License,
 * Attribution-NonCommercial-ShareAlike 3.0
 *
 * You are free:
 *   - to Share - to copy, distribute and transmit the work
 *   - to Remix - to adapt the work
 *
 * Under the following conditions:
 *
 *   - Attribution. You must attribute the work in the manner specified
 *     by the author or licensor (but not in any way that suggests that
 *     they endorse you or your use of the work).
 *  
 *   - Noncommercial. You may not use this work for commercial purposes.
 *  
 *   - Share Alike. If you alter, transform, or build upon this work,
 *     you may distribute the resulting work only under the same or
 *     similar license to this one.
 *
 * Any of the above conditions can be waived if you get permission
 * from the copyright holder.  Nothing in this license impairs or
 * restricts the author's moral rights.
 *
 * metricEvaluator is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied 
 * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
 **********************************************************************/

#ifndef LOGUTIL_H
#define LOGUTIL_H

#include "structs.h"

timepos parseRobotLaser(const std::string& s);
timepos parseFLaser(const std::string& s);
timepos parseOdom(const std::string& s);

#endif
