from __future__ import division
import sys,argparse
import xml.etree.ElementTree as ET
from os import listdir
from os.path import join,exists,isdir,isfile

def rescale(xmlFile,outputPath,scale):
	# extract the xmlName
	xmlName = xmlFile.split('/')[-1]
	savename =join(outputPath,xmlName.split('.')[0])+'.xml'
	# decode the XML tree
	tree = ET.parse(xmlFile)
	root = tree.getroot()
	ids = []
	rooms = []
	# recover the dataset scale
	meterScale = float(root.find("scale").findall(".//value")[1].text)
	meterScale = meterScale/scale
	root.find("scale").findall(".//value")[1].text = str(meterScale)
	points = root.findall('.//point')
	for point in points:
		x = float(point.get('x'))
		y = float(point.get('y'))
		point.set('x',str(x*scale))
		point.set('y',str(y*scale))
	# for MIT dataset only
	'''
	edges = root.findall('.//edge')
	for edge in edges:
		param = edge.get('param')
		if param!=None:
			edge.set('param',str(float(param)*scale))
		maxparam = edge.get('maxparam')
		if maxparam!=None:
			edge.set('maxparam',str(float(maxparam)*scale))
		minparam = edge.get('minparam')
		if minparam!=None:
			edge.set('minparam',str(float(minparam)*scale))'''
	centroids = root.findall('.//centroid')
	for centroid in centroids:		
		x = float(centroid.get('x'))
		y = float(centroid.get('y'))
		centroid.set('x', str(x*scale))
		centroid.set('y', str(y*scale))
	extents = root.findall('.//extent')
	for extent in extents: 
		maxx, maxy, minx, miny = float(extent.get('maxx')), float(extent.get('maxy')), float(extent.get('minx')), float(extent.get('miny'))
		extent.set('maxx', str(maxx*scale))
		extent.set('minx', str(minx*scale))
		extent.set('maxy', str(maxy*scale))
		extent.set('miny', str(miny*scale))
	tree.write(savename)

def scaleAll(xmlPath,outputPath,scale):
	if scale.is_integer() and scale >= 1:
		for f in listdir(xmlPath):
			if isfile(join(xmlPath,f)) and f[-4:]==".xml":
				print f
				rescale(join(xmlPath,f),outputPath,int(scale))
	else:
		print "This tool only works with integer scales greater than 1!"

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Given an XML input path, it rescales all XML files in it by a factor of <scale>, intended as a magnifying effect on the amount of pixels. For instance, if the original XML file has a scale of 1 pixel = 10 centimeters and a line is 200 pixels long, a scale of 2 will have the effect of turning the XML scale to 1 pixel = 5 centimeters long and the line length will be doubled to 400 pixels. It is a necessary preprocessing step in order to plot higher resolution images. It works on both "standard" XML files and MIT XML files, provided that the latter have already been preprocessed with the addMITScale.py script.')
	parser.add_argument('xml_input_path',help='the folder containing the xml files to be rescaled')
	parser.add_argument('xml_output_path', help='the folder where to save the rescaled xml files')
	parser.add_argument('scale',help='the rescaling factor (note: must be an integer > 1)')
	args = parser.parse_args()
	scaleAll(args.xml_input_path,args.xml_output_path,float(args.scale))
