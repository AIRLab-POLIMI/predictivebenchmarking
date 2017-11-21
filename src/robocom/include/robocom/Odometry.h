#ifndef INCLUDE_ROBOCOM_ODOMETRY_H_
#define INCLUDE_ROBOCOM_ODOMETRY_H_

#include <vector>
#include <string>

using namespace std;

class Odometry {
public:
	Odometry();
	~Odometry();
	virtual void integrate(const vector<double>& velocity, double dt) = 0;
	void calculateVariation(vector<double> *variation, const vector<double>& position, const vector<double>& velocity);
	vector<double> getPosition();
	vector<double> getVelocities();
protected:
	vector <double>*position;
	// Valerio: these are most likely needed for /odom to work correctly
	vector <double>*velocities;
};

#endif /* INCLUDE_ROBOCOM_ODOMETRY_H_ */
