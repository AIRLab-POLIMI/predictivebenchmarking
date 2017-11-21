#ifndef INCLUDE_ROBOCOM_EULERO_ODOMETRY_H_
#define INCLUDE_ROBOCOM_EULERO_ODOMETRY_H_

#include <vector>
#include <math.h>
#include <string>
#include "robocom/Odometry.h"

using namespace std;

class EuleroOdometry : public Odometry{
public:
	using Odometry::Odometry;
	void integrate(const vector<double>& velocity, double dt) override;
	vector<double> getPosition();
};

#endif /* INCLUDE_ROBOCOM_EULERO_ODOMETRY_H_ */
