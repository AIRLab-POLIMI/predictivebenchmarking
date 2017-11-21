# -*- coding: utf-8 -*-
'''
Legge i file XML ottenuto originariamente e plotta tutto
'''
from __future__ import division
import sys,argparse
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

def plot_XML(xmlFile, outputFolder, plotAxes=False, saveResults=True):
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
	types = []
	rooms = []
	# TODO MIT DATASET DOES NOT HAVE A SCALE - EVERYTHING IS IN METERS
	# recover the dataset scale
	pixelScale = root.find("scale").findall(".//value")[0].text 
	meterScale = root.find("scale").findall(".//value")[1].text
	scalingFactor = float(meterScale) / float(pixelScale) / 100 # cm to meters	
	line_width = 5
	spaces = root.findall('.//space')
	centroids = []
	portals = []
	# potentially useful if we want to draw the nodes in different colors
	colors ={}
	# for each room
	for space in spaces: 
		# decode its id and add it to the list of rooms
		s_id =str(space.get('name'))
		s_type = str(space.get('type'))
		ids.append(s_id)
		types.append(s_type)
		# leggo la geometria della stanza 
		cen = space.find('.//centroid')
		x = float(cen.get('x'))
		y = float(cen.get('y'))
		centroids.append(rescalePoint((x,y)))
		# retrieve the room bounding polygon
		pol = space.find('.//contour')
		# and store all its points in a list (to know how to draw the room)
		points = []
		point_dict = dict()
		i = 0
		for p in pol.findall('./point'):
			x = float(p.get('x'))
			y = float(p.get('y'))
			points.append(rescalePoint((x,y)))
			point_dict[i] = rescalePoint((x,y))
			i+=1
		points.append(points[0])
		point_dict[i]=point_dict[0]
		rooms.append(points)
		# then we need to handle the doors
		prevls = None # this stores the previous linesegment wrt the current one
		for ls in space.findall('./portal') :
			if ls.get('class') != 'VERTICAL' and 'FLOORCONTOUR' not in ls.get('target'):
				e = ls.find('./edge')
				i = e.get('index')
				x = float(point_dict[int(i)][0])
				y = float(point_dict[int(i)][1])
				succx = float(point_dict[int(i)+1][0])
				succy = float(point_dict[int(i)+1][1])
				edgeLength = np.sqrt((succx-x)**2+(succy-y)**2)
				# in a perfect manhattan world scenario, either x or y would match
				if succx==x: 
					lineType = LineTypes.VERTICAL
					ang_coeff = float("inf")
				elif succy==y:
					lineType = LineTypes.HORIZONTAL
					ang_coeff = 0
				# otherwise we are dealing with a diagonal wall: consider the angular coefficient
				else:
					lineType = LineTypes.DIAGONAL
					ang_coeff = (succy-y)/(succx-x)
				# we must determine the portal type
				if ls.get('type')=='explicit':
					# in this case, the scenario is: X / X+param / X+param+offset / Y
					param = float(e.get('param'))
					portals.append(((x),(y),lineType,ang_coeff,True,edgeLength,param,0))
				elif ls.get('type')=='implicit': # implicit
					maxparam = float(e.get('maxparam'))
					minparam = float(e.get('minparam'))
					portals.append(((x), (y),lineType,ang_coeff,False,edgeLength,maxparam,minparam))
				prevls = ls

		# potentially useful to draw the nodes of the graph in different colors according to the 
		# semantic of the room that they represent

		lab = s_type
		# letters[lab]['color']
		# at the moment, we are simply overriding this and drawing them in black
		colors[s_id]='k'

	#----------------PLOT THE GROUND TRUTH ROOM LAYOUT------------------------
	# compute the maximum and minimum coordinates of the building 
	xs = []
	ys = []
	for point in root.findall('*//point'):
		xs.append(float(point.get('x')))
		ys.append(float(point.get('y')))
	xs = map(rescale,xs)
	ys = map(rescale,ys)
	xmin_gt = min(xs)
	xmax_gt = max(xs)
	ymin_gt = min(ys)
	ymax_gt = max(ys)
	x_span = xmax_gt-xmin_gt+20
	y_span = ymax_gt-ymin_gt+20
	# start plotting
	fig,ax=setup_plot(x_span,y_span,xmin_gt,xmax_gt,ymin_gt,ymax_gt)
	for index,s in enumerate(rooms):
		x,y = zip(*s)
		ax.plot(x,y, linestyle='-', color='k', linewidth=float(round(line_width)))

	#---------PLOT THE DOORS ON TOP OF THE LAYOUT----------------
	for elem in portals:
		x,y,lineType,ang_coeff,isPortalExplicit,edgeLength,maxparam,minparam = elem
		doorSize = doorWidth/scalingFactor
		if isPortalExplicit:
			if lineType==LineTypes.VERTICAL:
				linex = [x,x]
				liney = [y+maxparam*edgeLength,y+maxparam*edgeLength+doorSize]
			elif lineType==LineTypes.HORIZONTAL:
				linex = [x+maxparam*edgeLength,x+maxparam*edgeLength+doorSize]
				liney = [y,y]
			else: # diagonal
				theta = math.atan(ang_coeff)
				linex = [x+maxparam*edgeLength*math.cos(theta),x+(maxparam*edgeLength+doorWidth)*math.cos(theta)]
				liney = [y+maxparam*edgeLength*math.sin(theta),y+(maxparam*edgeLength+doorWidth)*math.sin(theta)]
		else:
			if lineType==LineTypes.VERTICAL:
				linex = [x,x]
				liney = [y+minparam*edgeLength,y+maxparam*edgeLength]
			elif lineType==LineTypes.HORIZONTAL:
				linex = [x+minparam*edgeLength,x+maxparam*edgeLength]
				liney = [y,y]
			else:
				theta = math.atan(ang_coeff)
				linex = [x+minparam*edgeLength*math.cos(theta),x+maxparam*edgeLength*math.cos(theta)]
				liney = [y+minparam*edgeLength*math.sin(theta),y+maxparam*edgeLength*math.sin(theta)]
		ax.plot(linex,liney,'w-',linewidth=(math.ceil(float(line_width*3))))
	if not plotAxes:
		ax.axis('off')
		ax.xaxis.set_major_locator(NullLocator())
		ax.yaxis.set_major_locator(NullLocator())

	if saveResults:
		fig.savefig(savename,bbox_inches='tight',pad_inches=0,dpi=100,interpolation='none')
	else :
		plt.show()
	plt.close(fig)

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

def all(xmlPath,outputFolder,plotAxes) :
	# carico le label ordinate per label e pere numero (letters e numebers rispettivamente)
	#(letters,numbers) = get_label_dict()
	#----------CREO STANZE GROUND TRUTH ------------------
	for xmlFile in glob.glob(join(xmlPath,'*.xml')):
		# for diagnostic purposes, show which file is being processed at the moment
		print xmlFile
		plot_XML(xmlFile,outputFolder,plotAxes)

def one() :
		# carico le label ordinate per label e pere numero (letters e numebers rispettivamente)
	#(letters,numbers) = get_label_dict()
	#----------CREO STANZE GROUND TRUTH ------------------
	for xmlFile in glob.glob('dataset_test/XML/*.xml'):
		plot_XML(xmlFile,{},False,True)
		exit()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Plots the XML files contained in <xml_input_path> in <output_path>. This only works with MIT file format; to plot XML files in M.Luperto format, please refer to the plot_GT.py script.')
	parser.add_argument('xml_input_path',help='the folder containing the xml files to be plotted')
	parser.add_argument('output_path', help='the folder in which the plotted maps are saved')
	parser.add_argument('-a','--plot_axes',action='store_true',help='draws the axes on top of the map')
	args = parser.parse_args()
	all(args.xml_input_path,args.output_path,args.plot_axes)
	#if len(sys.argv)==3:
	#	all(sys.argv[1],sys.argv[2])
    #all(sys.argv[1],sys.argv[2]xmlPath,outputFolder)
    #one()
    #all()
