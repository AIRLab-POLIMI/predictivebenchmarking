define hokuyolaser ranger
(
	sensor
	(
		# laser-specific properties
		# factory settings for LMS200
		range [ 0  30.0 ]
		fov 180.0
		samples 180
        # for LMS100: fov 270, range 0-20m, samples 270 (0.5deg resolution)
	)

	# generic model properties
	color "blue"
	size [ 0.07 0.07 0.05 ] # dimensions from LMS200 data sheet
)




