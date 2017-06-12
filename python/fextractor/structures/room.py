'''
This class defines all the relevant parameters that we'd like to analyse for each room.
'''

from shapely.geometry import Polygon
import math
from structures import wall

class Room():
	room_count = 0
	def __init__(self, roomPolygon, scaling_factor):
		# dummy room identifier
		self.room_id = self.assignId()
		# scaling factor (1 pixel = n meters)
		self.scaling_factor = scaling_factor
		# area in square meters
		self.area = roomPolygon.area * math.pow(scaling_factor,2)
		# perimeter in meters
		self.perimeter = roomPolygon.length * scaling_factor
		# to extract the walls, we need to cycle through the individual lines of the
		# polygon's exterior border
		coords_list = list(roomPolygon.exterior.coords)
		# number of walls, as estimated by the polygon identified by the layout extractor
		self.n_walls = len(coords_list)-1
		# list of all walls
		self.walls = []
		coords_lengths = []
		for i in range(0,self.n_walls):
			x1 = coords_list[i][0]
			y1 = coords_list[i][1]
			x2 = coords_list[i+1][0]
			y2 = coords_list[i+1][1]
			dx = x2-x1
			dy = y2-y1
			length = math.sqrt(dx**2+dy**2)*scaling_factor
			coords_lengths.append(length)
			# add identified wall to walls list
			self.walls.append(wall.Wall(x1,y1,x2,y2,length))
		# identify shortest and longest wall to estimate eccentricity (1.0 means square)
		shortest_wall = min(coords_lengths)
		longest_wall = max(coords_lengths)
		# estimated eccentricity, i.e. ratio between the longest and the shortest wall
		self.wall_ratio = longest_wall/shortest_wall

	def assignId(self):
		room_id = Room.room_count
		Room.room_count += 1
		return room_id


	''' Debug method to ordinately list all the room features '''
	def printFeatures(self):
		print "Features of room #"+str(self.room_id)+":"
		print "  Area\t\t\t "+str(self.area) + " m^2"
		print "  Perimeter\t\t: "+str(self.perimeter)+ " m"
		print "  Number of walls\t: "+str(self.n_walls)
		print "  Wall ratio\t\t: "+str(self.wall_ratio)
		print "  Walls:"
		for i in range(0,len(self.walls)):
			print "    Wall #"+str(i+1)+": "+str(self.walls[i].length)+" m"




