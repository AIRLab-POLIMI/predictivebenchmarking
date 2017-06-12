import numpy as np
import xml.etree.cElementTree as ET
from xml.etree import ElementTree

#-------------------------------
#AZIONE = 'batch'
AZIONE = 'mappa_singola'

#-------------------------------
DISEGNA = True
#DISEGNA = False
#-------------------------------
#metodo di classificazione per le celle
#TRUE = Metodo di Matteo
#False = Metodo di Valerio
metodo_classificazione_celle = 1
#metodo_classificazione_celle = 2
#metodo_classificazione_celle = 3
#-------------------------------
#se voglio caricare i pickle basta caricare il main e quindi LOADMAIN = True, se voglio rifare tutto basta settare LOADMAIN = False
#LOADMAIN = True
LOADMAIN = False

#-------------------------------
#dipende da cosa stai considerando, per le mappe parziali non abbiamo l'xml, allora non posso calcolare l'accuracy
#mappa_completa = True
mappa_completa = False
#-------------------------------
#metodo di predizione scelto
#MCMC = True
MCMC = False #equivale a fare solo le azioni geometriche semplici

azioni_semplici = False

azione_complessa = True


class Path_obj():
	def __init__(self):
		#path output pickle
		self.outLayout_pickle_path = './data/OUTPUT/pickle/layout_stanze.pkl'
		self.outTopologicalGraph_pickle_path = './data/OUTPUT/pickle/grafo_topologico.pkl'

		self.out_pickle_path = './data/OUTPUT/pickle/'
		#dataset input folder
		self.INFOLDERS = './data/INPUT/'
		self.OUTFOLDERS = './data/OUTPUT/'
		#self.DATASETs =['SCHOOL']
		self.DATASETs =['PARZIALI']
		#self.DATASETs =['PARZIALI_METRICHE_FRONTIERE']
		#self.DATASETs =['SCHOOL_grandi']
 		#dataset output folder
		self.data_out_path = './data/OUTPUT/'
		#-----------------------------MAPPA METRICA--------------------------------
		#mappa metrica di default ricorda che se e' un survey allora devi anche mettere a true flip_dataset
		#self.metricMap = './data/INPUT/IMGs/SURVEY/office_e.png'
		#self.metricMap = './data/INPUT/IMGs/SCHOOL/herndon_updated.png'
		#self.metricMap = './data/INPUT/IMGs/SCHOOL/cunningham2f_updated.png'
		#self.metricMap = './data/INPUT/IMGs/SCHOOL/bronxville_updated.png'
		#self.metricMap = './data/INPUT/PARZIALI/battle_creekhs_1_updated78.png'
		#self.metricMap = './data/INPUT/PARZIALI/battle_creekhs_1_updated148.png'
		#self.metricMap = './data/INPUT/PARZIALI/scuola_sconosciuta_3_updated78.png'
		#self.metricMap = './data/INPUT/PARZIALI/Valleceppi_P1_updated93.png'
		#self.metricMap = './data/INPUT/PARZIALI_DATASET_COMPLETO/bronxville_updated170.png'
		#self.metricMap = './data/INPUT/PARZIALI/Valleceppi_P1_updated93.png' #mappa per under seg ed overseg



		#self.metricMap = './data/INPUT/IMGs/PARZIALI_METRICHE_FRONTIERE/Valleceppi_P0_updated165.png'
		#self.metricMap = './data/INPUT/PARZIALI/scuola_sconosciuta_3_updated142.png'
		#self.metricMap = './data/INPUT/PARZIALI/battle_creekhs_1_updated66.png'
		#self.metricMap = './data/INPUT/PARZIALI/battle_creekhs_1_updated72.png'
		self.metricMap = './f52.png'
		#self.metricMap = './data/INPUT/PARZIALI_DATASET_COMPLETO/battle_creekhs_1_updated110.png'
		#self.metricMap = './data/INPUT/POST/00_20_7postprocessing.png'
		#self.metricMap = './data/INPUT/PARZIALI/scuola_sconosciuta_3_updated56.png'




		#self.metricMap = './data/INPUT/PARZIALI/battle_creekhs_1_updated78.png'

		#self.metricMap = './data/INPUT/PARZIALI/test_7.png'

		#self.metricMap = './data/INPUT/PARZIALI/Valleceppi_P1_updated38.png'
		#self.metricMap = './data/INPUT/PARZIALI/Valleceppi_P1_updated84.png'

		#self.metricMap = './data/INPUT/PARZIALI/battle_creekhs_1_updated148.png'
		#self.metricMap = './data/INPUT/IMGs/SCHOOL_grandi/cunningham2f_updated.png'

		#----------------------------NOMI FILE DI INPUT----------------------------
		#xml ground truth corrispondente di default
		#nome_gt = './data/INPUT/XMLs/SCHOOL/cunningham2f_updated.xml'
		#self.nome_gt = './data/INPUT/XMLs/SURVEY/office_e.xml'
		#self.nome_gt = './data/INPUT/XMLs/SCHOOL/cunningham2f_updated.xml'
		#self.nome_gt = './data/INPUT/XMLs/SCHOOL/bronxville_updated.xml'
		self.nome_gt = './data/INPUT/XMLs/SCHOOL/battle_creekhs_1_updated.xml'


		#self.nome_gt = './data/INPUT/XMLs/SCHOOL/Valleceppi_P0_updated.xml'
		#self.nome_gt = './data/INPUT/XMLs/SCHOOL/scuola_sconosciuta_3_updated.xml'



		#CARTELLA DOVE SALVO
		self.filepath = './'
		self.filepath_pickle_layout = './Layout.pkl'
		self.filepath_pickle_grafoTopologico = './GrafoTopologico.pkl'


class Parameter_obj():
	def __init__(self):
		#distanza massima in pixel per cui 2 segmenti con stesso cluster angolare sono considerati appartenenti anche allo stesso cluster spaziale
		#self.minLateralSeparation = 7
		self.minLateralSeparation = 20
		#self.cv2thresh = 200
		self.cv2thresh = 150
		#self.cv2thresh = 170

		#parametri di Canny
		self.minVal = 90
		self.maxVal = 100

		#parametri di Hough
		self.rho = 1
		self.theta = np.pi/180
		self.thresholdHough = 13#15,20
		self.minLineLength = 20#15,7
		self.maxLineGap = 15#15,10,3

		#parametri di DBSCAN
		self.eps = 0.85#0.85#1.5#0.85
		self.minPts = 1

		#parametri di mean-shift
		self.h = 0.023
		self.minOffset = 0.00001

		#diagonali (se ho delle linee oblique metto diagonali a False)
		self.diagonali = True
		#self.diagonali = False

		#maxLineGap di hough
		self.m = 15#20
		#self.m = 50 #mappe parziali

		#flip_dataset = False #questo lo metti a true se la mappa che stai guardando e' di SURVEY
		self.flip_dataset=False

		#aggiunti di recente
		self.apertureSize = 5
		self.t =1
		#self.minimaLunghezzaParete = 40 #TODO: ancora da aggiungere all'XML, non lo sto piu' usando
		#self.sogliaLateraleClusterMura =8 #(prima era 10, guarda quale valore e' migliore)
		self.sogliaLateraleClusterMura = 10#10#era 10 rimetterlo cosi
		#self.sogliaLateraleClusterMura =20
		self.soglia_q_split = 0.2
		#parametro che divide il peso di un edge per attribuire un peso per la matrice L di Mura
		self.sigma=0.1#0.00000125 #TODO: da inserire in XML. prima era 0.1

		#raggio d'azione del laser(serve per le metriche sulle frontiere)
		self.raggio_azione= 30

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
	ET.SubElement(par, "p17", name="apertureSize").text = str(parameter_obj.apertureSize)
	ET.SubElement(par, "p18", name="t").text = str(parameter_obj.t)
	ET.SubElement(par, "p19", name="sogliaLateraleClusterMura").text = str(parameter_obj.sogliaLateraleClusterMura)
	ET.SubElement(par, "p20", name="soglia_q_split").text = str(parameter_obj.soglia_q_split)


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
		parameter_obj.apertureSize = int(parametro.find('p17').text)
		parameter_obj.t = int(parametro.find('p18').text)
		parameter_obj.sogliaLateraleClusterMura = int(parametro.find('p19').text)
		parameter_obj.soglia_q_split = int(parametro.find('p20').text)



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
