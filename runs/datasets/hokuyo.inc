define hokuyolaser ranger
(
	sensor
	(
		# laser-specific properties
		# factory settings for LMS100
		range [ 0.5  20.0 ]
		fov 270.0
		samples 540
        # for LMS200: fov 180, range 0-30m, samples 180 (1deg resolution)
	)

	# generic model properties
	color "blue"
	size [ 0.07 0.07 0.05 ] # dimensions from LMS200 data sheet
)




