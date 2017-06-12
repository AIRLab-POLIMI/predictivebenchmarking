import cv2
from matplotlib import pyplot as plt
from skimage.feature import blob_dog
import math
import numpy as np
import matplotlib.cm as cmx
import matplotlib
import random
import collections
from shapely.geometry import Point
import copy

def trova_spazi_gt_da_frontiere(best_stanze_gt, lista_pixel_frontiere, immagine_cluster, labels):
	'''
	terzo metodo per riconoscere le stanze parziali, basato sul riconoscimento delle frontiere. Questo metodo controlla che all'interno dei pixel di una cella ci siano almeno il 30% di pixel dello stesso cluster per fare in modo che quella cella sia una cella parziale
	'''
	
	img_flipt= cv2.flip(immagine_cluster,0) #capire se va usato sempre
	#img_flipt = immagine_cluster.copy()
	counter=collections.Counter(labels)

	stanze_gt_con_frontiera = []
	ordinamento_frontiere = []
	for stanza_gt in best_stanze_gt:
			
		bordo = stanza_gt.bounds #restituisce una tupla del tipo (minx, miny, maxx, maxy)
		
		immagine_cella = img_flipt[bordo[1]:bordo[3], bordo[0]:bordo[2]]	
		
		altezza = len(immagine_cella)
		larghezza = len(immagine_cella[0])
		total_count_pixel = 0
		pixel_diversi = 0
		
		cluster = None
		prima_volta = True
		for i in xrange(0, altezza):
			for j in xrange( 0, larghezza):
				r = immagine_cella[i][j][0]
				g = immagine_cella[i][j][1]
				b = immagine_cella[i][j][2]
				total_count_pixel += 1
				if r!=g or r!=b or g!=b:#se ci sono componenti rgb diverse allora non sono in scala di grigio e quel pixel fa parte della frontiera
					pixel_diversi += 1
					
					
					if prima_volta == True: #suppongo che una cella non abbia parti sconosciute su lati diversi (cioe' che il cluster della frontiera sia solo uno)
						for pixel in lista_pixel_frontiere:
							if pixel.rgb[0]==r and pixel.rgb[1]==g and pixel.rgb[2]==b:
								cluster = pixel.cluster
								prima_volta = False
					
					
		n_elementi_cluster = counter[cluster]
		#print "il numero di n_elementi_cluster", n_elementi_cluster
		if pixel_diversi >= 0.3 * n_elementi_cluster and n_elementi_cluster > 0: #la copertura deve essere il 30% di quel cluster
		#if pixel_diversi >= 50: #elimino un po' di rumore
			#celletta.set_vedo_frontiera(True)
			#celletta.set_celletta_out(False)
			#celletta.set_celletta_parziale(True)
			stanze_gt_con_frontiera.append(stanza_gt)
			ordinamento_frontiere.append(cluster)
			
	return stanze_gt_con_frontiera, ordinamento_frontiere

def trova_spazi_gt_da_frontiere_versione_2(best_stanze_gt, lista_pixel_frontiere, immagine_cluster, labels):	
	'''
	seconda versione piu' accurata per vedere se una frontiera e' dentro una stanza GT
	
	'''
	#devo flippare le coordinate di lista_pixel_frontiere
	lista_pixel = [] #mi tengo una copia
	for p in lista_pixel_frontiere:
		a = copy.deepcopy(p)
		lista_pixel.append(a)
	
	for p in lista_pixel_frontiere:
		p.y = immagine_cluster.shape[0]-1 - p.y
	for p in lista_pixel_frontiere:
		altezza = len(immagine_cluster)
		y_p2 = - p.x+ altezza
		x_p2 = - p.y+ altezza
		p.x = x_p2
		p.y = y_p2
	
	counter=collections.Counter(labels)
	stanze_gt_con_frontiera = []
	ordinamento_frontiere = []
	
	for stanza_gt in best_stanze_gt:
		#conto il numero di pixel di una frontiera che stanno dentro a questa stanza GT
		num_pixel = 0
		cluster = None
		prima_volta = True
		c = []
		for pixel in lista_pixel_frontiere:
			posizione = Point(pixel.x,pixel.y)
			if posizione.distance(stanza_gt) == 0:
				#significa che quel pixel e' all'interno
				#print "ci entro????????? mai "
				num_pixel+=1
				c.append(pixel.cluster)#added
				if prima_volta == True:
					cluster = pixel.cluster
					prima_volta = False
		#print "-------------------<<<<<<<<<<<<", num_pixel	
			
		#--------aggiungo parte dove faccio media del cluster dominante #nel caso questa cosa va aggiunta anche dalle altre parti
		#TODO: questo pezzo l'ho aggiunto perhe' altrimenti potrebbero esserci dei problemi quando scelgo il cluster sulla stanza GT 
		#questa cosa la faccio anche con la ricerca delle stanze parziali, ma il discorso e' un po' diverso. verificare che non debba essere aggiunto anche li
		max = 0
		for elem in c:
			if c.count(elem) > max:
				max = c.count(elem)
				cluster = elem			
		#---------------------		
		
			
		n_elementi_cluster = counter[cluster]	
		if num_pixel >= 0.3 * n_elementi_cluster and n_elementi_cluster > 0: #la copertura deve essere il 30% di quel cluster
			stanze_gt_con_frontiera.append(stanza_gt)
			ordinamento_frontiere.append(cluster)
	
	del lista_pixel_frontiere
	#rifaccio tornare la lista come prima
	lista_pixel_frontiere = []
	for p in lista_pixel:
		lista_pixel_frontiere.append(p) 

		
	return stanze_gt_con_frontiera, ordinamento_frontiere, lista_pixel_frontiere
	

def scan_bordo(img_rgb):	
	#parametri molto buoni che sbagliano poco sono, soglia_minima_grigio = 120, soglia_massima_grigio = 180
	#faccio uno scan della mappa pixel per pixel in scala di grigio e sistemo i buchi per non avere problemi con il convexhull

	altezza = len(img_rgb)
	larghezza = len(img_rgb[0])
	
	#scansione verso il basso		
	for i in xrange( 0, larghezza):
		for j in xrange( 0, altezza-1):
			r = img_rgb[j][i][0]
			g = img_rgb[j][i][1]
			b = img_rgb[j][i][2]
			r1 = img_rgb[j+1][i][0]
			g1 = img_rgb[j+1][i][1]
			b1 = img_rgb[j+1][i][2]
			
			if r!=0 and g!=127 and b!=255:
				img_rgb[j][i][0] = 0
				img_rgb[j][i][1] = 0
				img_rgb[j][i][2] = 0
			if r1==0 and g1==127 and b1==255:
				img_rgb[j+1][i][0]=0
				img_rgb[j+1][i][1]=0
				img_rgb[j+1][i][2]=0
				break
			
				
	#scansione verso l'alto
	for i in xrange( 0, larghezza):
		for j in xrange( altezza-1, -1,-1):
			if img_rgb[j][i][0]!=0 and img_rgb[j][i][1]!=127 and img_rgb[j][i][2]!=255:
				img_rgb[j][i][0] = 0
				img_rgb[j][i][1] = 0
				img_rgb[j][i][2] = 0
			if img_rgb[j-1][i][0]==0 and img_rgb[j-1][i][1]==127 and img_rgb[j-1][i][2]==255:
				img_rgb[j-1][i][0]=0
				img_rgb[j-1][i][1]=0
				img_rgb[j-1][i][2]=0
				break	
	
	return img_rgb
	
	
def crea_bolla_su_frontiere(img, centro, circle_radius):
	'''
	estrae una bolla con centro il centro della frontiera e raggio, il raggio massimo dello scanner laser
	'''
	
	cv2.circle(img,centro, circle_radius, (0,127,255), 1, 8, 0)
	#result_array = img & mask
	result_array = img
	#devo controllare che non vada fuori dall'immagine
	y1 = centro[1] - circle_radius -5
	y2 = centro[1] + circle_radius+5
	x1 = centro[0] -5 - circle_radius
	x2 = centro[0]+5 + circle_radius
	if y1<0:
		y1 = 0
	if y2>len(img)-1:
		y2 = len(img)-1
	if x1 <0:
		x1 = 0
	if x2>len(img[0])-1:
		x2 = len(img[0])-1
	result_array = result_array[y1: y2, x1:x2, :]
	#result_array = result_array[centro[1] - circle_radius -5: centro[1] + circle_radius+5,centro[0] -5 - circle_radius:centro[0]+5 + circle_radius,:]

	img = scan_bordo(result_array)
	
	return result_array
	
	
def info_gain_bolla(img_rgb):
	'''
	restituisce il numero di pixel grigi che ci sono. Questi equivalgono all'ambiente che si potrebbe osservare da quella postazione.
	'''	
	area_pixel = 0	
	altezza = len(img_rgb)
	larghezza = len(img_rgb[0])
	
	#scansione verso il basso		
	for i in xrange( 0, larghezza):
		for j in xrange( 0, altezza-1):
			r = img_rgb[j][i][0]
			g = img_rgb[j][i][1]
			b = img_rgb[j][i][2]
			if r==205 and g==205 and b==205:
				area_pixel +=1
	
	return area_pixel
	