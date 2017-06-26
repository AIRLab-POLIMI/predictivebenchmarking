include "hokuyo.inc"

define pioneer3at position
(
	color "red"          # Default color.
	drive "diff"         # Differential steering model.
	gui_nose 1           # Draw a nose on the robot so we can see which way it points
	obstacle_return 1    # Can hit things.
	laser_return 1	     # reflects sonar beams


	# alternative odometric localization with simple error model
	localization "odom"                 # Change to "gps" to have impossibly perfect, global odometry
	odom_error [ 0.01 0.01 0.02 0 ]      # Odometry error or slip in X, Y and Theta (Uniform random distribution)
	#localization "gps"

	# four DOF kinematics limits
	# [ xmin xmax ymin ymax zmin zmax amin amax ]
	velocity_bounds     [-0.7 0.7 0 0 0 0 -70.0 70.0 ]
	acceleration_bounds [-2.5 2.5 0 0 0 0 -70.0 70.0 ]

	# Actual size
	size [0.25 0.25 0.4]

	# The pioneer's center of rotation is offset from its center of area
	origin [0 0 0 0]

	# Estimated mass in KG
	mass 30.0

	# Body shape:
#	block
#	(
#		points 4
#		point[0] [-0.125 -0.125]
#		point[1] [-0.125 0.125]
#		point[2] [0.125 0.125]
#		point[3] [0.125 -0.125]
#		z [0 1]
#	)

	hokuyolaser( pose [0.0 0 -0.2 0 ])
)


