#include "mocap_optitrack/mocap_datapackets.h"

#include <stdio.h>
#include <string>
#include <iostream>
#include <ros/console.h>
using namespace std;

RigidBody::RigidBody() 
  : NumberOfMarkers(0), marker(0)
{
}

RigidBody::~RigidBody()
{
  delete[] marker;
}

const geometry_msgs::PoseStamped RigidBody::get_ros_pose()
{
  geometry_msgs::PoseStamped ros_pose;
  ros_pose.header.stamp = ros::Time::now();
  // y & z axes are swapped in the Optitrack coordinate system
  ros_pose.pose.position.x = -pose.position.x;
  ros_pose.pose.position.y = pose.position.z;
  ros_pose.pose.position.z = pose.position.y;

  ros_pose.pose.orientation.x = -pose.orientation.x;
  ros_pose.pose.orientation.y = pose.orientation.z;
  ros_pose.pose.orientation.z = pose.orientation.y;
  ros_pose.pose.orientation.w = pose.orientation.w;

  return ros_pose;
}

bool RigidBody::has_data()
{
    static const char zero[sizeof(pose)] = { 0 };
    return memcmp(zero, (char*) &pose, sizeof(pose));
}

ModelDescription::ModelDescription()
  : numMarkers(0), markerNames(0)
{
}

ModelDescription::~ModelDescription()
{
  delete[] markerNames;
}

ModelFrame::ModelFrame()
  : markerSets(0), otherMarkers(0), rigidBodies(0), 
    numMarkerSets(0), numOtherMarkers(0), numRigidBodies(0),
    latency(0.0)
{
}

ModelFrame::~ModelFrame()
{
  delete[] markerSets;
  delete[] otherMarkers;
  delete[] rigidBodies;
}

MoCapDataFormat::MoCapDataFormat(const char *packet, unsigned short length) 
  : packet(packet), length(length), frameNumber(0)
{
}

MoCapDataFormat::~MoCapDataFormat()
{
}

void MoCapDataFormat::seek(size_t count)
{
  packet += count;
  length -= count;
}

void MoCapDataFormat::parse()
{
  seek(4);

  // parse frame number
  read_and_seek(frameNumber);

  // count number of packetsets
  read_and_seek(model.numMarkerSets);
  model.markerSets = new MarkerSet[model.numMarkerSets];
  ROS_DEBUG("Number of marker sets: %d\n", model.numMarkerSets);

  for (int i = 0; i < model.numMarkerSets; i++)
  {
    strcpy(model.markerSets[i].name, packet);
    seek(strlen(model.markerSets[i].name) + 1);

    ROS_DEBUG("Parsing marker set named: %s\n", model.markerSets[i].name);

    // read number of markers that belong to the model
    read_and_seek(model.markerSets[i].numMarkers);
    ROS_DEBUG("Number of markers in set: %d\n", model.markerSets[i].numMarkers);

    model.markerSets[i].markers = new Marker[model.markerSets[i].numMarkers];
    for (int k = 0; k < model.markerSets[i].numMarkers; k++)
    {
      // read marker positions
      read_and_seek(model.markerSets[i].markers[k]);
    }
  }

  // read number of 'other' markers (cf. NatNet specs)
  read_and_seek(model.numOtherMarkers);
  model.otherMarkers = new Marker[model.numOtherMarkers];
  ROS_DEBUG("Number of markers not in sets: %d\n", model.numOtherMarkers);
  for (int l = 0; l < model.numOtherMarkers; l++)
  {
    // read positions of 'other' markers
    read_and_seek(model.otherMarkers[l]);
  }

  // read number of rigid bodies of the model
  read_and_seek(model.numRigidBodies);
  ROS_DEBUG("Number of rigid bodies: %d\n", model.numRigidBodies);

  model.rigidBodies = new RigidBody[model.numRigidBodies];
  for (int m = 0; m < model.numRigidBodies; m++)
  {
    // read id, position and orientation of each rigid body
    read_and_seek(model.rigidBodies[m].ID);
    read_and_seek(model.rigidBodies[m].pose);

    // get number of markers per rigid body
    read_and_seek(model.rigidBodies[m].NumberOfMarkers);
    ROS_DEBUG("Rigid body ID: %d\n", model.rigidBodies[m].ID);
    ROS_DEBUG("Number of rigid body markers: %d\n", model.rigidBodies[m].NumberOfMarkers);
    if (model.rigidBodies[m].NumberOfMarkers > 0)
    {
      model.rigidBodies[m].marker = new Marker [model.rigidBodies[m].NumberOfMarkers];
      size_t byte_count = model.rigidBodies[m].NumberOfMarkers * sizeof(Marker);
      memcpy(model.rigidBodies[m].marker, packet, byte_count);
      seek(byte_count);

      // skip marker IDs
      byte_count = model.rigidBodies[m].NumberOfMarkers * sizeof(int);
      seek(byte_count);

      // skip marker sizes
      byte_count = model.rigidBodies[m].NumberOfMarkers * sizeof(float);
//      seek(byte_count);

      float markers_size[model.rigidBodies[m].NumberOfMarkers];

      model.rigidBodies[m].NumberOfTrackedMarkers = 0;
      for (int k = 0; k < model.rigidBodies[m].NumberOfMarkers; k++)
      {
        read_and_seek(markers_size[k]);

        if(markers_size[k] > 0.0) model.rigidBodies[m].NumberOfTrackedMarkers ++;
        // TODO add also the value in array in RigidBody
      }

      ROS_DEBUG("Rigid body %d; tracked markers: %d / %d, \t pos: [%3.2f,%3.2f,%3.2f], \t ori: [%3.2f,%3.2f,%3.2f,%3.2f]", model.rigidBodies[m].ID,
          model.rigidBodies[m].NumberOfTrackedMarkers,
          model.rigidBodies[m].NumberOfMarkers,
          model.rigidBodies[m].pose.position.x,
          model.rigidBodies[m].pose.position.y,
          model.rigidBodies[m].pose.position.z,
          model.rigidBodies[m].pose.orientation.x,
          model.rigidBodies[m].pose.orientation.y,
          model.rigidBodies[m].pose.orientation.z,
          model.rigidBodies[m].pose.orientation.w);
    }

    // skip mean marker error
    seek(sizeof(float));
    seek(2);
  }

  // TODO: read skeletons
  int numSkeletons = 0;
  read_and_seek(numSkeletons);

  // get latency
  read_and_seek(model.latency);
}


