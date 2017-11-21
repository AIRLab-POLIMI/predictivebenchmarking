#ifndef INCLUDE_ROBOCOM_PATH_PUBLISHER_H_
#define INCLUDE_ROBOCOM_PATH_PUBLISHER_H_

#include <vector>
#include <string>
#include <ros/ros.h>
#include <tf/transform_listener.h>

using namespace std;

class PathPublisher {

public:
	PathPublisher(ros::NodeHandle& nh, string tfPosTargetFrame, string tfPosSourceFrame,
					string pathHeaderFrameId, string pathTopic);
	void getPose();
	void publishPath();

private:
	ros::NodeHandle nh;
	string tfPosTargetFrame;					//target frame (first param of listener.lookupTransform)		
	string tfPosSourceFrame;					//source frame (second param of listener.lookupTransform)
	string pathHeaderFrameId;					//id of header frame to set inside msg Path
	string pathTopic;							//name of topics over publish path
    ros::Publisher pathPublisher;
    vector<geometry_msgs::PoseStamped> poses;	//poses of the path
    tf::TransformListener listener;

};

#endif /* INCLUDE_ROBOCOM_PATH_PUBLISHER_H_ */
