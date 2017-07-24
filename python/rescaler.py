from __future__ import division
import sys
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
		x = int(point.get('x'))
		y = int(point.get('y'))
		point.set('x',str(x*scale))
		point.set('y',str(y*scale))
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
	scaleAll(sys.argv[1],sys.argv[2],float(sys.argv[3]))
