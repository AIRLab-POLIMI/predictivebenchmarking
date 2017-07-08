/*********************************************************************
*
* Software License Agreement (BSD License)
*
*  Copyright (c) 2009, Willow Garage, Inc.
*  All rights reserved.
*
*  Redistribution and use in source and binary forms, with or without
*  modification, are permitted provided that the following conditions
*  are met:
*
*   * Redistributions of source code must retain the above copyright
*     notice, this list of conditions and the following disclaimer.
*   * Redistributions in binary form must reproduce the above
*     copyright notice, this list of conditions and the following
*     disclaimer in the documentation and/or other materials provided
*     with the distribution.
*   * Neither the name of Willow Garage, Inc. nor the names of its
*     contributors may be used to endorse or promote products derived
*     from this software without specific prior written permission.
*
*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
*  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
*  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
*  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
*  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
*  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
*  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
*  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
*  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
*  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
*  POSSIBILITY OF SUCH DAMAGE.
*
* Author: Eitan Marder-Eppstein
*********************************************************************/
#include <clear_inner_costmap/clear_inner_costmap.h>
#include <pluginlib/class_list_macros.h>
#include <costmap_2d/obstacle_layer.h>

PLUGINLIB_DECLARE_CLASS(clear_inner_costmap, ClearInnerCostmap, clear_inner_costmap::ClearInnerCostmap,
    nav_core::RecoveryBehavior)

namespace clear_inner_costmap
{
  ClearInnerCostmap::ClearInnerCostmap():global_costmap_(NULL), local_costmap_(NULL), 
                                       initialized_(false){}

  ClearInnerCostmap::~ClearInnerCostmap()
  {
  }

  void ClearInnerCostmap::initialize (std::string n, tf::TransformListener* tf,
      costmap_2d::Costmap2DROS* global_costmap,
      costmap_2d::Costmap2DROS* local_costmap)
  {
    global_costmap_ = global_costmap;
    local_costmap_ = local_costmap;

    ros::NodeHandle private_nh_("~/" + n);
    private_nh_.param("clearing_distance", clearing_distance_, 1.0);

    initialized_ = true;
  }

  void ClearInnerCostmap::runBehavior()
  {
    if(!initialized_)
    {
      ROS_ERROR("This recovery behavior has not been initialized, doing nothing.");
      return;
    }
    ROS_WARN("Clear inner costmap recovery behavior started.");
    ROS_WARN("Clearing inner costmap around the robot.");
    tf::Stamped<tf::Pose> global_pose, local_pose;
    global_costmap_->getRobotPose(global_pose);
    local_costmap_->getRobotPose(local_pose);

    std::vector<geometry_msgs::Point> global_poly, local_poly;
    geometry_msgs::Point pt;

    for(int i = -1; i <= 1; i+=2)
    {
      pt.x = global_pose.getOrigin().x() + i * clearing_distance_;
      pt.y = global_pose.getOrigin().y() + i * clearing_distance_;
      global_poly.push_back(pt);

      pt.x = global_pose.getOrigin().x() + i * clearing_distance_;
      pt.y = global_pose.getOrigin().y() + -1.0 * i * clearing_distance_;
      global_poly.push_back(pt);

      pt.x = local_pose.getOrigin().x() + i * clearing_distance_;
      pt.y = local_pose.getOrigin().y() + i * clearing_distance_;
      local_poly.push_back(pt);

      pt.x = local_pose.getOrigin().x() + i * clearing_distance_;
      pt.y = local_pose.getOrigin().y() + -1.0 * i * clearing_distance_;
      local_poly.push_back(pt);
    }

    //clear the desired space in the costmaps
    std::vector<boost::shared_ptr<costmap_2d::Layer> >* plugins = global_costmap_->getLayeredCostmap()->getPlugins();
    for (std::vector<boost::shared_ptr<costmap_2d::Layer> >::iterator pluginp = plugins->begin(); pluginp != plugins->end(); ++pluginp) {
            boost::shared_ptr<costmap_2d::Layer> plugin = *pluginp;
          if(plugin->getName().find("obstacles")!=std::string::npos){
            boost::shared_ptr<costmap_2d::ObstacleLayer> costmap;
            costmap = boost::static_pointer_cast<costmap_2d::ObstacleLayer>(plugin);
            costmap->setConvexPolygonCost(global_poly, costmap_2d::FREE_SPACE);
          }
    }
     
    plugins = local_costmap_->getLayeredCostmap()->getPlugins();
    for (std::vector<boost::shared_ptr<costmap_2d::Layer> >::iterator pluginp = plugins->begin(); pluginp != plugins->end(); ++pluginp) {
            boost::shared_ptr<costmap_2d::Layer> plugin = *pluginp;
          if(plugin->getName().find("obstacles")!=std::string::npos){
            boost::shared_ptr<costmap_2d::ObstacleLayer> costmap;
            costmap = boost::static_pointer_cast<costmap_2d::ObstacleLayer>(plugin);
            costmap->setConvexPolygonCost(local_poly, costmap_2d::FREE_SPACE);
          }
    } 
   //local_costmap_->resetLayers();
   //global_costmap_->resetLayers();
  }
};
