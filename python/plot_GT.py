# -*- coding: utf-8 -*-
'''
Legge i file XML ottenuto originariamente e plotta tutto
'''
from __future__ import division
import sys
import math
import glob
import cv2
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import networkx as nx
import numpy as np
from os.path import join
from enum import Enum
import Image
from matplotlib.ticker import NullLocator

class LineTypes(Enum):
	HORIZONTAL = 1
	VERTICAL = 2
	DIAGONAL = 3

# Potentially useful if we want to plot images at a higher resolution
def rescale(coord):
	return coord

def rescalePoint(point):
	return (rescale(point[0]),rescale(point[1]))

def setup_plot(x_span,y_span,xmin_gt,xmax_gt,ymin_gt,ymax_gt):
	fig = plt.figure(figsize=(x_span/100, y_span/100), dpi=100)
	# VERY IMPORTANT: if this is not set, the building will be stretched and lose its original proportion!
	plt.axis('equal')
	ax = fig.add_subplot(111)
	ax.set_xlim(xmin_gt-10,xmax_gt+10)
	ax.set_ylim(ymin_gt-10,ymax_gt+10)
	return fig,ax

def plot_XML(xmlFile, outputFolder, removeAxes=True, plotGraph=False, saveResults=True):
	# extract the xmlName
	xmlName = xmlFile.split('/')[-1]
	savename =join(outputFolder,xmlName.split('.')[0])+'.png'
	# decode the XML tree
	tree = ET.parse(xmlFile)
	root = tree.getroot()
	# parameters
	doorWidth = 0.9 # meters wide: length of a door (to be sure a 40x40cm robot can travel through it)
	# a wall should probably be around 30 cm wide
	wall_width = 0.3 # meters
	ids = []
	rooms = []
	# recover the dataset scale
	pixelScale = root.find("scale").findall(".//value")[0].text 
	meterScale = root.find("scale").findall(".//value")[1].text
	scalingFactor = float(meterScale) / float(pixelScale) / 100 # cm to meters	
	line_width = (wall_width/scalingFactor)*0.7
	spaces = root.findall('.//space')
	centroids = []
	portals = []
	# potentially useful if we want to draw the nodes in different colors
	colors ={}
	# for each room
	for space in spaces: 
		# decode its id and add it to the list of rooms
		s_id =str(space.get('id'))
		ids.append(s_id)
		# leggo la geometria della stanza 
		cen = space.find('.//centroid')
		p = cen.find('.//point')
		x = int(p.get('x'))
		y = int(p.get('y'))
		centroids.append(rescalePoint((x,y)))
		# retrieve the room bounding polygon
		pol = space.find('.//bounding_polygon')
		# and store all its points in a list (to know how to draw the room)
		points = []
		for p in pol.findall('./point'):
			x = int(p.get('x'))
			y = int(p.get('y'))
			points.append(rescalePoint((x,y)))
		points.append(points[0])
		rooms.append(points)
		# then we need to handle the doors
		sr = space.find('.//space_representation')
		prevls = None # this stores the previous linesegment wrt the current one
		for ls in sr.findall('./linesegment') :
			ls_class = ls.find('./class').text
			if ls_class == 'PORTAL': 
				p = ls.find('.//point')
				x = int(p.get('x'))
				y = int(p.get('y'))
				prevp = prevls.find('.//point')
				prevx = int(prevp.get('x'))
				prevy = int(prevp.get('y'))
				# in a perfect manhattan world scenario, either x or y would match
				if prevx==x: 
					lineType = LineTypes.VERTICAL
					ang_coeff = float("inf")
				elif prevy==y:
					lineType = LineTypes.HORIZONTAL
					ang_coeff = 0
				# otherwise we are dealing with a diagonal wall: consider the angular coefficient
				else:
					lineType = LineTypes.DIAGONAL
					ang_coeff = (y-prevy)/(x-prevx)
				portals.append((rescale(x),rescale(y),lineType,ang_coeff))
			prevls = ls

		# potentially useful to draw the nodes of the graph in different colors according to the 
		# semantic of the room that they represent
		lb = space.find('.//labels')
		lab = lb.find('.//label').text
		# letters[lab]['color']
		# at the moment, we are simply overriding this and drawing them in black
		colors[s_id]='k'

	#----------------PLOT THE GROUND TRUTH ROOM LAYOUT------------------------
	# compute the maximum and minimum coordinates of the building 
	xs = []
	ys = []
	for point in root.findall('*//point'):
		xs.append(int(point.get('x')))
		ys.append(int(point.get('y')))
	xs = map(rescale,xs)
	ys = map(rescale,ys)
	xmin_gt = min(xs)
	xmax_gt = max(xs)
	ymin_gt = min(ys)
	ymax_gt = max(ys)
	x_span = xmax_gt-xmin_gt+20
	y_span = ymax_gt-ymin_gt+20
	print xmin_gt,xmax_gt,ymin_gt,ymax_gt
	print xmax_gt-xmin_gt,ymax_gt-ymin_gt
	# start plotting
	fig,ax=setup_plot(x_span,y_span,xmin_gt,xmax_gt,ymin_gt,ymax_gt)
	print int(round(line_width))
	for index,s in enumerate(rooms):
		x,y = zip(*s)
		ax.plot(x,y, linestyle='-', color='k', linewidth=int(round(line_width)))

	#---------BUILD THE TOPOLOGICAL GRAPH-----------------------------------

	# build the list of connected rooms
	# each element in the list is a pair of ids, representing rooms that are connected through doors
	connectedRooms = []
	for space in spaces:
		doors = space.findall('.//portal')
		for door in doors:
			doorConnections = []
			for i in door.findall('.//id'):
				doorConnections.append(i.text)
			connectedRooms.append(doorConnections)
	# instantiate the graph
	G=nx.Graph()
	for i in ids:
		G.add_node(i)
	# add the edges
	G.add_edges_from(connectedRooms)
	# set the location of the nodes
	pos = {ids[0]: centroids[0]}
	for i,l in enumerate(ids[1:]):
		pos[l] = (centroids[i+1])


	#---------PLOT THE GRAPH AND THE DOORS ON TOP OF THE LAYOUT----------------

	# plot the graph
	if plotGraph:
		colors = [colors[i] for i in G.nodes()]
		nx.draw_networkx_nodes(G,pos,node_size=50,node_color='b')
		nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
	for elem in portals:
		x,y,lineType,ang_coeff = elem
		if lineType==LineTypes.VERTICAL:
			dx = 0
			dy = doorWidth/scalingFactor
		elif lineType==LineTypes.HORIZONTAL:
			dx = doorWidth/scalingFactor
			dy = 0
		else: # diagonal
			theta = math.atan(ang_coeff)
			dx = doorWidth/scalingFactor*math.cos(theta)
			dy = doorWidth/scalingFactor*math.sin(theta)
		linex = [x-dx/2,x+dx/2]
		liney = [y-dy/2,y+dy/2]
		ax.plot(linex,liney,'w-',linewidth=(int(round(line_width))))
	if removeAxes:
		ax.axis('off')
		ax.xaxis.set_major_locator(NullLocator())
		ax.yaxis.set_major_locator(NullLocator())

	if saveResults:
		fig.savefig(savename,bbox_inches='tight',pad_inches=0,dpi=100,interpolation='none')
	else :
		plt.show()


def fig2data (fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw ( )
 
    # Get the RGBA buffer from the figure
    w,h = fig.canvas.get_width_height()
    buf = np.fromstring( fig.canvas.tostring_argb(), dtype=np.uint8 )
    buf.shape = (w, h,4)
 
    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = np.roll(buf, 3, axis = 2)
    return buf

def fig2img (fig):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data(fig)
    w, h, d = buf.shape
    return Image.frombytes("RGBA", ( w ,h ), buf.tostring( ))

def all(xmlPath,outputFolder,removeAxes,plotGraph) :
	# carico le label ordinate per label e pere numero (letters e numebers rispettivamente)
	#(letters,numbers) = get_label_dict()
	#----------CREO STANZE GROUND TRUTH ------------------
	for xmlFile in glob.glob(join(xmlPath,'*.xml')):
		# for diagnostic purposes, show which file is being processed at the moment
		print xmlFile
		plot_XML(xmlFile,outputFolder,removeAxes,plotGraph)

def one() :
		# carico le label ordinate per label e pere numero (letters e numebers rispettivamente)
	#(letters,numbers) = get_label_dict()
	#----------CREO STANZE GROUND TRUTH ------------------
	for xmlFile in glob.glob('dataset_test/XML/*.xml'):
		plot_XML(xmlFile,{},False,True)
		exit()

if __name__ == '__main__':
	removeAxes = True if len(sys.argv)<4 else sys.argv[3]
	plotGraph = False if len(sys.argv)<5 else sys.argv[4]
	all(sys.argv[1],sys.argv[2],removeAxes,plotGraph)
	#if len(sys.argv)==3:
	#	all(sys.argv[1],sys.argv[2])
    #all(sys.argv[1],sys.argv[2]xmlPath,outputFolder)
    #one()
    #all()
