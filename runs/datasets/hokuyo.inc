define hokuyolaser ranger
(
	sensor
	(
		# laser-specific properties
		range [ 0.0  80.0] # maximum range, actual detection up to 30m is set inside launch file via maxURange
		fov 270.0
		samples 540
	)

	# generic model properties
	color "blue"
	size [ 0.07 0.07 0.05 ] # dimensions from LMS200 data sheet
)




