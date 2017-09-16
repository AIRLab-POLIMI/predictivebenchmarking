import numpy as np
import xml.etree.cElementTree as ET
from xml.etree import ElementTree
from structures import room as sr
from shapely.geometry import Polygon

def buildBoundingBoxExtremes(minX, minY, maxX, maxY):
	boundingBoxStr  = '<bounding_box>\n'
	boundingBoxStr += '<point x="'+str(minX)+'" y="'+str(minY)+'" />'+'\n'
	boundingBoxStr += '<point x="'+str(minX)+'" y="'+str(maxY)+'" />'+'\n'
	boundingBoxStr += '<point x="'+str(maxX)+'" y="'+str(maxY)+'" />'+'\n'
	boundingBoxStr += '<point x="'+str(maxX)+'" y="'+str(minY)+'" />'+'\n'
	boundingBoxStr += '</bounding_box>'
	return boundingBoxStr

def buildDatasetExtremes(vertices):
	extremes = ""
	for v in vertices: 
		extremes += '<point x="'+str(int(v[0]))+'" y="'+str(int(v[1]))+'" />\n'
	return extremes



def crea_xml(nome_xml_segmentato, spazi, imageScale, vertices, connectedRooms):
	'''
	Creo xml delle stanze segmentate.
	'''
	#------------------CREO XML--------------------------------------------------------------------

	import uuid
	id_stanze = []
	connessi = {}
	for i,s in enumerate(spazi):
		id_stanze.append(i)
	for [r1,r2] in connectedRooms:
		if r1 not in connessi:
			connessi[r1] = []
		if r2 not in connessi:
			connessi[r2] = []
		connessi[r1].append(r2)
		connessi[r2].append(r1)

	xml = open(nome_xml_segmentato, "w")
	xml_id = uuid.uuid4()
	xml.write('<building id="'+str(xml_id)+'">\n<name>'+str(nome_xml_segmentato)+'</name>\n<scale>\n<represented_distance>\n<value>1</value>\n<um>pixel</um>\n</represented_distance>\n<real_distance>\n<value>'+str(imageScale)+'</value>\n<um>m</um>\n</real_distance>\n</scale>\n<Info>Inserire informazioni sull\'edificio</Info>\n<building_type>\n<main_type>SCHOOL</main_type>\n</building_type>\n<floor>\n')
	extremes = buildDatasetExtremes(vertices)
	xml.write('<bounding_polygon>\n'+extremes+'</bounding_polygon>\n')
	xml.write('<spaces>\n')
	for i,s in enumerate(spazi):
		#indice_gt_corrisp = indici_gt_corrispondenti_fwd[i]
		xml.write('<space id="'+str(id_stanze[i])+'">\n')	
		xml.write('<partial_room>'+str(s.parziale)+'</partial_room>\n')	
		boundingBoxStr = buildBoundingBoxExtremes(int(s.spazio.bounds[0]), int(s.spazio.bounds[1]), int(s.spazio.bounds[2]), int(s.spazio.bounds[3]))
		xml.write('<centroid>\n<point x="'+str(int(s.spazio.centroid.x))+'" y="'+str(int(s.spazio.centroid.x))+'" />\n</centroid>\n'+boundingBoxStr+'\n<bounding_polygon>\n')
		if s.spazio.boundary.type is 'MultiLineString':
			for l in s.spazio.boundary:
				b = l.coords.xy
				for n in xrange(0,len(b[0])):
					xml.write('<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n')
		
			xml.write('</bounding_polygon>\n<space_representation>\n')
			for l in s.spazio.boundary:
				b = l.coords.xy
				for n in xrange(0,len(b[0])-1):
					xml.write('<linesegment id="'+str(uuid.uuid4())+'">\n<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n<point x="'+str(int(b[0][n+1]))+'" y="'+str(int(b[1][n+1]))+'" />\n<class>WALL</class>\n<type>EXPLICIT</type>\n<features>NORMAL</features>\n</linesegment>\n')
	
		else:	
			b = s.spazio.boundary.coords.xy
			for n in xrange(0,len(b[0])):
				xml.write('<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n')

			xml.write('</bounding_polygon>\n<space_representation>\n')
			for n in xrange(0,len(b[0])-1):
				xml.write('<linesegment id="'+str(uuid.uuid4())+'">\n<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n<point x="'+str(int(b[0][n+1]))+'" y="'+str(int(b[1][n+1]))+'" />\n<class>WALL</class>\n<type>EXPLICIT</type>\n<features>NORMAL</features>\n</linesegment>\n')
		r1 = i
		if r1 in connessi:
			xml.write('<portals>\n')
			for r2 in connessi[r1]:
				xml.write('<portal>\n')
				xml.write('<linesegment>UNKNOWN</linesegment>\n')
				xml.write('<class>UNKNOWN</class>\n')
				xml.write('<type>EXPLICIT</type>\n')
				xml.write('<direction>BOTH</direction>\n')
				xml.write('<target>\n')
				if r1 < r2:
					xml.write('<id>'+str(id_stanze[r1])+'</id>\n')
					xml.write('<id>'+str(id_stanze[r2])+'</id>\n')
				else:
					xml.write('<id>'+str(id_stanze[r2])+'</id>\n')
					xml.write('<id>'+str(id_stanze[r1])+'</id>\n')
				xml.write('</target>\n')
				xml.write('<features>NORMAL</features>\n')
				xml.write('</portal>\n')
			xml.write('</portals>\n')

		xml.write('</space_representation>\n')
	
		xml.write('</space>\n')

	xml.write('</spaces>\n</floor>\n</building>')
	xml.close()
	
	return id_stanze

def extractCoordsFromPoint(point):
	return float(point.get("x")), float(point.get("y"))

def extractBoundingPolygon(boxNode):
	vertices = boxNode.findall("point")
	return Polygon([extractCoordsFromPoint(v) for v in vertices])

def loadXML(XMLFile):
	''' Loads an XML Layout File and returns the set of rooms that it describes.'''
	tree = ET.parse(XMLFile)
	# get the root node (in this case, the "building" element)	
	root = tree.getroot()
	# from here, there are a few interesting pieces of information to dump
	# get all children
	children = list(root)
	# bounding polygon
	boundingPolygonTag = root.find("floor").find("bounding_polygon")
	boundingPolygon = extractBoundingPolygon(boundingPolygonTag)
	# extract scale information as 1 pixel : n meters
	pixelScale = root.find("scale").findall(".//value")[0].text 
	meterScale = root.find("scale").findall(".//value")[1].text
	scalingFactor = float(meterScale) / float(pixelScale)	
	# extract information about rooms
	spaces = root.find("floor").find("spaces").findall("space")
	rooms = []
	connectedRooms = []
	# iterate over the rooms
	for space in spaces: 
		# we need to recreate a polygon
		# collect its walls
		roomId = space.get("id")
		walls = space.findall(".//linesegment")
		vertices = []
		for w in walls:
			if w.find("point")!=None: # if this linesegment is really a line and not just a pointer
				vertices.append(w.find("point"))
		roomPolygon = Polygon([extractCoordsFromPoint(v) for v in vertices])
		# bounding box
		roomBoundingBoxTag = space.find("./bounding_box")
		roomBoundingBox = extractBoundingPolygon(roomBoundingBoxTag)
		# bounding polygon
		roomBoundingPolygonTag = space.find("./bounding_polygon")
		roomBoundingPolygon = extractBoundingPolygon(roomBoundingPolygonTag)
		room = sr.Room(roomId, roomPolygon, roomBoundingBox, roomBoundingPolygon, scalingFactor)
		rooms.append(room)
		# list all connections
		portals = space.findall(".//portal")
		for portal in portals:
			srcId = int(portal.find("target").findall("id")[0].text)
			dstId = int(portal.find("target").findall("id")[1].text)
			if srcId < dstId: 
				connectedRooms.append([srcId,dstId])
		# print room
	return rooms, connectedRooms, boundingPolygon, scalingFactor