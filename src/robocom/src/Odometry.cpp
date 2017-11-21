#include <vector>
#include <math.h>
#include <string>
#include <ros/ros.h>
#include "robocom/RungeKutta4Odometry.h"
#include "robocom/Odometry.h"
#include "robocom/EuleroOdometry.h"

using namespace std;
Odometry:: Odometry() {
		position = new vector<double>(3,0);
		velocities = new vector<double>(3,0);
}

Odometry:: ~Odometry() {
		delete position;
		delete velocities;
}

//calculates the infinitesimal variation of the function, given the actual position and the velocity
void Odometry::calculateVariation(vector<double> *variation, const vector<double>& position, const vector<double>& velocity) {
	(*velocities)[0] = velocity[0];
	(*velocities)[1] = velocity[1];
	(*velocities)[2] = velocity[2];
    (*variation)[0] = (cos(position[2]) * velocity[0] - sin(position[2]) * velocity[1]);
    (*variation)[1] = (sin(position[2]) * velocity[0] + cos(position[2]) * velocity[1]);
    (*variation)[2] = velocity[2];
};
vector<double> Odometry::getPosition() {
	return *position;
}
vector<double> Odometry::getVelocities(){
	return *velocities;
}
