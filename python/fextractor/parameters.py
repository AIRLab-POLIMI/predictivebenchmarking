import numpy as np
import xml.etree.cElementTree as ET
from xml.etree import ElementTree

#-------------------------------
#AZIONE = 'batch'
AZIONE = 'mappa_singola'

#-------------------------------
DISEGNA = True

#-------------------------------
#metodo di classificazione per le celle
#TRUE = Metodo di Matteo
#False = Metodo di Valerio
metodo_classificazione_celle = True
#metodo_classificazione_celle = False
#-------------------------------
#se voglio caricare i pickle basta caricare il main e quindi LOADMAIN = True, se voglio rifare tutto basta settare LOADMAIN = False
#LOADMAIN = True
LOADMAIN = False


class Path_obj():
	def __init__(self):
		#path output pickle
		self.outLayout_pickle_path = './data/OUTPUT/pickle/layout_stanze.pkl'
		self.outTopologicalGraph_pickle_path = './data/OUTPUT/pickle/grafo_topologico.pkl'

		self.out_pickle_path = './data/OUTPUT/pickle/'
		#dataset input folder
		self.INFOLDERS = './data/INPUT/'
		self.OUTFOLDERS = './data/OUTPUT/'
		self.DATASETs =['SCHOOL']
 		#dataset output folder
		self.data_out_path = './data/OUTPUT/'
		#-----------------------------MAPPA METRICA--------------------------------
		#mappa metrica di default
		self.metricMap = './data/INPUT/IMGs/SURVEY/Freiburg79_scan.png'
		#----------------------------NOMI FILE DI INPUT----------------------------
		#xml ground truth corrispondente di default
		#nome_gt = './data/INPUT/XMLs/SCHOOL/cunningham2f_updated.xml'
		self.nome_gt = './data/INPUT/XMLs/SURVEY/Freiburg79_scan.xml'
		#CARTELLA DOVE SALVO
		self.filepath = './'
		self.filepath_pickle_layout = './Layout.pkl'
		self.filepath_pickle_grafoTopologico = './GrafoTopologico.pkl'


class Parameter_obj():
	def __init__(self):
		#distanza massima in pixel per cui 2 segmenti con stesso cluster angolare sono considerati appartenenti anche allo stesso cluster spaziale
		self.minLateralSeparation = 10
		self.cv2thresh = 220

		#parametri di Canny
		self.minVal = 90
		self.maxVal = 100

		#parametri di Hough
		self.rho = 1
		self.theta = np.pi/180
		self.thresholdHough = 20
		self.minLineLength = 7
		self.maxLineGap = 3

		#parametri di DBSCAN
		self.eps = 0.85#1.5#0.85
		self.minPts = 1

		#parametri di mean-shift
		self.h = 0.023
		self.minOffset = 0.00001

		self.apertureSize = 5
		self.t = 1

		#diagonali
		self.diagonali = True

		#maxLineGap di hough
		self.m = 20

		#flip_dataset = False #questo lo metti a true se la mappa che stai guardando e' di SURVEY
		self.flip_dataset=True

		#----------------------FEATURE EXTRACTION PARAMETERS---------------------#

		# scaling factor (1 pixel = n meters)
		self.scaling_factor = 0.025

def indent(elem, level=0):
    i = "\n" + level*"\t"
    j = "\n" + (level-1)*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

def to_XML(parameter_obj, path_obj):

	root = ET.Element("root")
	par = ET.SubElement(root, "parametri")
	ET.SubElement(par, "p1", name="minLateralSeparation").text = str(parameter_obj.minLateralSeparation)
	ET.SubElement(par, "p2", name="cv2thresh").text = str(parameter_obj.cv2thresh)
	ET.SubElement(par, "p3", name="minVal").text = str(parameter_obj.minVal)
	ET.SubElement(par, "p4", name="maxVal").text = str(parameter_obj.maxVal)
	ET.SubElement(par, "p5", name="rho").text = str(parameter_obj.rho)
	ET.SubElement(par, "p6", name="theta").text = str(parameter_obj.theta)
	ET.SubElement(par, "p7", name="thresholdHough").text = str(parameter_obj.thresholdHough)
	ET.SubElement(par, "p8", name="minLineLength").text = str(parameter_obj.minLineLength)
	ET.SubElement(par, "p9", name="maxLineGap").text = str(parameter_obj.maxLineGap)
	ET.SubElement(par, "p10", name="eps").text = str(parameter_obj.eps)
	ET.SubElement(par, "p11", name="minPts").text = str(parameter_obj.minPts)
	ET.SubElement(par, "p12", name="h").text = str(parameter_obj.h)
	ET.SubElement(par, "p13", name="minOffset").text = str(parameter_obj.minOffset)
	ET.SubElement(par, "p14", name="diagonali").text = str(parameter_obj.diagonali)
	ET.SubElement(par, "p15", name="m").text = str(parameter_obj.m)
	ET.SubElement(par, "p16", name="flip_dataset").text = str(parameter_obj.flip_dataset)

	par2 = ET.SubElement(root, "path")
	ET.SubElement(par2, "p1", name="INFOLDERS").text = str(path_obj.INFOLDERS)
	ET.SubElement(par2, "p2", name="OUTFOLDERS").text = str(path_obj.OUTFOLDERS)
	#ET.SubElement(par2, "p3", name="DATASETs").text = path_obj.DATASETs
	ET.SubElement(par2, "p4", name="data_out_path").text = str(path_obj.data_out_path)
	ET.SubElement(par2, "p5", name="metricMap").text = str(path_obj.metricMap)
	ET.SubElement(par2, "p6", name="nome_gt").text = str(path_obj.nome_gt)
	ET.SubElement(par2, "p7", name="filepath").text = str(path_obj.filepath)
	ET.SubElement(par2, "p8", name="filepath_pickle_layout").text = str(path_obj.filepath_pickle_layout)
	ET.SubElement(par2, "p9", name="filepath_pickle_grafoTopologico").text = str(path_obj.filepath_pickle_grafoTopologico)

	tree = ET.ElementTree(root)
	indent(root)
	tree.write(path_obj.filepath+"parametri.xml")
	#ElementTree.dump(root)

	#root = ElementTree.parse(path_obj.filepath+"parametri.xml").getroot()
	#indent(root)
	#ElementTree.dump(root)

def load_from_XML(parXML):

	#creo nuovi oggetti del tipo parameter_obj, path_obj
	parameter_obj =  Parameter_obj()
	path_obj = Path_obj()

	tree = ET.parse(parXML)
	root = tree.getroot()
	for parametro in root.findall('parametri'):
		parameter_obj.minLateralSeparation = int(parametro.find('p1').text)
		parameter_obj.cv2thresh = int(parametro.find('p2').text)
		parameter_obj.minVal = int(parametro.find('p3').text)
		parameter_obj.maxVal = int(parametro.find('p4').text)
		parameter_obj.rho = int(parametro.find('p5').text)
		parameter_obj.theta = float(parametro.find('p6').text)
		parameter_obj.thresholdHough = int(parametro.find('p7').text)
		parameter_obj.minLineLength = int(parametro.find('p8').text)
		parameter_obj.maxLineGap = int(parametro.find('p9').text)
		parameter_obj.eps = float(parametro.find('p10').text)
		parameter_obj.minPts = int(parametro.find('p11').text)
		parameter_obj.h = float(parametro.find('p12').text)
		parameter_obj.minOffset = float(parametro.find('p13').text)
		parameter_obj.diagonali = bool(parametro.find('p14').text)
		parameter_obj.m = int(parametro.find('p15').text)
		parameter_obj.flip_dataset = bool(parametro.find('p16').text)

	for path in root.findall('path'):
		path_obj.INFOLDERS = path.find('p1').text
		path_obj.OUTFOLDERS = path.find('p2').text
		#path_obj.DATASETs = path.find('p3').text  #TODOquesto non e' una stringa ma una lista non puoi fare in qusto modo, ma siccome non ti dovrebbe servire mai per ora non lo caricare la lascialo vuoto
		path_obj.data_out_path = path.find('p4').text
		path_obj.metricMap = path.find('p5').text
		path_obj.nome_gt = path.find('p6').text
		path_obj.filepath = path.find('p7').text
		path_obj.filepath_pickle_layout = path.find('p8').text
		path_obj.filepath_pickle_grafoTopologico = path.find('p9').text

	return parameter_obj, path_obj
