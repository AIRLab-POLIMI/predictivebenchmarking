'''
This class defines the properties that characterise a room's wall.
'''

from shapely.geometry import Polygon
import math

class Wall():
	def __init__(self, x1, y1, x2, y2, length):
		# extremes of the walls
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		# length of the wall
		self.length = length
