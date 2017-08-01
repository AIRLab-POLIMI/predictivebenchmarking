'''
This class defines all the relevant parameters that we'd like to analyse for each room.
'''
from geometry import PolygonProperties

class Room():
	roomCount = 0
	def __init__(self, roomPolygon, boundingBox, boundingPolygon, scalingFactor):
		# dummy room identifier
		self._roomId = self.assignId()
		self._boundingBox = boundingBox
		self._boundingPolygon = boundingPolygon
		# scaling factor (1 pixel = n meters)
		self._scalingFactor = scalingFactor
		self._shape = PolygonProperties(roomPolygon, scalingFactor)
		self._boundingBox = PolygonProperties(boundingBox, scalingFactor)
		self._boundingPolygon = PolygonProperties(boundingPolygon, scalingFactor)

	def assignId(self):
		roomId = Room.roomCount
		Room.roomCount += 1
		return roomId

	@property
	def roomId(self):
		""" Returns the progressive numerical identifier of the room. """
		return self._roomId

	@property
	def shape(self):
		""" Returns a container for the geometrical properties of the room polygon.
		Note that the room polygon is contained within the bounding polygon. """
		return self._shape

	@property
	def boundingPolygon(self):
		""" Returns a container for the geometrical properties of the bounding polygon containing the room.
		Note that the bounding polygon is contained within the bounding box."""
		return self._boundingPolygon

	@property
	def boundingBox(self):
		""" Returns a container for the geometrical properties of the bounding box containing the room."""
		return self._boundingBox


	def __repr__(self):
		""" Ordinately list all room features """
		return "Features of room #"+str(self.roomId)+":"+"\n"+\
		"Shape: \n"+str(self.shape)+"\n"+\
		"Bounding polygon: \n"+str(self.boundingPolygon)+"\n"+\
		"Bounding box: \n"+str(self.boundingBox)+"\n"
	