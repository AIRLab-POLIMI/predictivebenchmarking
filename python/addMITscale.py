from __future__ import division
import sys, argparse
import xml.etree.ElementTree as ET
from os import listdir
from os.path import join,exists,isdir,isfile

def rescale(xmlFile,outputPath):
	# extract the xmlName
	xmlName = xmlFile.split('/')[-1]
	savename =join(outputPath,xmlName.split('.')[0])+'.xml'
	# decode the XML tree
	tree = ET.parse(xmlFile)
	root = tree.getroot()
	scale_elem = ET.Element('scale', {})
	represented_distance_elem = ET.Element('represented_distance', {})
	value_elem = ET.Element('value')
	value_elem.text = str(1)
	um_elem = ET.Element('um')
	um_elem.text = 'pixel'
	represented_distance_elem.append(value_elem)
	represented_distance_elem.append(um_elem)
	real_distance_elem = ET.Element('real_distance')
	value_elem = ET.Element('value')
	value_elem.text = str(100)
	um_elem = ET.Element('um')
	um_elem.text = 'cm'
	real_distance_elem.append(value_elem)
	real_distance_elem.append(um_elem)
	scale_elem.append(represented_distance_elem)
	scale_elem.append(real_distance_elem)
	root.append(scale_elem)
	tree.write(savename)

def scaleAll(xmlPath,outputPath):
	for f in listdir(xmlPath):
		if isfile(join(xmlPath,f)) and f[-4:]==".xml":
			print f
			rescale(join(xmlPath,f),outputPath)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This tool adds to each MIT dataset XML file stored in <xml_input_path> the missing scale parameter (which for MIT is 1 pixel = 1 meter) and stores the modified XML files in <xml_output_path>.')
	parser.add_argument('xml_input_path',help='the path where the unmodified MIT XML files are located')
	parser.add_argument('xml_output_path',help='the path where the scaled MIT XML files are saved')
	args = parser.parse_args()
	scaleAll(args.xml_input_path,args.xml_output_path)
