'''
chiedere conferma.
questa classe dovrebbe essere come la retta ma invece che essere infinita ha un inizio ed una fine,
che corrispondono ai bounding box della mappa.

questa credo sia una classe che serve puramente a disegnare le rette sei muri.
'''

from __future__ import division
import numpy as np
import math
from matplotlib import pyplot as plt

class Extended_segment(object):
	def __init__(self, punto1, punto2, cluster_angolare, cluster_spaziale):
		self.x1=punto1[0]
		self.y1=punto1[1]
		self.x2=punto2[0]
		self.y2=punto2[1]
		self.cluster_angolare = cluster_angolare
		self.cluster_spaziale = cluster_spaziale
	def set_weight(self, peso):
		self.peso = peso
	def set_copertura(self, n_stanze):#corrisponde al numero di stanze che tocca
		self.copertura_stanze = n_stanze

def crea_extended_segments(xmin, xmax, ymin, ymax, extended_lines):
	'''
	crea un extended_segment per ogni extended_line, come intersezione tra la extended_line e il bounding box
	'''
	extended_seg = []
	for e in extended_lines:
		if e.cluster_angolare == 0: #orizzontale
			point2 = np.array([xmax,e.punto[1]])
			seg = Extended_segment(e.punto,point2,e.cluster_angolare,e.cluster_spaziale)
			extended_seg.append(seg)
		else:		
			if e.cluster_angolare == math.radians(90): #verticale
				point2 = np.array([e.punto[0],ymax])
				seg = Extended_segment(e.punto,point2,e.cluster_angolare,e.cluster_spaziale)
				extended_seg.append(seg)
			else:
				m = math.tan(e.cluster_angolare)
				q = e.punto[1] - (m*e.punto[0])
				y_for_xmin = m*(xmin) + q
				y_for_xmax = m*(xmax) + q
				x_for_ymin = ((ymin)-q)/m
				x_for_ymax = ((ymax)-q)/m
				if e.cluster_angolare < 0 or (e.cluster_angolare)*180/math.pi > 90 :
					if(ymax < y_for_xmin):
						point1 = np.array([x_for_ymax,ymax])
					else:
						point1 = np.array([xmin,y_for_xmin])
					if(ymin > y_for_xmax):
						point2 = np.array([x_for_ymin,ymin])
					else:
						point2 = np.array([xmax,y_for_xmax])
				else:
					if(y_for_xmin > ymin):
						point1 = np.array([xmin,y_for_xmin])
					else:
						point1 = np.array([x_for_ymin,ymin])
					if(y_for_xmax < ymax):
						point2 = np.array([xmax,y_for_xmax])
					else:
						point2 = np.array([x_for_ymax,ymax])
				seg = Extended_segment(point1, point2, e.cluster_angolare, e.cluster_spaziale)
				extended_seg.append(seg)
	point1 = np.array([xmin,ymin])
	point2 = np.array([xmin,ymax])
	point3 = np.array([xmax,ymax])
	point4 = np.array([xmax,ymin])
	# seg1 = Extended_segment(point1, point2, None, None)
# 	seg2 = Extended_segment(point2, point3, None, None)
# 	seg3 = Extended_segment(point4, point3, None, None)
# 	seg4 = Extended_segment(point1, point4, None, None)
	seg1 = Extended_segment(point1, point2, None, 'bordo1')#MIO, aggiungo un cluster spaziale ai bordi
	seg2 = Extended_segment(point2, point3, None, 'bordo2')
	seg3 = Extended_segment(point4, point3, None, 'bordo3')
	seg4 = Extended_segment(point1, point4, None, 'bordo4')
	extended_seg.extend((seg1,seg2,seg3,seg4))				
	return extended_seg

def estrai_extended_segment_da_cella(cella, extended_segment):
	'''
	restituisce la lista di extended segment di una cella
	'''
	extended_comuni = []
	for edge in cella.bordi:
		for ext in extended_segment:
			#if edge.cluster_spaziale == ext.cluster_spaziale and ext.cluster_spaziale != None:
			if edge.cluster_spaziale == ext.cluster_spaziale:
				extended_comuni.append(ext)
				
	return list(set(extended_comuni))

def estrai_extended_segment_da_bordo_cella(bordo, extended_segments):
	'''
	estraggo l'extended segment corrispondente al bordo di cella
	'''
	extended = None
	for ext in extended_segments:
		#if bordo.cluster_spaziale == ext.cluster_spaziale and ext.cluster_spaziale != None:
		if bordo.cluster_spaziale == ext.cluster_spaziale:
			extended = ext
	return extended