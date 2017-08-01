''' Dataset
This is the main class that holds all the information related to a certain dataset (i.e., a certain world file).
In particular, it holds:
- file information, i.e. file name
- list of executed runs
- average performance statistics as evaluated by the metricEvaluator
- geometrical information, i.e. number of rooms, area, perimeter...
- topological informoation, i.e. how rooms are connected together, ... '''

import copy

class Dataset():
	def __init__(self, name, runs, perfStats):
		self._name = name
		self._runs = runs
		self._perfStats = perfStats
		self._geometry = None
		self._topology = None

	@property
	def name(self):
		""" Returns the dataset name. """
		return self._name

	@property
	def runs(self):
		""" Returns a copy of the list of executed runs. """
		return copy.copy(self._runs)

	@property
	def perfStats(self):
		""" Returns a copy of the object holding the performance stats of the dataset. """
		return copy.copy(self._perfStats)

	@perfStats.setter
	def perfStats(self,perfStats):
		self._perfStats = perfStats

	@property
	def geometry(self):
		""" Returns a copy of the object holding the geometrical properties of the dataset. """
		return copy.copy(self._geometry)

	@geometry.setter
	def geometry(self, value):
		self._geometry = value

	@property
	def topology(self):
		""" Returns a copy of the object holding the topological properties of the dataset. """
		return copy.copy(self._topology)
		
	def __repr__(self):
		return "Printing dataset information. \n"+\
		"Name: "+self.name+"\n"+\
		"Performance data: \n"+\
		str(self.perfStats)+"\n"+\
		"Geometry: \n"+str(self.geometry)+"\n"