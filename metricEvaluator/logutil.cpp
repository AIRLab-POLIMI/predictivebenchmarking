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

#include "logutil.h"

#include <sstream>
using namespace std;

timepos parseRobotLaser(const std::string& s)
{
  string token;
  stringstream sin(s);
  timepos tp;
  int num_val = 0;

  sin >> token; // skip tag
  // skip laser params
  for (int i = 0; i < 7; ++i)
    sin >> token;
  // skip ranges
  sin >> num_val;
  for (int i = 0; i < num_val; ++i)
    sin >> token;
  // skip remission
  sin >> num_val;
  for (int i = 0; i < num_val; ++i)
    sin >> token;
  // skip laser pose
  for (int i = 0; i < 3; ++i)
    sin >> token;
  // read robot pose
  sin >> tp.pos.x >> tp.pos.y >> tp.pos.theta;
  // skip stuff
  for (int i = 0; i < 5; ++i)
    sin >> token;
  sin >> tp.timestamp;

  return tp;
}

timepos parseFLaser(const std::string& s)
{
  string token;
  stringstream sin(s);
  timepos tp;
  int num_val = 0;

  sin >> token; // skip tag
  // skip ranges
  sin >> num_val;
  for (int i = 0; i < num_val; ++i)
    sin >> token;
  // skip laser pose
  for (int i = 0; i < 3; ++i)
    sin >> token;
  // read robot pose
  sin >> tp.pos.x >> tp.pos.y >> tp.pos.theta;
  sin >> tp.timestamp;

  return tp;
}

timepos parseOdom(const std::string& s)
{
  string token;
  stringstream sin(s);
  timepos tp;

  sin >> token; // skip tag
  // read robot pose
  sin >> tp.pos.x >> tp.pos.y >> tp.pos.theta;
  // skip stuff
  for (int i = 0; i < 3; ++i)
    sin >> token;
  sin >> tp.timestamp;

  return tp;
}
