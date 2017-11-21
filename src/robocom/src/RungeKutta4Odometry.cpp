#include <vector>
#include <math.h>
#include <string>
#include <ros/ros.h>
#include "robocom/RungeKutta4Odometry.h"
#include "robocom/Odometry.h"

void RungeKutta4Odometry::integrate(const vector<double>& velocity, double dt) {
	vector<double> k1(3,0), k2(3,0), k3(3,0), k4(3,0);	//k that allow to calculate the position
	vector<double> sk2(3,0), sk3(3,0), sk4(3,0);		//variation due to k1, k2, k3
	
	calculateVariation(&k1, *position, velocity);
    //calcolo k2
    for(int i=0; i<3; i++)
        sk2[i] = (*position)[i] + 1/2 * k1[i] * dt;
    
    calculateVariation(&k2, sk2, velocity);
    
    //calcolo k3
    for(int i=0; i<3; i++)
        sk3[i] = (*position)[i] + 1/2 * k3[i] * dt;
    
    calculateVariation(&k3, sk3, velocity);
    
    //calcolo k4
    for(int i=0; i<3; i++)
    	sk4[i] = (*position)[i] + 1/2 * k4[i] * dt;
        
    calculateVariation(&k4, sk4, velocity);
    
    for(int i=0; i<3; i++)
    	(*position)[i] += dt/6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]);
}
