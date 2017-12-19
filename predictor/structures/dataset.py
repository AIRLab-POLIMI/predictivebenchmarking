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
		self._topologyStats = None
		self._voronoi = None
		self._voronoiStats = None
		self._voronoiCenter = None
		self._voronoiDistance = 0
		self._voronoiTopVisits = 0
		self._voronoiRotation = 0
		self._entropy = 0

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

	@topology.setter
	def topology(self, value):
		self._topology = value

	@property
	def topologyStats(self):
		return self._topologyStats

	@topologyStats.setter
	def topologyStats(self,value):
		self._topologyStats = value

	@property
	def voronoi(self):
		return copy.copy(self._voronoi)

	@voronoi.setter
	def voronoi(self, value):
		self._voronoi = value

	@property
	def voronoiStats(self):
		return self._voronoiStats

	@voronoiStats.setter
	def voronoiStats(self,value):
		self._voronoiStats = value

	@property
	def voronoiCenter(self):
		return self._voronoiCenter

	@voronoiCenter.setter
	def voronoiCenter(self, value):
		self._voronoiCenter = value
		
	@property
	def voronoiDistance(self):
		return self._voronoiDistance

	@voronoiDistance.setter
	def voronoiDistance(self, value):
		self._voronoiDistance = value

	@property
	def voronoiTopVisits(self):
		return self._voronoiTopVisits

	@voronoiTopVisits.setter
	def voronoiTopVisits(self, value):
		self._voronoiTopVisits = value

	@property
	def voronoiRotation(self):
		return self._voronoiRotation

	@voronoiRotation.setter
	def voronoiRotation(self, value):
		self._voronoiRotation = value

	@property
	def entropy(self):
		return self._entropy

	@entropy.setter
	def entropy(self, value):
		self._entropy = value

	def __repr__(self):
		return "Printing dataset information. \n"+\
		"Name: "+self.name+"\n"+\
		"Performance data: \n"+\
		str(self.perfStats)+"\n"+\
		"Geometry: \n"+str(self.geometry)+"\n"