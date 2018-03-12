''' Run
Auxiliary class that holds all the information related to a specific run of a certain dataset (i.e., a
certain world file).
In particular, for both the transactional and rotational errors, it holds the necessary statistics (mean,
standard deviation, min, max, number of samples) of the run, as computed by the metricEvaluator. '''

import copy

class Run():
	def __init__(self, tstats, rstats, totalTime=0, totalLength=0, totalRot=0):
		self._transStats = tstats
		self._rotStats = rstats
		self._totalTime = totalTime
		self._totalLength = totalLength
		self._totalRot = totalRot

	@property
	def transStats(self):
		""" Returns a copy of the object holding the transational error statistics of the run. """
		return copy.copy(self._transStats)

	@property
	def rotStats(self):
		""" Returns a copy of the object holding the rotational error statistics of the dataset. """
		return copy.copy(self._rotStats)

	@property
	def totalTime(self):
		""" Returns the total time that was required to complete the run. """
		return self._totalTime

	@property 
	def totalLength(self):
		""" Returns the total length travelled by the robot during the run. """
		return self._totalLength

	@property 
	def totalRot(self):
		""" Returns the total rotation performed by the robot during the run. """
		return self._totalRot

	def __repr__(self):
		return "Printing run stats:"+"\n"+ \
		"Transactional error stats: "+str(self._transStats)+ \
		"Rotational error stats: "+str(self._rotStats)+ \
		"Total time: "+str(self._totalTime)+ "\n"+\
		"Total length: "+str(self._totalLength)+ "\n"
