
import sys,argparse
import xml.etree.ElementTree as ET
from os import listdir
from os.path import join,exists,isdir,isfile

def sectionMapper():
	mapper = ["no_action"]*26 # preset what action should be done for each line of the world file
	mapper[6] = "resolution"
	mapper[14] = "world_name"
	mapper[15] = "file_name"
	mapper[16] = "size"
	return mapper


def XMLToWorld(xmlFile,outputPath):
	# decode the XML file
	xmlName = xmlFile.split('/')[-1][:-4]
	tree = ET.parse(xmlFile)
	root = tree.getroot()
	# retrieve the scale
	pixelScale = root.find("scale").findall(".//value")[0].text 
	meterScale = root.find("scale").findall(".//value")[1].text
	scalingFactor = float(meterScale) / float(pixelScale) / 100 # cm to meters	
	# retrieve the dataset size
	xs = []
	ys = []
	for punto in root.findall('*//point'):
		xs.append(int(float(punto.get('x'))))
		ys.append(int(float(punto.get('y'))))
	width = round((max(xs)-min(xs))*scalingFactor,2)
	height = round((max(ys)-min(ys))*scalingFactor,2)
	# we then use a world template to generate the world file
	worldTemplate = open("template.world",'r')
	outputContent = []
	lines = worldTemplate.readlines()
	actions = sectionMapper()
	for i in range(0,len(lines)):
		# we act according to the specific line
		action = actions[i]
		if action=="resolution":
			line = "resolution "+' '*15+"0.025"+'\n'
		elif action=="world_name":
			line = '  name "'+xmlName+'"\n'
		elif action=="file_name":
			line = '  bitmap "'+xmlName+'.png"'+'\n'
		elif action=="size":
			line = "  size ["+str(width)+" "+str(height)+" 1.0]"+'\n'
		else:
			line = lines[i]
		outputContent.append(line)
	worldTemplate.close()
	outputFile = open(join(outputPath,xmlName)+".world",'w')
	for item in outputContent:
		outputFile.write("%s" % item)
	outputFile.close()

def convertXMLInDirectory(xmlPath,outputPath):
	for f in listdir(xmlPath):
		if isfile(join(xmlPath,f)) and f[-4:]==".xml":
			print f
			XMLToWorld(join(xmlPath,f),outputPath)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='For each XML file inside the specified <xml_input_folder>, this tool produces a corresponding .world file inside <world_output_folder>.')
	parser.add_argument('xml_input_folder',help='the path containing the XML files for which the accompanying world files must be generated')
	parser.add_argument('world_output_folder',help='the path where the world files will be saved')
	args = parser.parse_args()
	convertXMLInDirectory(args.xml_input_folder,args.world_output_folder)

