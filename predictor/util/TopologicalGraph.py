import networkx as nx
import cv2
import numpy as np
from random import seed, randint
from shapely.geometry import Polygon,Point

''' Outline of the algorithm.
1) Detect adjacent/bordering rooms. To do this, we enlarge the walls of each room to full-fledged rectangles 
of a proper width/height (parametric wrt the map resolution in terms of pixels-to-meters ratio); then we
check all possible pairs of walls to verify whether they intersect or not. This may also use a percentage
of intersection to discard false positives.
2) Detect doors. To do this, consider the rooms that have been found to be adjacent, take their respective
centroids and perform a floodfill; then verify whether the centroid of the other room has been colored.
N.B. This must be performed on a masked image that contains only the two rooms we are investigating,
otherwise we'd also detect indirect connections (e.g. through corridors) '''

def createGraph(imagePath,rooms,wallEnlargement):
	''' Creates a topological graph of the image. '''
	seed()
	print wallEnlargement
	# Read a grayscale image
	image = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
	# Apply threshold to convert it to binary
	th, im_th = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
	# Cycle over the rooms (type 'spazio') to enlarge the walls
	for r in rooms: 
		r.enlargeWalls(wallEnlargement)
	# now check for overlapping
	borderingRooms = []
	connectedRooms = []
	for r1_idx in range(0,len(rooms)):
		r1 = rooms[r1_idx]
		for w1 in r1.enlargedWalls:
			for r2_idx in range(r1_idx+1,len(rooms)):
				r2 = rooms[r2_idx]
				for w2 in r2.enlargedWalls:
					# if two walls are intersecting, then the two rooms are adjacent
					if w1.intersects(w2):
						if [r1_idx,r2_idx] not in borderingRooms:
							borderingRooms.append([r1_idx,r2_idx])
	# if two adjacent rooms are also connected by a door, add them to connectedRooms
	for pair in borderingRooms:
		if areRoomsConnected(im_th,rooms[pair[0]],rooms[pair[1]],wallEnlargement):
			connectedRooms.append(pair)
	# create the graph
	G=nx.Graph()
	for i,s in enumerate(rooms):
		G.add_node(i)
	G.add_edges_from(connectedRooms)
	# create a dictionary containing the nodes positions (i.e. their representative points)
	pos = {0: (rooms[0].spazio.representative_point().x,rooms[0].spazio.representative_point().y)}
	for i,s in enumerate(rooms[1:]):
		pos[i+1] = (int(s.spazio.representative_point().x),int(s.spazio.representative_point().y))
	# set the nodes positions
	for n, p in pos.iteritems():
		G.node[n]['pos'] = p
	return G,pos,connectedRooms

def getFreeRepresentativePoint(image,poly,size,maxAttempts):
	initPoint = poly.representative_point()
	reprPoint = initPoint
	count = 0
	h, w = image.shape[:2]
	while not (int(reprPoint.x)<w and int(reprPoint.y)<h and image[int(h-reprPoint.y),int(reprPoint.x)]==255 and poly.contains(reprPoint)) and count<maxAttempts: 
		dx = randint(0,size)-size/2
		dy = randint(0,size)-size/2
		reprPoint = Point(initPoint.x+dx,initPoint.y+dy)
		count += 1
	return reprPoint

def areRoomsConnected(image,r1,r2,wallEnlargement):
	''' Tests whether two adjacent rooms are also connected by a door. '''
	filling_color = 200
	h, w = image.shape[:2]
	# First, we "cut" the region of the image where the first room lies 
	ignore_mask_color = 255
	mask = np.zeros((h, w), np.uint8)
	roi_corners =[]
	for [x,y] in r1.spazio.exterior.coords:
		roi_corners.append([x,h-y])
	roi_corners = np.array([roi_corners],np.int32)
	cv2.fillPoly(mask, roi_corners, ignore_mask_color)
	masked_image_1 = cv2.bitwise_and(image, mask)
	#cv2.imshow('image',cv2.resize(masked_image_1, (0,0), fx=1.0, fy=1.0))
	#cv2.waitKey(0)
	# Then, we "cut" the region of the image where the second room lies
	mask = np.zeros((h, w), np.uint8)
	roi_corners =[]
	for [x,y] in r2.spazio.exterior.coords:
		roi_corners.append([x,h-y])
	roi_corners = np.array([roi_corners],np.int32)
	cv2.fillPoly(mask, roi_corners, ignore_mask_color)
	masked_image_2 = cv2.bitwise_and(image, mask)
	#cv2.imshow('image',cv2.resize(masked_image_2, (0,0), fx=1.0, fy=1.0))
	#cv2.waitKey(0)
	# Finally, we join them 
	im_floodfill = cv2.bitwise_or(masked_image_1,masked_image_2)
	# At this point, im_floodfill retains only the two rooms we are investigating
	# Mask used to flood filling.
	# Notice the size needs to be 2 pixels than the image.
	mask = np.zeros((h+2, w+2), np.uint8)
	# We retrieve the coordinates of the representative points of the two roms
	reprPoint1 = getFreeRepresentativePoint(image, r1.spazio, int(wallEnlargement*2), 100)
	reprPoint2 = getFreeRepresentativePoint(image, r2.spazio, int(wallEnlargement*2), 100)
	r1_center = (int(reprPoint1.x),int(reprPoint1.y))
	r2_center = (int(reprPoint2.x),int(reprPoint2.y))
	# Flip coordinates to work with image
	r1_center = (r1_center[0],h-r1_center[1])
	r2_center = (r2_center[0],h-r2_center[1])
	# Perform floodfill. The idea is that at this point, the representative point of the second room 
	# will be colored by the filling process iff there is a direct connection (a white space) between 
	# the two rooms
	cv2.floodFill(im_floodfill, mask, r1_center, filling_color)
	connected = False
	if im_floodfill[r2_center[1],r2_center[0]]==filling_color:
		connected = True
	#im_floodfill[r1_center[1],r1_center[0]] = 50
	#im_floodfill[r2_center[1],r2_center[0]] = 50
	#cv2.imshow('image',cv2.resize(im_floodfill, (0,0), fx=1.0, fy=1.0))
	#cv2.waitKey(0)
	return connected

