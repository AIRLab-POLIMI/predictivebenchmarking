# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
import cv2
from skimage.morphology import medial_axis
from skimage.morphology import skeletonize
from scipy import ndimage
import pymorph as m
from shapely.geometry import Point
from util import disegna as dsg
from scipy import ndimage



def flip_vertici(vertici_porte, altezza):
	for v in vertici_porte:
		v[1] = altezza - v[1]
	return vertici_porte


def isolato(immagine,riga,col):
	for r in xrange(max(0,riga-1),min(immagine.shape[0],riga+2)):
		for c in xrange(max(0,col-1),min(immagine.shape[1],col+2)):
			if (immagine[r][c]==True) and not (r==riga and c==col):
				return False
	return True

def get_distance_transforme(im_bw):
	'''
	restituisce la distance transforme
	'''
	distanceMap = ndimage.distance_transform_edt(im_bw)
	return distanceMap

def medial_points(thresh):
	#leggo l'immagine e la trasformo in 0 o 255
	
	(th, im_bw) = cv2.threshold(thresh, 240, 255, cv2.THRESH_BINARY_INV)
	#plt.imshow(cv2.cvtColor(im_bw,cv2.COLOR_GRAY2RGB))
	#plt.show()

	#points = punti dei muri
	points = []
	for y in xrange(0,im_bw.shape[1]):
		for x in xrange(im_bw.shape[0]):
			if im_bw[x, y] == (0):
				points.append([y,x])

	points = np.asarray(points)

	#distance transform
# 	distanceMap = ndimage.distance_transform_edt(im_bw)
# 	plt.title('8.distance map')
# 	plt.imshow(distanceMap)
# 	plt.show()
	#disegno distance transforme
	
	#distanceMap = dsg.disegna_distance_transform(im_bw, filepath = filepath)#plot
	distanceMap = get_distance_transforme(im_bw)

	#medial axis sulla distance transform
	skel, distance = medial_axis(distanceMap, return_distance=True)
	
	#elimino parte delle imprecisioni della skeletonization
	#b3 = m.thin(skel, m.endpoints('homotopic'), 15)
	b3 = m.thin(skel, m.endpoints('homotopic'), 500)
	
	'''
	#------
	import copy
	b4 = copy.copy(b3)
	#ottengo solo critical points
	#critical_points = []
	for riga in xrange(b4.shape[0]):
		for col in xrange(b4.shape[1]):
			if b4[riga][col]==True:
				#controllo se in un intorno di quel punto c'è una frontiera
				#creo intorno del pixel 
				start_x = riga-17 #15
				end_x = riga+17
				start_y = col-17
				end_y = col+17
				count = 0
				for x in xrange(start_x,end_x):
					for y in xrange(start_y, end_y):
						if im_bw[x, y] <= (200): #se almeno una componente rgb di un pixel nell'introno del pixel cha fa parte del medial axis e' un pixel della frontiera
							count+=1
				if count <= 5:
					b4[riga][col]=False
				# else:
# 					#è un critical_points
# 					critical_points.append([riga, col])

	critical_points = []
	#salvo in una lista i critical points che fanno parte del medial axis
	for riga in xrange(b4.shape[0]):
		for col in xrange(b4.shape[1]):
			if (b4[riga][col]==True):
				critical_points.append((col,riga))
	critical_points = np.asarray(critical_points)
	flip_vertici(critical_points,b4.shape[0]-1)
	#------
	'''
	

	#elimino i punti isolati del medial axis, sono rumore
	for riga in xrange(b3.shape[0]):
		for col in xrange(b3.shape[1]):
			if b3[riga][col]==True and isolato(b3,riga,col):
				b3[riga][col]=False
	
	
	
	#disegno medial axis
# 	plt.title('9.medial axis')
# 	plt.plot(points[:,0],points[:,1],'.')			
# 	plt.imshow(b3,cmap='Greys')
# 	plt.show()
	#disegno medial axis
	#dsg.disegna_medial_axis(points, b3, filepath = filepath)#quiiiiiiiii

	punti_medial = []
	#salvo in una lista i punti che fanno parte del medial axis
	for riga in xrange(b3.shape[0]):
		for col in xrange(b3.shape[1]):
			if (b3[riga][col]==True):
				punti_medial.append((col,riga))
	punti_medial = np.asarray(punti_medial)
	flip_vertici(punti_medial,b3.shape[0]-1)

	return punti_medial, distanceMap, points, b3, distance


def trovaCollegamenti(stanze,stanze_collegate,punti_medial):
	'''
Date le stanze e i punti del medial axis, trova i punti che confinano con più di una stanza, e restituisce la lista di coppie di stanze collegate e la lista di coordinate dei punti/porte.
	'''
	porte_colleganti = []
	for p in punti_medial:
		a = 0
		temp = []
		for index,s in enumerate(stanze):
			if (s.boundary).distance(Point(p[0],p[1])) < 1: #se il bordo della stanza dista meno di 1 dal punto.
				a+=1
				if not (s in temp): #se la stanza non è già stata aggiunta la aggiungo.
					temp.append(index)
		temp.sort()
		#se la coppia non è già in stanze_porte, la aggiungo.
		if not (temp in stanze_collegate) and (len(temp)==2):
			stanze_collegate.append(temp)
			porte_colleganti.append(Point(p[0],p[1]))
		if (len(temp)>2):
			for index,a in enumerate(temp):
				for b in temp[index+1:]:
					tmp = []
					tmp.extend((a,b))
					if not (tmp in stanze_collegate):
						stanze_collegate.append(tmp)
						porte_colleganti.append(Point(p[0],p[1]))	

	#print(stanze_collegate)
	return stanze_collegate, porte_colleganti



def critical_points(metricMap):
	'''
	ottengo i critical points dal medial axis
	'''
	
	if cv2.__version__[0] == '3' :
		flag = cv2.IMREAD_GRAYSCALE
	elif cv2.__version__[0] == '2' :
		flag = cv2.CV_LOAD_IMAGE_GRAYSCALE
	else :
		raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*') 

	im_gray = cv2.imread(metricMap, flag)
	#leggo l'immagine e la trasformo in 0 o 255	
	(thresh, im_bw) = cv2.threshold(im_gray, 240, 255, cv2.THRESH_BINARY_INV)
	
	(th, im_bw) = cv2.threshold(im_bw, 240, 255, cv2.THRESH_BINARY_INV)	
	
	#points = punti dei muri
	points = []
	for y in xrange(0,im_bw.shape[1]):
		for x in xrange(im_bw.shape[0]):
			if im_bw[x, y] == (0):
				points.append([y,x])

	points = np.asarray(points)
	
	#distance map
	distanceMap = get_distance_transforme(im_bw)

	#medial axis sulla distance transform
	skel, distance = medial_axis(distanceMap, return_distance=True)
	
	#elimino parte delle imprecisioni della skeletonization
	#b3 = m.thin(skel, m.endpoints('homotopic'), 15)
	b3 = m.thin(skel, m.endpoints('homotopic'), 500)

	#---
	import copy
	b4 = copy.copy(b3)
	#ottengo solo critical points
	#critical_points = []
	for riga in xrange(b4.shape[0]):
		for col in xrange(b4.shape[1]):
			if b4[riga][col]==True:
				#controllo se in un intorno di quel punto c'è una frontiera
				#creo intorno del pixel 
				start_x = riga-17 #15
				end_x = riga+17
				start_y = col-17
				end_y = col+17
				count = 0
				for x in xrange(start_x,end_x):
					for y in xrange(start_y, end_y):
						if im_bw[x, y] <= (200): #se almeno una componente rgb di un pixel nell'introno del pixel cha fa parte del medial axis e' un pixel della frontiera
							count+=1
				if count <= 5:
					b4[riga][col]=False
				# else:
# 					#è un critical_points
# 					critical_points.append([riga, col])

	critical_points = []
	#salvo in una lista i critical points che fanno parte del medial axis
	for riga in xrange(b4.shape[0]):
		for col in xrange(b4.shape[1]):
			if (b4[riga][col]==True):
				critical_points.append((col,riga))
	critical_points = np.asarray(critical_points)
	flip_vertici(critical_points,b4.shape[0]-1)
	#------
	
	return distanceMap,points, b3, b4, critical_points