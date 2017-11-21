#include <vector>
#include <math.h>
#include <string>
#include <ros/ros.h>
#include "robocom/EuleroOdometry.h"
#include "robocom/Odometry.h"

void EuleroOdometry::integrate(const vector<double>& velocity, double dt) {
	vector<double> variation(3,0);
    calculateVariation(&variation, *position, velocity);
    for(int i=0;i<3;i++)
        (*position)[i] += variation[i] * dt;    		//sums variation
}
