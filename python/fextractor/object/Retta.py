'''
Una retta e' l'oggetto sulla quale giace un muro. Quando diverse rette si incrociano formano delle superfici.

'''
from __future__ import division
import numpy as np
import math

class Retta(object):
	def __init__(self,punto,cluster_angolare,cluster_spaziale):
		self.punto = punto
		self.cluster_angolare = cluster_angolare
		self.cluster_spaziale = cluster_spaziale


#questo metodo secondo me si dovrebbe chiamare crea_retta
def crea_extended_lines(cluster_spaziali, lista_muri, xmin, ymin):
	'''
	crea una extended_line per ogni cluster spaziale. La retta avra' cluster spaziale e angolare = a cluster spaziale e angolare
	dei muri che la generano, e come punto avra' (mediana delle x dei punti medi, ymin) se e' verticale,
	(xmin, mediana delle y dei punti medi) se e' orizzontale, mediana dei punti medi se e' obliqua.
	'''  
	extended_lines = []
	for c in set(cluster_spaziali):
		mid_points = []
		angolazione = None
		for muro in lista_muri:
			if (muro.cluster_spaziale == c):
				if(angolazione==None):
					angolazione = muro.cluster_angolare
					#setto una sola volta, tanto tutti i muri con stesso cl_spaz hanno anche stesso cl_ang
				mid_x = (muro.x1+muro.x2)/2
				mid_y = (muro.y1+muro.y2)/2
				mid_point = np.array([mid_x,mid_y])
				mid_points.append(mid_point)
		#devo controllare se il cluster angolare e' orizzontale verticale o obliquo
		if (angolazione == 0): #orizzontale
			mid_points.sort(key=lambda x: (x[1], x[0])) #li metto in ordine per y
			indice = len(mid_points)//2
			punto = np.array([xmin,mid_points[indice][1]])	
		else:
			if (angolazione == math.radians(90)): #verticale
				mid_points.sort(key=lambda x: (x[0], x[1])) #li metto in ordine per x
				indice = len(mid_points)//2
				punto = np.array([mid_points[indice][0],ymin])
			else: #obliquo
				mid_points.sort(key=lambda x: (x[0], x[1])) #li metto in ordine per x
				indice = len(mid_points)//2
				punto = mid_points[indice]
		#for p in mid_points:
		#	print p
		#print punto
		#print ("\n")
		extended_lines.append(Retta(punto,angolazione,c))
	return extended_lines
'''
#creo la retta posizionando il punto su una media pesata tra tutti i cluster centers dei segmenti
def crea_extended_lines_su_media_pesata_punti(cluster_spaziali, lista_muri, xmin, ymin):

	extended_lines = []
	for c in set(cluster_spaziali):
		mid_points = []
		angolazione = None
		for muro in lista_muri:
			if (muro.cluster_spaziale == c):
				if(angolazione==None):
					angolazione = muro.cluster_angolare
					#setto una sola volta, tanto tutti i muri con stesso cl_spaz hanno anche stesso cl_ang
				mid_x = (muro.x1+muro.x2)/2
				mid_y = (muro.y1+muro.y2)/2
				mid_point = np.array([mid_x,mid_y])
				mid_points.append(mid_point)
		#devo controllare se il cluster angolare e' orizzontale verticale o obliquo
		if (angolazione == 0): #orizzontale
			# mid_points.sort(key=lambda x: (x[1], x[0])) #li metto in ordine per y
# 			indice = len(mid_points)//2
# 			punto = np.array([xmin,mid_points[indice][1]])	
			
			#sommo tutte le y e ne faccio la media pesata
			somma_y = 0
			for coord in mid_points:
				somma_y = somma_y + mid_points[1]
			media_y = somma_y / len(mid_points)
			punto = np.array([xmin,media_y])
		else:
			if (angolazione == math.radians(90)): #verticale
				# mid_points.sort(key=lambda x: (x[0], x[1])) #li metto in ordine per x
# 				indice = len(mid_points)//2
# 				punto = np.array([mid_points[indice][0],ymin])
				somma_x = 0
				for coord in mid_points:
					somma_x = somma_x + mid_points[0]
				media_x = somma_x / len(mid_points)
				punto = np.array([media_x,ymin])
			else: #obliquo
				mid_points.sort(key=lambda x: (x[0], x[1])) #li metto in ordine per x
				indice = len(mid_points)//2
				punto = mid_points[indice]
		#for p in mid_points:
		#	print p
		#print punto
		#print ("\n")
		extended_lines.append(Retta(punto,angolazione,c))
	return extended_lines

'''


