#include <vector>
#include <string>
#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <nav_msgs/Path.h>

#include "robocom/PathPublisher.h"

using namespace std;

class PathNode {
public:
	PathNode(ros::NodeHandle& nh, double dt, vector<string> tfPosTargetFrames, vector<string> tfPosSourceFrames, vector<string> pathHeaderFrameIds, vector<string> pathTopics)
    : nh(nh), rate(0) {
        
        //allocate pathPublishers
        pathPublishers = vector<PathPublisher*>();
        for(int i=0; i<tfPosTargetFrames.size(); i++) {
            pathPublishers.push_back(new PathPublisher(nh, tfPosTargetFrames[i], tfPosSourceFrames[i], pathHeaderFrameIds[i], pathTopics[i]));
        }
	    
        //allocate rate with freq 1/dt
	    rate = ros::Rate(1/dt);
	}
	
	void spin() {
		for(int i=0; i<pathPublishers.size(); i++) {
			pathPublishers[i]->getPose();
			pathPublishers[i]->publishPath();
		}
		ros::spinOnce();
     	rate.sleep();
	}
	
private:
	ros::NodeHandle nh;
	vector<PathPublisher*> pathPublishers;
    ros::Rate rate;
};

int main(int argc, char ** argv) {
    ros::init(argc, argv, "path");

	ros::NodeHandle nh("~");
	double dt;
	nh.param("period", dt, 0.01);
	if(dt <= 0) {
		dt = 0.01;
	}
    
    vector<string> tfPosTargetFrames;
    nh.getParam("tfPosTargetFrames", tfPosTargetFrames);
    vector<string> tfPosSourceFrames;
    nh.getParam("tfPosSourceFrames", tfPosSourceFrames);
    vector<string> pathHeaderFrameIds;
    nh.getParam("pathHeaderFrameIds", pathHeaderFrameIds);
    vector<string> pathTopics;
    nh.getParam("pathTopics", pathTopics);
    
    if(tfPosTargetFrames.size() == tfPosSourceFrames.size() &&
       tfPosTargetFrames.size() == pathHeaderFrameIds.size() &&
       tfPosTargetFrames.size() == pathTopics.size()) {
        
        PathNode pathNode(nh, dt, tfPosTargetFrames, tfPosSourceFrames, pathHeaderFrameIds, pathTopics);
        while(ros::ok()) {
            pathNode.spin();
        }
    } else {
        ROS_INFO("Invalid params passed");
    }
}
