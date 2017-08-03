''' Geometry
Auxiliary class holding the geometrical properties of a dataset. '''

import copy
import math
from shapely.ops import cascaded_union
from shapely.geometry import Polygon, MultiPolygon
from wall import Wall

class Geometry():
	def __init__(self, rooms, boundingPolygon, scalingFactor):
		self._rooms = rooms
		self._shape = PolygonProperties(boundingPolygon, scalingFactor)
		self._boundingBox = PolygonProperties(self._buildBoundingBox(boundingPolygon), scalingFactor)

	def _buildBoundingBox(self, polygon):
		minX = polygon.bounds[0]
		minY = polygon.bounds[1]
		maxX = polygon.bounds[2]
		maxY = polygon.bounds[3]
		return Polygon([(minX, minY), (minX, maxY), (maxX, maxY), (maxX, minY)])

	@property
	def rooms(self):
		""" Returns the set of rooms in the dataset. """
		return self._rooms

	@property
	def shape(self):
		""" Returns a container for the geometrical properties of the dataset polygon.
		Note that the room polygon is contained within the bounding polygon. """
		return self._shape

	@property
	def boundingPolygon(self):
		""" Returns a container for the geometrical properties of the bounding polygon containing the dataset.
		Note that the bounding polygon is contained within the bounding box."""
		return self._boundingPolygon

	@property
	def boundingBox(self):
		""" Returns a container for the geometrical properties of the bounding box containing the dataset."""
		return self._boundingBox

	def __repr__(self):
		roomsRep = ""
		for r in self.rooms:
			roomsRep += str(r)
		return "Rooms: \n"+roomsRep+\
		"Shape: \n"+str(self.shape)+"\n"+\
		"Bounding box: \n"+str(self.boundingBox)


class PolygonProperties():
	def __init__(self, polygon, scalingFactor):
		self._polygon = polygon
		self._scalingFactor = scalingFactor
		self._perimeter = polygon.length * scalingFactor
		self._area = polygon.area * math.pow(scalingFactor,2)
		self._setWalls()

	def _setWalls(self):
		# to extract the walls, we need to cycle through the individual lines of the
		# polygon's exterior border
		coords = list(self.polygon.exterior.coords)
		# number of walls, as estimated by the polygon identified by the layout extractor
		self._numWalls = len(coords)-1
		# list of all walls
		self._walls = []
		coordsLengths = []
		for i in range(0,self._numWalls):
			x1 = coords[i][0]
			y1 = coords[i][1]
			x2 = coords[i+1][0]
			y2 = coords[i+1][1]
			dx = x2-x1
			dy = y2-y1
			length = math.sqrt(dx**2+dy**2)*self.scalingFactor
			coordsLengths.append(length)
			# add identified wall to walls list
			self._walls.append(Wall(x1,y1,x2,y2,length))
		# identify shortest and longest wall to estimate eccentricity (1.0 means square)
		# TODO: sometimes the layout extraction tool "sees" a zero-length fake wall
		# and breaks everything. This is a safety check to avoid that situation.
		shortestWall = min(filter(lambda x : x >= 0.05, coordsLengths))
		longestWall = max(coordsLengths)
		# estimated eccentricity, i.e. ratio between the longest and the shortest wall
		self._wallRatio = longestWall/shortestWall

	@property
	def numWalls(self):
		""" Returns the number of walls of the polygon. """
		return self._numWalls

	@property
	def walls(self):
		""" Returns the list of walls of the polygon. """
		return self._walls

	@property
	def wallRatio(self):
		""" Returns the ratio between the longest and the shortest wall of the polygon. """
		return self._wallRatio

	@property
	def polygon(self):
		""" Returns the actual shapely polygon. """
		return self._polygon

	@property
	def scalingFactor(self):
		""" Returns the length scaling factor as 1 pixel : n meters. """
		return self._scalingFactor

	@property
	def perimeter(self):
		""" Returns the perimeter of the polygon in meters. """
		return self._perimeter

	@property
	def area(self):
		""" Returns the area of the polygon in square meters. """
		return self._area

	def __repr__(self):
		""" Ordinately list all the polygon features """
		wallStr = ""
		for i in range(0,len(self.walls)):
			wallStr += "    Wall #"+str(i+1)+": "+str(self.walls[i].length)+" m"+"\n"
		return "  Area\t\t\t: "+str(self.area) + " m^2"+"\n"+\
		"  Perimeter\t\t: "+str(self.perimeter)+ " m"+"\n"+\
		"  Number of walls\t: "+str(self.numWalls)+"\n"+\
		"  Wall ratio\t\t: "+str(self.wallRatio)+"\n"+\
		"  Walls:"+"\n"+wallStr