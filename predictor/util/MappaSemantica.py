# -*- coding: utf-8 -*-

print "PLEASE REMOVE ALL IMPORTS FROM MAPPASEMANTICA"


import matplotlib.patches as patches
import sys
import matplotlib.colors as colors
import numpy as np
import math
import matplotlib.pyplot as plt
from igraph import *
from shapely.geometry import Polygon
from descartes import PolygonPatch
from shapely.geometry import Point
import random
import networkx as nx

from itertools import cycle

import cv2
import matplotlib.image as mpimg

from sklearn.cluster import DBSCAN

from scipy.spatial import ConvexHull
from shapely.ops import cascaded_union
import xml.etree.ElementTree as ET


import cmath
import logging
import glob
from xml.dom.minidom import parse
import numpy.random as rnd
from sklearn import cross_validation
from sklearn.ensemble import ExtraTreesClassifier
from igraph import *
from random import shuffle

import time
import datetime
from random import randint
import matplotlib.cbook as cbook
import matplotlib.colors as pltcol

# STUPIDO SCIKIT
import warnings
warnings.filterwarnings("ignore")

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Number of trees
N_TREES = 500



def get_stanze_gt(nome_gt, estremi):
	'''
	Prende in input il nome dell'xml ground e restituisce la lista di stanze ground truth,
	i loro nomi (classroom ecc), le loro label RC RCE e FCES e le coppie di stanze collegate
	'''

	tree = ET.parse(nome_gt)
	root = tree.getroot()

	xs = []
	ys = []
	for punto in root.findall('*//point'):
		xs.append(int(punto.get('x')))
		ys.append(int(punto.get('y')))

	#lista di stanze ground truth e dei loro id.
	ids_gt = []
	stanze_gt = []
	spaces = root.findall('.//space')
	for space in spaces:
		ids_gt.append(str(space.get('id')))
		pol = space.find('.//bounding_polygon')
		punti = []
	
		for p in pol.findall('./point'):
			x = int(p.get('x'))
			y = int(p.get('y'))
			punti.append((x,y))
			#punti.append((int(p.get('x')),ymax_gt+ymin_gt-int(p.get('y'))))
		stanze_gt.append(Polygon(punti))

	#lista dei nomi delle stanze gt che nell'xml corrispondono al campo label (classroom, stairs, lab, ecc).
	nomi_stanze_gt = []
	for space in spaces:
		nomi_stanze_gt.append(space.find('.//label').text)

	#coppie di stanze ground truth collegate tramite porta.
	collegate_gt = []
	for space in spaces:
		porte = space.findall('.//portal')
		for porta in porte:
			connessioni_porta = []
			for i in porta.findall('.//id'):
				connessioni_porta.append(ids_gt.index(str(i.text)))
			collegate_gt.append(connessioni_porta)


	#liste di label di tipo RC, RCE ed FCES, relative alle stanze ground truth.
	FCES = []
	RCE = []
	RC = []

	tree2 = ET.parse('school.xml')
	root2 = tree2.getroot() 
	for n in nomi_stanze_gt:
		for l in root2.findall('.//label'):
			nome = l.find('./name').text
			if  nome == n:
				function = l.find('./function').text
				type_ = l.find('./type').text
				rces = function# if function != 'F' else 'R'
				rces = rces if rces != 'A' else 'S'
				rces = rces if n != 'BATHROOM' else 'S'
				rce = type_
				rc = rce if rce != 'E' else 'R'
				rc = rc if n != 'WASHROOM' else 'R'
				rce = rce if n != 'WASHROOM' else 'R'
				rces = rces if n != 'WASHROOM' else 'S'
				FCES.append(rces)
				RCE.append(rce)
				RC.append(rc)

	stanze_gt = update_gt(estremi, root, xs, ys)

	#disegno stanze ground truth
	fig = plt.figure()
	plt.title('stanze_gt')
	ax = fig.add_subplot(111)
	for index,s in enumerate(stanze_gt):
		f_patch = PolygonPatch(s,fc='WHITE',ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(0,1000)
		ax.set_ylim(0,900)

	plt.show()

	return stanze_gt, nomi_stanze_gt, RC, RCE, FCES, spaces, collegate_gt


def get_corrispondenze(stanze, stanze_gt):
	'''
	Riceve stanze segmentate e ground truth
	e restituisce le corrispondenze backward e forward.
	La lista bwd e' ordinata come stanze_gt, nella posizione i contiene l'indice della stanza segmentata che corrisponde alla i-esima stanza gt. 
	Fwd è ordinata come stanze, nella posizione i contiene l'indice della stanza gt che corrisponde alla i-esima stanza segmentata.
	''' 
	#calcolo recall, salvando gli indici delle stanze segmentate corrispondenti alle gt.
	somma_recall = 0
	recalls = []
	indici_corrispondenti_bwd = []
	for s in stanze_gt:
		max_overlap_recall = 0
		for index,s2 in enumerate(stanze):
			if (s2.intersects(s)):
				if(s2.intersection(s).area >= max_overlap_recall):
					max_overlap_recall = s2.intersection(s).area
					indice_stanza_corrispondente = index
		recall_stanza = max_overlap_recall/s.area	
		recalls.append(recall_stanza)
		indici_corrispondenti_bwd.append(indice_stanza_corrispondente)
	'''
	recall = np.mean(recalls)
	recall_var = np.var(recalls)
	print recall
	'''

	#calcolo precision, salvando gli indici delle stanze ground truth corrispondenti a quelle segmentate
	indici_gt_corrispondenti_fwd = [] 
	somma_precision = 0
	precisions = []
	for s in stanze:
		max_overlap_precision = 0
		for index,s2 in enumerate(stanze_gt):
			if (s2.intersects(s)):
				if(s2.intersection(s).area >= max_overlap_precision):
					max_overlap_precision = s2.intersection(s).area
					indice_stanza_gt_corrispondente = index
		precision_stanza = max_overlap_precision/s.area	
		precisions.append(precision_stanza)
		indici_gt_corrispondenti_fwd.append(indice_stanza_gt_corrispondente)
	'''
	precision = np.mean(precisions)
	precision_var = np.var(precisions)
	print precision

	f = open('recall_precision_b.txt','w')
	f.write('recall = '+str(recall)+' +- '+str(recall_var)+'\n')
	f.write('precision = '+str(precision)+' +- '+str(precision_var)+'\n')
	f.close()
	'''

	return indici_corrispondenti_bwd, indici_gt_corrispondenti_fwd


def crea_xml(nome_xml_segmentato,stanze,porte_colleganti,collegate,indici_gt_corrispondenti_fwd,RCE,nomi_stanze_gt):
	'''
	Creo xml delle stanze segmentate.
	'''
	#------------------CREO XML--------------------------------------------------------------------

	import uuid
	id_stanze = []
	for s in stanze:
		id_stanze.append(uuid.uuid1())


	id_porte = []
	for p in porte_colleganti:
		id_porte.append(uuid.uuid1())


	xml = open(nome_xml_segmentato, "w")
	xml_id = uuid.uuid1()
	xml.write('<building id="'+str(xml_id)+'">\n<name>'+str(nome_xml_segmentato)+'</name>\n<scale>\n<represented_distance>\n<value>10</value>\n<um>pixel</um>\n</represented_distance>\n<real_distance>\n<value>90</value>\n<um>cm</um>\n</real_distance>\n</scale>\n<Info>Inserire informazioni sull\'edificio</Info>\n<building_type>\n<main_type>SCHOOL</main_type>\n</building_type>\n<floor>\n<spaces>\n')
	for i,s in enumerate(stanze):
		indice_gt_corrisp = indici_gt_corrispondenti_fwd[i]
		xml.write('<space id="'+str(id_stanze[i])+'">\n<labels>\n')		
		xml.write('<type>'+ str(RCE[indice_gt_corrisp])+ '</type>\n<label>'+ str(nomi_stanze_gt[indice_gt_corrisp])+ '</label>\n</labels>\n')
	

		xml.write('<centroid>\n<point x="'+str(int(s.centroid.x))+'" y="'+str(int(s.centroid.x))+'" />\n</centroid>\n<bounding_box>\n<maxx>\n<point x="'+str(int(s.bounds[2]))+'" y="'+str(int(s.bounds[3]))+'" />\n</maxx>\n<maxy>\n<point x="'+str(int(s.bounds[2]))+'" y="'+str(int(s.bounds[3]))+'" />\n</maxy>\n<minx>\n<point x="'+str(int(s.bounds[0]))+'" y="'+str(int(s.bounds[1]))+'" />\n</minx>\n<miny>\n<point x="'+str(int(s.bounds[0]))+'" y="'+str(int(s.bounds[1]))+'" />\n</miny>\n</bounding_box>\n<bounding_polygon>\n')
		if s.boundary.type is 'MultiLineString':
			for l in s.boundary:
				b = l.coords.xy
				for n in xrange(0,len(b[0])):
					xml.write('<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n')
		
			xml.write('</bounding_polygon>\n<space_representation>\n')
			for l in s.boundary:
				b = l.coords.xy
				for n in xrange(0,len(b[0])-1):
					xml.write('<linesegment id="'+str(uuid.uuid1())+'">\n<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n<point x="'+str(int(b[0][n+1]))+'" y="'+str(int(b[1][n+1]))+'" />\n<class>WALL</class>\n<type>EXPLICIT</type>\n<features>NORMAL</features>\n</linesegment>\n')
	
		else:	
			b = s.boundary.coords.xy
			for n in xrange(0,len(b[0])):
				xml.write('<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n')

			xml.write('</bounding_polygon>\n<space_representation>\n')
			for n in xrange(0,len(b[0])-1):
				xml.write('<linesegment id="'+str(uuid.uuid1())+'">\n<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n<point x="'+str(int(b[0][n+1]))+'" y="'+str(int(b[1][n+1]))+'" />\n<class>WALL</class>\n<type>EXPLICIT</type>\n<features>NORMAL</features>\n</linesegment>\n')

		for index,coppia in enumerate(collegate):
			if i in coppia:
				id_porta = id_porte[index]
				id_stanza1 = id_stanze[coppia[0]]
				id_stanza2 = id_stanze[coppia[1]]
				xml.write('<linesegment id="'+str(id_porta)+'">\n<point x="'+str(int(porte_colleganti[index].x))+'" y="'+str(int(porte_colleganti[index].y))+'" />\n<point x="'+str(int(porte_colleganti[index].x))+'" y="'+str(int(porte_colleganti[index].y))+'" />\n<class>PORTAL</class>\n<type>EXPLICIT</type>\n<features>NORMAL</features>\n</linesegment>\n')

		xml.write('</space_representation>\n')
		for coppia in collegate:
			if i in coppia:
				xml.write('<portals>\n')
				break

		for index,coppia in enumerate(collegate):
			if i in coppia:
				id_porta = id_porte[index]
				id_stanza1 = id_stanze[coppia[0]]
				id_stanza2 = id_stanze[coppia[1]]
				xml.write('<portal>\n<linesegment>'+str(id_porta)+'</linesegment>\n<class>HORIZONTAL</class>\n<type>EXPLICIT</type>\n<direction>BOTH</direction>\n<target>\n<id>'+str(id_stanza1)+'</id>\n<id>'+str(id_stanza2)+'</id>\n</target>\n<features>NORMAL</features>\n</portal>\n')

		for coppia in collegate:
			if i in coppia:
				xml.write('</portals>\n')
				break	
		xml.write('</space>\n')

	xml.write('</spaces>\n</floor>\n</building>')
	xml.close()
	
	return id_stanze


def find_area (array):
	a = 0
	ox,oy = array[0]
	for x,y in array[1:]:
		a += (x*oy-y*ox)
		ox,oy = x,y
	return abs(a/2)

def find_perimeter (array):
	p = 0
	ox,oy = array[0]
	for x,y in array[1:]:
		p += points_distance(ox,oy,x,y)
		ox,oy = x,y
	return p

def find_centroid (array):
	c=[0,0]
	ox,oy = array[0]
	sumx=0
	sumy=0
	for x,y in array[1:]:
		sumx += (ox+x)*((ox*y)-(x*oy))
		sumy += (oy+y)*((ox*y)-(x*oy))
		ox,oy = x,y
	area = find_area(array)
	c[0]=((1/(6*area))*sumx)
	c[1]=((1/(6*area))*sumy)
	return c

def dist_centr_bound(c,array):
	val = []
	cx,cy = c
	for x,y in array[1:]:
		val += [points_distance(cx,cy,x,y)]
	return val

def normalize_array(array):
	maxval = np.amax(array)
	for i in range(len(array)):
		array[i] = array[i]/maxval
	return array
	
def points_distance (x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2+(y1-y2)**2)

def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i


def parsa(dataset_name, xml_file):
		###ADDING FEATURES###

	#dataset
	#SOLO CORR NO LABEL
	buildingtypestr = str()
	#TUTTE LE LABEL
	buildingtypestr2 = str()
	#SOLO ALCUNE LABEL
	buildingtypestr3 = str()
	# 4 LABEL (R/C/E/S)
	buildingtypestr4 = str()
	# 2 label (R/C)
	buildingtypestr5 = str()

	withCentrality = True


	if dataset_name == 'fake' :
		data_name = 'office'
	else :
		data_name = dataset_name
	functional_labels = get_labels_reverse_dict(get_label_dict(data_name),'function','R')

	print xml_file
	xml_name = xml_file[7:]
	print xml_name
	tree = ET.parse(xml_file)
	root = tree.getroot()
	floor = root.find('floor')
	spaces = floor.find('spaces')
	pixels = int(root.find('scale').find('represented_distance').find('value').text)


	# Mi serve per numerare gli space
	i = 0
	translator = dict()
	for r in spaces.iter('space') :
		translator[r.get('id')] = i
		i += 1

	nSpaces = i
	adj_matrix = np.zeros([nSpaces, nSpaces])	

	for space in spaces.iter('space'):
		points = []
		area = 0
		perimeter = 0
		DCS = []
		for point in space.find('bounding_polygon').findall('point'):
			points += [[int(point.get('x'))/pixels,int(point.get('y'))/pixels]]
		centxml = space.find('centroid').find('point')
		cent = [int(centxml.get('x'))/pixels,int(centxml.get('y'))/pixels]
		cent = find_centroid (points)
		area = find_area (points)
		perimeter = find_perimeter (points)
		DCS = dist_centr_bound(cent,points)
	
		features_xml = ET.SubElement(space, 'features')
	
		area_xml = ET.SubElement(features_xml,'area')
		area_xml.set('value', str(area))

		perimeter_xml = ET.SubElement(features_xml,'perimeter')
		perimeter_xml.set('value', str(perimeter))

		f3_xml = ET.SubElement(features_xml,'aoverp')
		f3_xml.set('value', str(area/perimeter))

		f4_xml = ET.SubElement(features_xml,'adcs')
		f4_xml.set('value', str(np.mean(DCS)))

		f5_xml = ET.SubElement(features_xml,'Standard_Deviation_Dist_Cent-Shape')
		f5_xml.set('value', str(np.std(DCS)))

		f12_xml = ET.SubElement(features_xml,'ff')
		f12_xml.set('value', str(4*math.pi*area/math.sqrt(perimeter)))

		f13_xml = ET.SubElement(features_xml,'circularity')
		f13_xml.set('value', str(perimeter**2/area))

		f14_xml = ET.SubElement(features_xml,'normalcirc')
		f14_xml.set('value', str(4*math.pi*area/perimeter**2))

		f15_xml = ET.SubElement(features_xml,'andcs')
		f15_xml.set('value', str(np.mean(normalize_array(DCS))))

		f16_xml = ET.SubElement(features_xml,'Standard_Deviation_Dist_Cent-Shape')
		f16_xml.set('value', str(np.std(normalize_array(DCS))))



		#legacy: for plotting
		#poly = plt.Polygon(points, closed=True, fill=None, edgecolor='r')
		#plt.gca().add_patch(poly)
	
		#MISSING FEATURES:
		#For 6 7 8
		#complex_points = []
		#for e in points:
		#	complex_points.append(complex(e[0],e[1]))
		#print complex_points
		#fftarray = np.fft.fft(complex_points)	
		# 9 10 11 MISSING



		portals = space.find('portals')
		space_id = space.get('id')
		if portals:
			for portal in portals.iter('portal') :
				tmp = tuple([i.text for i in portal.find('target').findall('id')])

				if tmp[1] != space_id :
					adj_matrix[translator[space_id]][translator[tmp[1]]] = 1
				elif tmp[0] != space_id :
					adj_matrix[translator[space_id]][translator[tmp[0]]] = 1
				else :
					print 'error!'
					exit()

	graph = Graph.Adjacency(adj_matrix.tolist(), mode=ADJ_UNDIRECTED)
	graph.vs["bs"] = graph.betweenness()
	graph.vs["cs"] = graph.closeness()

	# print "bs", graph.vs["bs"]
	# print "cs", graph.vs["cs"]
	# layout = graph.layout("kk")
	# plot(graph, layout = layout)

	
	for space in spaces.iter('space'):

		features_xml = space.find('features')

		# Calcolo e salvo la betweenness e la closeness
		f17_xml = ET.SubElement(features_xml,'betweenness')
		f17_xml.set('value', str(float(graph.vs[translator[space.get('id')]]["bs"])/((nSpaces-1)*(nSpaces-2))))
		f18_xml = ET.SubElement(features_xml,'closeness')
		f18_xml.set('value', str(graph.vs[translator[space.get('id')]]["cs"]))
		# Traduco i vicini in label
	
	#legacy: linesegment plot for comparison
	'''for space in spaces.iter('space'):
		for lineseg in space.find('space_representation').findall('linesegment'):
			points = []
			for point in lineseg.findall('point'):
				points += [int(point.get('x'))]
				points += [int(point.get('y'))]
			line = plt.Line2D((points[0], points[2]), (points[1], points[3]), lw=0.5, markerfacecolor='b', markeredgecolor='b')
			plt.gca().add_line(line)'''




	indent(root)
	tree.write('Output/XMLs/'+xml_name)
	
	return 'Output/XMLs/'+xml_name


def getTrainingData(labels_type, centrality, max_samples):
	# Recupero i dati degli xml ground truth school, li uso come training, creo training_rset
	#features = dizionario che ad ogni id di xml associa tutte le features.
	features_training = get_features('school')
	#all_buildings = lista di tutti gli edifici. Ogni edificio consiste a sua volta in una lista di stanze, e ogni stanza consiste nell'insieme delle features con aggiunte le labels delle stanze confinanti e la propria label indicata come un numero.
	all_buildings_training, id_edifici_training, id_stanze_training, labels_training, labels_sys_training = format_features(features_training, "spaces", 'school', labels_type, centrality)
	shuffle(all_buildings_training)
	if(max_samples > 0) :
		buildings_training = all_buildings_training[:max_samples]
	else :
		buildings_training = all_buildings_training

	training_rooms = []
	for b in buildings_training:
		training_rooms += b 
	training_rset = np.array(training_rooms)

	training_labels = []
	for r in training_rset:
		training_labels.append(r[-1])
	
	return training_rset, training_labels


def getTestingData(xml_file, dataset_name, labels_type, centrality, max_samples):
	# Recupero i dati dei miei xml, da classificare, e li salvo in training_rset_shuf
	#features = dizionario che ad ogni id di xml associa tutte le features.
	(features, xml_names) = get_features_xml(dataset_name, xml_file)
	#all_buildings = lista di tutti gli edifici. Ogni edificio consiste a sua volta in una lista di stanze, e ogni stanza consiste nell'insieme delle features con aggiunte le labels delle stanze confinanti e la propria label indicata come un numero.
	(all_buildings, id_edifici, id_stanze, labels, labels_sys) = format_features(features, "spaces", dataset_name, labels_type, centrality)
	#shuffle(all_buildings)
	if(max_samples > 0) :
		buildings = all_buildings[:max_samples]
	else :
		buildings = all_buildings

	errors = []

	testing_rooms = []
	for b in buildings:
		testing_rooms += b 
	testing_rset = np.array(testing_rooms)


	xml_nomi = []
	xml_ids = []
	xml_names = []

	tree = ET.parse(xml_file)	
	root = tree.getroot()	
	xml_name = xml_file[6:]
	xml_nomi.append(xml_name)
	xml_ids.append(root.attrib.get('id'))
	for id_ed in id_edifici:
		for i, xml_id in enumerate(xml_ids):
			if id_ed==xml_id:
				xml_names.append(xml_nomi[i])
	
	return testing_rset, xml_names, id_edifici, id_stanze, labels, labels_sys


def classifica(clf, testing_rset, f, xml_names, id_edifici, id_stanze, labels, labels_sys, xml_file,):
	predizioni = []
	errors = []
	for index,r in enumerate(testing_rset):
		prediction = clf.predict(r[:-1])
		predizioni.append((str(labels_sys[int(prediction)]),id_stanze[index]))
		f.write("nome xml = "+str(xml_names[index])+"\n")
		f.write("id_edificio: "+str(id_edifici[index])+"\n")
		f.write("id_stanza = "+str(id_stanze[index])+"\n")
		f.write("label = "+str(labels[index])+"\n")
		f.write("predizione = "+str(prediction)+"\n")
		f.write("predizione = "+str(labels_sys[int(prediction)])+"\n\n")
		if labels[index] != prediction:
			errors.append((str(xml_names[index]),1))
			f.write("errore\n")
		else:
			errors.append((str(xml_names[index]),0))
	errori_per_edificio = []
	index = 0

	for nome in xml_names:
		tmp = []
		for e in errors:
			if e[0]==str(nome):
				tmp.append(e[1])
		n_stanze = len(tmp) 
		somma_errori_edificio = np.count_nonzero(tmp)
		errori_per_edificio.append(somma_errori_edificio / n_stanze)

	f.write("error mean "+str(xml_file)+" = "+str(np.mean(errori_per_edificio))+"\n")
	f.write("error var "+str(xml_file)+" = "+str(np.var(errori_per_edificio))+"\n\n\n")
	f.close()

	return predizioni
	



def classif(dataset_name, xml_file, labels_type, centrality, max_samples):
	f = open('classificazione'+str(labels_type)+str(centrality)+'.txt', 'w')

	all_lables = True

	log_pattern = 'Classif: %s, Dataset: %s, Samples: %s, Lables: %s, Centrality: %s, Error Mean: %f, Error Var: %f, #True: %f, #False: %f'

	# Log handler
	handler = None

	# Crea un file di log. Nel nome viene creato 
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y_%H-%M-%S')
	#handler = create_logfile('results_' + st, logger, handler)

	#creo il classificatore
	n_estimators = N_TREES
	criterion = 'entropy'
	max_depth = None
	min_samples_split = 1
	random_state = 0
		    
	clf = ExtraTreesClassifier(n_estimators = n_estimators, criterion = criterion, max_depth = max_depth, min_samples_split = min_samples_split, random_state = random_state)

	#recupero dati di training, ovvero le stanze ground truth: vettore di feature e rispettive label
	(training_rset, training_labels) = getTrainingData(labels_type, centrality, max_samples)

	#addestro il classificatore
	clf.fit(training_rset[:, :-1],training_labels)
	
	#recupero dati di testing
	(testing_rset, xml_names, id_edifici, id_stanze, labels, labels_sys) = getTestingData(xml_file, dataset_name, labels_type, centrality, max_samples)
	
	f.write('labels_type = '+str(labels_type)+'\n')
	f.write('centrality = '+str(centrality)+'\n')
	
	#classifico
	predizioni = classifica(clf, testing_rset, f, xml_names, id_edifici, id_stanze, labels, labels_sys, xml_file) 	
	
	return predizioni
	








def get_features_xml(dataset_name, xml_file) :
	counter = 0
	xml_names = []
	id_edifici = []
	id_stanze = []
	space_labels = {}
	labels = []
	portal_tuple = []
	buildings_dict = dict()

	if counter != 0 :
		print "Start parsing files."
		#break
	else :
		counter += 1
	print "#"*50
	print xml_file
	xml_name = xml_file[7:]
	print xml_name
	tree = ET.parse(xml_file)
	root = tree.getroot()
	# Assumendo che la root sia sempre <building>
	floor_id = root.attrib.get('id')
	floor = root.find('floor')
	spaces = floor.find('spaces')
	pixels = int(root.find('scale').find('represented_distance').find('value').text)
	portals = root.find('portal')
	#labels = list(set(labels))
	rooms = dict()

	# Mi serve per numerare gli space
#dizionario che all'id del primo space (stanza) associa 0, all'id della seconda stanza 1 e cosi' via.
	i = 0
	translator = dict()
	for r in spaces.iter('space') :
		translator[r.get('id')] = i
		i += 1

	# Recupero e salvo le features
	for space in spaces.iter('space') :
		xml_names.append(xml_name)
		id_edifici.append(floor_id)
		id_stanze.append(space.get('id'))
		#nel dizionario space_labels, ad ogni id delle stanze associo la label (nei miei xml e' room o corridor).
		space_labels[space.get('id')] = space.find('labels').find('label').text
		#creo un dizionario space_dict in cui alla chiave label associo la label della stanza.
		space_dict = dict()
		space_dict['label'] = space.find('labels').find('label').text
		space_dict['connections'] = []
		#alla lista labels aggiungo la label della stanza.
		labels.append(space.find('labels').find('label').text)
		portals = space.find('portals')

		# Appendo le features al dizionario space_dict.
		features_xml = space.find('features')
		area = features_xml.find('area').get('value')
		space_dict['area'] = area
		perimeter = features_xml.find('perimeter').get('value')
		space_dict['perimeter'] = perimeter
		aoverp = features_xml.find('aoverp').get('value')
		space_dict['aoverp'] = aoverp
		adcs = features_xml.find('adcs').get('value')
		space_dict['adcs'] = adcs
		ff = features_xml.find('ff').get('value')
		space_dict['ff'] = ff
		circularity = features_xml.find('circularity').get('value')
		space_dict['circularity'] = circularity
		normalcirc = features_xml.find('normalcirc').get('value')
		space_dict['normalcirc'] = normalcirc
		andcs = features_xml.find('andcs').get('value')
		space_dict['andcs'] = andcs
		# Bulding type
		space_dict['building'] = dataset_name
		space_dict['betweenness'] = features_xml.find('betweenness').get('value')
		space_dict['closeness'] = features_xml.find('closeness').get('value')

		#per ogni orta della stanza, aggiungo al dizionario l'id della stanza a cui si arriva tramite quella porta, sotto la chiave connections.
		if portals:
			for portal in portals.iter('portal') :
				tmp = tuple([i.text for i in portal.find('target').findall('id')])
				if tmp[1] != space.get('id') :
					space_dict['connections'].append(tmp[1])
				elif tmp[0] != space.get('id') :
					space_dict['connections'].append(tmp[0])
				else :
					print 'error!'
					exit()

				if not ((tmp[0],tmp[1]) in portal_tuple or (tmp[1],tmp[0]) in portal_tuple) :
					portal_tuple.append(tmp)

		#aggiungo al dizionario rooms il dizionario space_dict, sotto la chiave id della stanza.
		rooms[space.get('id')] = space_dict

#aggiungo la chiave neigh ad ogni dizionario incluso nel dizionario rooms. Questa contiene le labels dei vicini.
	for i in rooms.keys() :
		# Traduco i vicini in label
		neigh_labels = []
		for j in rooms[i]['connections'] :
			neigh_labels.append(rooms[j]['label'])
		rooms[i]['neigh'] = neigh_labels

#aggiungo il dizionario rooms al dizionario buildings_dict, sotto la chiave floor_id.
	buildings_dict[floor_id] = rooms
#ritorno buildings_dict, che e' un dizionario che ha come chiavi gli id dei file xml appartenenti ad uno stesso tipo/cartella. Ogni elemento associato a una chiave e' a sua volta un dizionario, chiamato rooms, che ha come chiavi gli id delle stanze e come valori un dizionario space_dict. Questo dizionario ha come chiavi i nomi delle features (a cui e' stato aggiunto neigh) a cui sono associati i valori estratti dall'xml.
	return buildings_dict, xml_names


def format_features(features, ftype = 'spaces', dataset_name = 'school', labels_syss = "RC", centrality = 'Y') :

	#dizionario che esamina il file dataset_name.xml (ad es. school.xml) e associa a ogni nome di label le lettere relative a RC, RCE e RCES.
	label_dict = get_labels_dict(dataset_name)

	labels_sys = []
	#per ogni chiave del dizionario prendo tutti i valori relativi a labels_syss (che puo essere RC RCE o RCES) e li salvo nella lista labels_sys. Ad esempio se labels_syss e' RC, labels_sys conterra' i valori R e C (solo una volta ciascuno, non ripetuti).
	for j in label_dict.keys() :
		if not(label_dict[j][labels_syss] in labels_sys) :
			 labels_sys.append(label_dict[j][labels_syss])

	buildings = []
	id_edifici = []
	id_stanze = []
	labels = []
	# Trasformo tutte le stanze degli edifici in una matrice
	# di feature con label di tipo "labels_syss"
	for building_id in features.keys() :
		rooms = []
		for room_id in features[building_id].keys() :
			id_edifici.append(building_id)
			id_stanze.append(room_id)
			room = []
			# Copio tutte le feature (escluse le label e l'edificio)
			room.append(float(features[building_id][room_id]['area']))
			room.append(float(features[building_id][room_id]['perimeter']))
			room.append(float(features[building_id][room_id]['aoverp']))
			room.append(float(features[building_id][room_id]['adcs']))
			room.append(float(features[building_id][room_id]['ff']))
			room.append(float(features[building_id][room_id]['circularity']))
			room.append(float(features[building_id][room_id]['normalcirc']))
			room.append(float(features[building_id][room_id]['andcs']))

			if centrality == 'Y' :
				room.append(float(features[building_id][room_id]['betweenness']))
				room.append(float(features[building_id][room_id]['closeness']))

			# Conto le label dei neighbors di ogni room
			# e aggiungo il numero alle features
			nLabels = dict()
			for l in labels_sys:
				nLabels[l] = 0

			for j in features[building_id][room_id]['neigh'] :
				for l in labels_sys:
					if label_dict[j][labels_syss] == l:
						nLabels[l] += 1

			for l in labels_sys :
				room.append(nLabels[l])

			# Salvo la label della stanza come uno scalare
			real_label = features[building_id][room_id]['label']
			tmp_label = label_dict[real_label][labels_syss]
			label_number = labels_sys.index(tmp_label)
			labels.append(label_number)
			room.append(label_number)

			# Salvo il tipo di edificio come uno scalare, pero' solo se ftype (ovvero il secondo parametro di format_features) e' buildings e non spaces.
			if ftype == "buildings" :
				tmp_building = features[building_id][room_id]['building']
				room.append(building_to_number(tmp_building))

			# Aggiungo la stanza a quelle gia' salvate
			rooms.append(room)

		buildings.append(rooms)

	# Il dato da classificare e' sempre
	# sull'ultima colonna della matrice "rooms"
	return buildings, id_edifici, id_stanze, labels, labels_sys



def get_features(dataset_name = 'school') :
	counter = 0
	xml_names = []
	id_edifici = []
	id_stanze = []
	space_labels = {}
	labels = []
	portal_tuple = []
	buildings_dict = dict()
	#for xml_file in glob.glob('ClassifierInputs/XMLs/'+dataset_name+'/*.xml'): #questa cartella dov'e?
	for xml_file in glob.glob('Output/XMLs/'+dataset_name+'/*.xml'):
		if counter != 0 :
			print "Start parsing files."
			#break
		else :
			counter += 1
		print "#"*50
		print xml_file
		xml_name = xml_file[6:]
		print xml_name
		tree = ET.parse(xml_file)
		root = tree.getroot()
		# Assumendo che la root sia sempre <building>
		floor_id = root.attrib.get('id')
		floor = root.find('floor')
		spaces = floor.find('spaces')
		pixels = int(root.find('scale').find('represented_distance').find('value').text)
		portals = root.find('portal')
		#labels = list(set(labels))
		rooms = dict()

		# Mi serve per numerare gli space
#dizionario che all'id del primo space (stanza) associa 0, all'id della seconda stanza 1 e cosi' via.
		i = 0
		translator = dict()
		for r in spaces.iter('space') :
			translator[r.get('id')] = i
			i += 1

		# Recupero e salvo le features
		for space in spaces.iter('space') :
			xml_names.append(xml_name)
			id_edifici.append(floor_id)
			id_stanze.append(space.get('id'))
			#nel dizionario space_labels, ad ogni id delle stanze associo la label (nei miei xml e' room o corridor).
			space_labels[space.get('id')] = space.find('labels').find('label').text
			#creo un dizionario space_dict in cui alla chiave label associo la label della stanza.
			space_dict = dict()
			space_dict['label'] = space.find('labels').find('label').text
			space_dict['connections'] = []
			#alla lista labels aggiungo la label della stanza.
			labels.append(space.find('labels').find('label').text)
			portals = space.find('portals')

			# Appendo le features al dizionario space_dict.
			features_xml = space.find('features')
			area = features_xml.find('area').get('value')
			space_dict['area'] = area
			perimeter = features_xml.find('perimeter').get('value')
			space_dict['perimeter'] = perimeter
			aoverp = features_xml.find('aoverp').get('value')
			space_dict['aoverp'] = aoverp
			adcs = features_xml.find('adcs').get('value')
			space_dict['adcs'] = adcs
			ff = features_xml.find('ff').get('value')
			space_dict['ff'] = ff
			circularity = features_xml.find('circularity').get('value')
			space_dict['circularity'] = circularity
			normalcirc = features_xml.find('normalcirc').get('value')
			space_dict['normalcirc'] = normalcirc
			andcs = features_xml.find('andcs').get('value')
			space_dict['andcs'] = andcs
			# Bulding type
			space_dict['building'] = dataset_name
			space_dict['betweenness'] = features_xml.find('betweenness').get('value')
			space_dict['closeness'] = features_xml.find('closeness').get('value')

			#per ogni orta della stanza, aggiungo al dizionario l'id della stanza a cui si arriva tramite quella porta, sotto la chiave connections.
			if portals:
				for portal in portals.iter('portal') :
					tmp = tuple([i.text for i in portal.find('target').findall('id')])
					if tmp[1] != space.get('id') :
						space_dict['connections'].append(tmp[1])
					elif tmp[0] != space.get('id') :
						space_dict['connections'].append(tmp[0])
					else :
						print 'error!'
						exit()

					if not ((tmp[0],tmp[1]) in portal_tuple or (tmp[1],tmp[0]) in portal_tuple) :
						portal_tuple.append(tmp)

			#aggiungo al dizionario rooms il dizionario space_dict, sotto la chiave id della stanza.
			rooms[space.get('id')] = space_dict

#aggiungo la chiave neigh ad ogni dizionario incluso nel dizionario rooms. Questa contiene le labels dei vicini.
		for i in rooms.keys() :
			# Traduco i vicini in label
			neigh_labels = []
			for j in rooms[i]['connections'] :
				neigh_labels.append(rooms[j]['label'])
			rooms[i]['neigh'] = neigh_labels

#aggiungo il dizionario rooms al dizionario buildings_dict, sotto la chiave floor_id.
		buildings_dict[floor_id] = rooms
#ritorno buildings_dict, che e' un dizionario che ha come chiavi gli id dei file xml appartenenti ad uno stesso tipo/cartella. Ogni elemento associato a una chiave e' a sua volta un dizionario, chiamato rooms, che ha come chiavi gli id delle stanze e come valori un dizionario space_dict. Questo dizionario ha come chiavi i nomi delle features (a cui e' stato aggiunto neigh) a cui sono associati i valori estratti dall'xml.
	return buildings_dict


def building_to_number(building) :
	if building == 'school' :
		return 0
	elif building == 'office' :
		return 1
	elif building == 'fake' :
		return 2
	else :
		return -1


def get_labels_dict(buildingtype = 'school'):
	labelxml = buildingtype+'.xml'
	xmldoc = parse(labelxml)
	labels = {}
	letters = {}
	nodeLabels = xmldoc.getElementsByTagName("label")
	counter = 1;
	for nodeLabel in nodeLabels:
		name = nodeLabel.getElementsByTagName("name")[0].childNodes[0].nodeValue
		letter = nodeLabel.getElementsByTagName("letter")[0].childNodes[0].nodeValue
		function = nodeLabel.getElementsByTagName("function")[0].childNodes[0].nodeValue
		RCES = function# if function != u'F' else u'R'
		RCES = RCES if RCES != u'A' else u'S'
		RCES = RCES if name != 'BATHROOM' else u'S'
		RCE = nodeLabel.getElementsByTagName("type")[0].childNodes[0].nodeValue
		RC = RCE if RCE != u'E' else u'R'
		# Sistemo le washroom
		RC = RC if name != 'WASHROOM' else 'R'
		RCE = RCE if name != 'WASHROOM' else 'R'
		RCES = RCES if name != 'WASHROOM' else u'S'
		labels[name] = letter
		letters[name] = { 
				'RC' : RC,
				'RCE' : RCE,
				'RCES':  RCES,
				'key' : name
		}
		counter+=1;
	return letters


def creaMappaSemantica(predizioni, G, pos, stanze, id_stanze, estremi, colori, labels, collegate):
	#salvo le predizioni prodotte dalla classificazione delle mie stanze
	semantic_labels = {}
	for i,id_stanza in enumerate(id_stanze):
		for p in predizioni:
			if p[1]==str(id_stanza):
				#print ("si")
				semantic_labels[i] = p[0]

	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]

	#plotto le mie stanze
	fig = plt.figure()
	plt.title('mappa semantica prodotta')
	ax = fig.add_subplot(111)
	for index,s in enumerate(stanze):
		f_patch = PolygonPatch(s,fc=colori[index],ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin-10,xmax+10)
		ax.set_ylim(ymin-10,ymax+10)


	#plotto il grafo
	nx.draw_networkx_nodes(G,pos,node_color='w')
	nx.draw_networkx_labels(G,pos,semantic_labels)

	for coppia in collegate:
		i1 = list(set(labels)).index(coppia[0])
		i2 = list(set(labels)).index(coppia[1])
		p1 = stanze[i1].representative_point()
		p2 = stanze[i2].representative_point()
		plt.plot([p1.x,p2.x],[p1.y,p2.y],color='k',ls = 'dotted', lw=0.5)

	
	#plt.show()


def creaMappaSemanticaGt(stanze_gt, collegate_gt, labels_type, estremi, colori):
	#salvo le etichette ground truth
	semantic_labels_gt = {}
	for i, rc in enumerate(labels_type):
		semantic_labels_gt[i] = rc
	

	#creo un dizionario che contiene le posizioni dei nodi. Le posizioni sono i representative point delle stanze corrispondenti. Creo la prima chiave del dizionario, poi aggiungo le restanti con un ciclo for.
	pos_gt = {int(0): (stanze_gt[0].representative_point().x,stanze_gt[0].representative_point().y)}
	for i,s in enumerate(stanze_gt[1:]):
		pos_gt[i+1] = (s.representative_point().x,s.representative_point().y)


	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]

	#plotto le stanze ground truth
	fig = plt.figure()
	plt.title('ground truth')
	ax = fig.add_subplot(111)
	for index,s in enumerate(stanze_gt):
		f_patch = PolygonPatch(s,fc=random.choice(colori),ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin-10,xmax+10)
		ax.set_ylim(ymin-10,ymax+10)

	#creo grafo ground truth
	G=nx.Graph()
	for i,s in enumerate(stanze_gt):
		G.add_node(i)


	#aggiungo l'attributo posizione ad ogni nodo
	for n, p in pos_gt.iteritems():
		G.node[n]['pos'] = p


	#plotto il grafo
	nx.draw_networkx_nodes(G,pos_gt,node_color='w')
	nx.draw_networkx_labels(G,pos_gt,semantic_labels_gt)

	for coppia in collegate_gt:
		p1 = stanze_gt[coppia[0]].representative_point()
		p2 = stanze_gt[coppia[1]].representative_point()
		plt.plot([p1.x,p2.x],[p1.y,p2.y],color='k',ls = 'dotted', lw=0.5)


def update_gt(estremi,root, xs, ys):

	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]
	xmin_gt = min(xs)
	xmax_gt = max(xs)
	ymin_gt = min(ys)
	ymax_gt = max(ys)

	fattore_x = (xmax-xmin)/(xmax_gt-xmin_gt)
	fattore_y = (ymax-ymin)/(ymax_gt-ymin_gt)
	xmin_gt_scalato = xmin_gt*fattore_x
	ymin_gt_scalato = ymin_gt*fattore_y
	stanze_gt = []
	spaces = root.findall('.//space')
	for space in spaces:
		pol = space.find('.//bounding_polygon')
		punti = []
		for p in pol.findall('./point'):
			x = int(p.get('x'))
			y = int(p.get('y'))
			x_scalato = x*fattore_x
			y_scalato = y*fattore_y
			x_traslato = x_scalato+(xmin-xmin_gt_scalato)
			y_traslato = y_scalato+(ymin-ymin_gt_scalato)
			punti.append((x_traslato,y_traslato))
			#punti.append((int(p.get('x')),ymax_gt+ymin_gt-int(p.get('y'))))
		stanze_gt.append(Polygon(punti))
	return stanze_gt

