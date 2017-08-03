'''
This class defines the properties that characterise a room's wall.
'''

from shapely.geometry import Polygon
import math
from enum import Enum

class LineTypes(Enum):
	HORIZONTAL = 1
	VERTICAL = 2
	DIAGONAL = 3

class Wall():
	def __init__(self, x1, y1, x2, y2, length):
		# extremes of the walls
		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2
		# length of the wall
		self._length = length
		# in a perfect manhattan world scenario, either x or y would match
		if x1==x2: 
			self._lineType = LineTypes.VERTICAL
			self._angCoeff = float("inf")
		elif y1==y2:
			self._lineType = LineTypes.HORIZONTAL
			self._angCoeff = 0
		# otherwise we are dealing with a diagonal wall: consider the angular coefficient
		else:
			self._lineType = LineTypes.DIAGONAL
			self._angCoeff = (y2-y1)/(x2-x1)

	@property
	def firstPoint(self):
		return (self._x1,self._y1)

	@property
	def endPoint(self):
		return (self._x2,self._y2)

	@property
	def x1(self):
		return self._x1

	@property
	def x2(self):
		return self._x2

	@property
	def y1(self):
		return self._y1

	@property
	def y2(self):
		return self._y2

	@property
	def length(self):
		return self._length

	@property
	def lineType(self):
		return self._lineType

	@property
	def angCoeff(self):
		return self._angCoeff

	def __repr__(self):
		return "x1: "+str(self.x1)+" y1: "+str(self.y1)+" x2: "+str(self.x2)+" y2: "+str(self.y2)