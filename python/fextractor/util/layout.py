'''
funzioni utili alla costruzione del layout delle stanze partendo da un immagine nota della mappa, dalla quale non si conosce nulla.
'''
import cv2
import warnings
warnings.warn("rinominare object")

from util import disegna as dsg
from util import mean_shift as ms
from util import rototranslation as rotot
from object import Segmento as sg
from object import Retta as rt
from object import Extended_segment as ext
from object import Superficie as fc #prima si chiamava cella
from object import Spazio as sp

import image as im
from shapely.geometry import Polygon
import math
import matrice as mtx
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation
from shapely.ops import cascaded_union
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import random
import numpy

from descartes import PolygonPatch



#secondo me in questa classe ci vuole un costruttore che contenga il contorno, la lista delle stanze, e tutto quello che mi serve.
def scan_bordo(img_rgb, soglia_minima_grigio = 120, soglia_massima_grigio = 180):
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
			if soglia_minima_grigio<=r<=soglia_massima_grigio and soglia_minima_grigio<=g<=soglia_massima_grigio and soglia_minima_grigio<=b<=soglia_massima_grigio and j!= altezza-1:
				if (r1>soglia_massima_grigio or g1>soglia_massima_grigio or b1>soglia_massima_grigio) :
					img_rgb[j+1][i][0] = 0
					img_rgb[j+1][i][1] = 0
					img_rgb[j+1][i][2] = 0

	#scansione verso l'alto
	for i in xrange( 0, larghezza):
		for j in xrange( altezza-1, -1,-1):
			if soglia_minima_grigio<=img_rgb[j][i][0]<=soglia_massima_grigio and soglia_minima_grigio<=img_rgb[j][i][1]<=soglia_massima_grigio and soglia_minima_grigio<=img_rgb[j][i][2]<=soglia_massima_grigio and j!=0:
				if (img_rgb[j-1][i][0]>soglia_massima_grigio or img_rgb[j-1][i][1]>soglia_massima_grigio or img_rgb[j-1][i][2]>soglia_massima_grigio):
					img_rgb[j-1][i][0] = 0
					img_rgb[j-1][i][1] = 0
					img_rgb[j-1][i][2] = 0


	#scansione verso destra
	for i in xrange(0, altezza ):
		for j in xrange(0, larghezza):
			if soglia_minima_grigio<=img_rgb[i][j][0]<=soglia_massima_grigio and soglia_minima_grigio<=img_rgb[i][j][1]<=soglia_massima_grigio and soglia_minima_grigio<=img_rgb[i][j][2]<=soglia_massima_grigio and j!= larghezza-1:
				if(img_rgb[i][j+1][0]>soglia_massima_grigio or img_rgb[i][j+1][1]>soglia_massima_grigio or img_rgb[i][j+1][2]>soglia_massima_grigio) :
					img_rgb[i][j+1][0] = 0
					img_rgb[i][j+1][1] = 0
					img_rgb[i][j+1][2] = 0


	#scansione verso sinistra
	for i in xrange( 0, altezza):
		for j in xrange( larghezza-1, -1,-1):
			if soglia_minima_grigio<=img_rgb[i][j][0]<=soglia_massima_grigio and soglia_minima_grigio<=img_rgb[i][j][1]<=soglia_massima_grigio and soglia_minima_grigio<=img_rgb[i][j][2]<=soglia_massima_grigio and j!= 0:
				if(img_rgb[i][j-1][0]>soglia_massima_grigio or img_rgb[i][j-1][1]>soglia_massima_grigio or img_rgb[i][j-1][2]>soglia_massima_grigio) :
					img_rgb[i][j-1][0] = 0
					img_rgb[i][j-1][1] = 0
					img_rgb[i][j-1][2] = 0

	return img_rgb

def get_layout(metricMap, minVal, maxVal, rho, theta, thresholdHough, minLineLength, maxLineGap, eps, minPts, h, minOffset, minLateralSeparation, apertureSize, t, m, filepath, cv2thresh=127, diagonali=True, metodo_classificazione_celle = True):
	'''
	Genera il layout delle stanze
	INPUT: mappa metrica, i parametri di canny, hough, mean-shift, dbscan, distanza per clustering spaziale.
	OUTPUT: la lista di poligoni shapely che costituiscono le stanze, la lista di cluster corrispondenti, la lista estremi che contiene [minx,maxx,miny,maxy] e la lista di colori.
	'''
	print filepath
	#leggo l'immagine originale in scala di grigio e la sistemo con il thresholding
	img_rgb = cv2.imread(metricMap)
	img_ini = img_rgb.copy() #copio l'immagine

	#scansione dei bordi
	#img_rgb = scan_bordo(img_rgb)

	# 127 per alcuni dati, 255 per altri
	ret,thresh1 = cv2.threshold(img_rgb,cv2thresh,255,cv2.THRESH_BINARY)

	#img_ini = thresh1.copy()


	#------------------CANNY E HOUGH PER TROVARE MURI-----------------------------------
	walls , canny = start_canny_ed_hough(thresh1,minVal,maxVal,rho,theta,thresholdHough,minLineLength,maxLineGap,apertureSize)


	#questo lo posso anche eliminare alla fine
	#----primo plot-->richiedo il disegno delle hough lines
	dsg.disegna_map(img_rgb,filepath = filepath )
	dsg.disegna_canny(canny,filepath = filepath)
	dsg.disegna_hough(img_rgb,walls,filepath = filepath)


	lines = flip_lines(walls, img_rgb.shape[0]-1)
	walls = crea_muri(lines)

	#anche questo lo posso eliminare
	#disegno i muri
	#----secondo plot --> disegna i muri corrispondenti ai segmenti individuati in precedenza
	#dsg.disegna_segmenti(walls)#solo un disegno poi lo elimino
	#-----------------------------------------------------------------------------------


	#------------SETTO XMIN YMIN XMAX YMAX DI walls-------------------------------------
	#tra tutti i punti dei muri trova l'ascissa e l'ordinata minima e massima.
	estremi = sg.trova_estremi(walls)
	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]
	offset = 20
	xmin -= offset
	xmax += offset
	ymin -= offset
	ymax += offset

	#-----------------------------------------------------------------------------------


	#---------------CONTORNO ESTERNO----------------------------------------------------
	(contours, vertici) = contorno_esterno(img_rgb, minVal, maxVal, xmin, xmax, ymin, ymax, apertureSize, t, m, metricMap,filepath)
	#-----------------------------------------------------------------------------------

	#---------------MEAN SHIFT PER TROVARE CLUSTER ANGOLARI-----------------------------
	(indici, walls, cluster_angolari) = cluster_ang(h, minOffset, walls, diagonali= diagonali) #probabilmente indici non serve veraente
	#-----------------------------------------------------------------------------------

	#---------------CLUSTER SPAZIALI----------------------------------------------------
	cluster_spaziali = cluster_spaz(minLateralSeparation, walls)
	#-----------------------------------------------------------------------------------

	#-------------------CREO EXTENDED_LINES---------------------------------------------
	(extended_lines, extended_segments) = extend_line(cluster_spaziali, walls, xmin, xmax, ymin, ymax,filepath)
	#-----------------------------------------------------------------------------------

	#-------------CREO GLI EDGES TRAMITE INTERSEZIONI TRA EXTENDED_LINES----------------
	edges = sg.crea_edges(extended_segments)
	#-----------------------------------------------------------------------------------

	#----------------------SETTO PESI DEGLI EDGES---------------------------------------
	#non so a cosa serva
	edges = sg.setPeso(edges, walls)
	#-----------------------------------------------------------------------------------

	#----------------CREO LE CELLE DAGLI EDGES------------------------------------------
	celle = fc.crea_celle(edges)
	#-----------------------------------------------------------------------------------

#----------------------------------problemi---------------------------------------------
	#TODO: questi due pezzi di codice hanno un problema, per ora non ho capito cosa. Ci sono gia' i metodi in fondo
	'''
	#questa non va

	#----------------CLASSIFICO CELLE---------------------------------------------------
	(celle, celle_out, celle_poligoni, indici, celle_parziali, contorno, centroid, punti) = classificazione_superfici(vertici, celle)
	#-----------------------------------------------------------------------------------

	#questo non va
	#--------------------------POLIGONI CELLE-------------------------------------------
	#TODO: questo medodo non e' di questa classe ma e' della classe Sapzio, in sostanza gli passi le celle e lui crea lo spazio che poi potro classificare come stanza o corridoio
	(celle_poligoni, out_poligoni, parz_poligoni) = crea_poligoni_da_celle(celle, celle_out, celle_parziali)
	#-----------------------------------------------------------------------------------
	'''

	#se voglio classifica le celle con il metodo di matteo metti TRUE, altrimenti se vuoi classificare con il metodo di Valerio con le percentuali metti False
	if metodo_classificazione_celle:
		print "sono entrato qui dentro hahahahahah"
		#----------------CLASSIFICO CELLE---------------------------------------------------
		#creo poligono del contorno
		contorno = Polygon(vertici)

		celle_poligoni = []
		indici = []
		celle_out = []
		celle_parziali = []
		for index,f in enumerate(celle):
			punti = []
			for b in f.bordi:
				punti.append([float(b.x1),float(b.y1)])
				punti.append([float(b.x2),float(b.y2)])
			#ottengo i vertici della cella senza ripetizioni
			punti = sort_and_deduplicate(punti)
			#ora li ordino in senso orario
			x = [p[0] for p in punti]
			y = [p[1] for p in punti]
			global centroid
			centroid = (sum(x) / len(punti), sum(y) / len(punti))
			punti.sort(key=algo)
			#dopo averli ordinati in senso orario, creo il poligono della cella.
			cella = Polygon(punti)
			#se il poligono della cella non interseca quello del contorno esterno della mappa, la cella e' fuori.
			if cella.intersects(contorno)==False:
				#indici.append(index)
				f.set_out(True)
				f.set_parziale(False)
				celle_out.append(f)
			#se il poligono della cella interseca il contorno esterno della mappa
			if (cella.intersects(contorno)):
				#se l'intersezione e' piu' grande di una soglia la cella e' interna
				if(cella.intersection(contorno).area >= cella.area/2):
					f.set_out(False)
				#altrimenti e' esterna
				else:
					f.set_out(True)
					f.set_parziale(False)
					celle_out.append(f)



		'''
		#le celle che non sono state messe come out, ma che sono adiacenti al bordo dell'immagine (hanno celle adiacenti < len(bordi)) sono per forza parziali
		a=0
		for f in celle:
			for f2 in celle:
				if (f!=f2) and (fc.adiacenti(f,f2)):
					a += 1
			if (a<len(f.bordi)):
				#print("ciao")
				if not (f.out):
					f.set_out(True)
					f.set_parziale(True)
					celle_parziali.append(f)
			a = 0

		#le celle adiacenti ad una cella out tramite un edge che pesa poco, sono parziali.
		a = 1
		while(a!=0):
			a = 0
			for f in celle:
				for f2 in celle:
					if (f!=f2) and (f.out==False) and (f2.out==True) and (fc.adiacenti(f,f2)):
						if(fc.edge_comune(f,f2)[0].weight < 0.2):
							f.set_out(True)
							f.set_parziale(True)
							celle_parziali.append(f)
							a = 1
		'''

		#tolgo dalle celle out le parziali
		celle_out = list(set(celle_out)-set(celle_parziali))
		#tolgo dalle celle quelle out e parziali
		celle = list(set(celle)-set(celle_out))
		celle = list(set(celle)-set(celle_parziali))
	else:
		print "uffffa ################################"
		#sto classificando le celle con il metodo delle percentuali
		(celle_out, celle, centroid, punti,celle_poligoni, indici, celle_parziali) = classifica_celle_con_percentuale(vertici, celle, img_ini)

	#--------------------------POLIGONI CELLE-------------------------------------------------

	#adesso creo i poligoni delle celle (celle = celle interne) e delle celle esterne e parziali

	#poligoni celle interne
	celle_poligoni = []
	for f in celle:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		celle_poligoni.append(cella)

	#poligoni celle esterne
	out_poligoni = []
	for f in celle_out:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		out_poligoni.append(cella)

	#poligoni celle parziali
	parz_poligoni = []
	for f in celle_parziali:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		parz_poligoni.append(cella)
#----------------------------fine problemi----------------------------------------------

	#------------------CREO LE MATRICI L, D, D^-1, ED M = D^-1 * L----------------------
	(matrice_l, matrice_d, matrice_d_inv, X) = crea_matrici(celle)
	#-----------------------------------------------------------------------------------

	#----------------DBSCAN PER TROVARE CELLE NELLA STESSA STANZA----------------------
	colori, fig, ax, clustersCelle = DB_scan(eps, minPts, X, celle, celle_poligoni, xmin, ymin, xmax, ymax, edges, contours,filepath)
	#-----------------------------------------------------------------------------------

	#------------------POLIGONI STANZE(spazio)------------------------------------------
	stanze, spazi = crea_spazio(clustersCelle, celle, celle_poligoni, colori, xmin, ymin, xmax, ymax, filepath)
	#-----------------------------------------------------------------------------------

	return  (stanze, clustersCelle, estremi, colori, spazi)



def start_canny_ed_hough(thresh1,minVal,maxVal,rho,theta,thresholdHough,minLineLength,maxLineGap,apertureSize):
#def start_canny_ed_hough(thresh1,parametri_obj):
	'''
	CANNY ED HOUGH per trovare i muri. e' un meccanismo di edge detection.
	OPENCV VERSION PROBLEMS
	'''
	#canny
	cannyEdges = cv2.Canny(thresh1,minVal,maxVal, apertureSize)
	#cannyEdges = cv2.Canny(thresh1,parametri_obj.minVal,parametri_obj.maxVal,apertureSize=parametri_obj.apertureSize)
	#hough
	#DIFF (se uso la prima riga ottengo un valore diverso rispetto alla seconda)
	#walls = cv2.HoughLinesP(cannyEdges,parametri_obj.rho,parametri_obj.theta,parametri_obj.thresholdHough,minLineLength=parametri_obj.minLineLength, maxLineGap = parametri_obj.maxLineGap)
	walls = cv2.HoughLinesP(cannyEdges,rho,theta,thresholdHough,minLineLength,maxLineGap)

	if cv2.__version__[0] == '3' :
		walls = [i[0]for i in walls]
	elif cv2.__version__[0] == '2' :
		walls = walls[0]
	else :
		raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*')
	return walls ,cannyEdges

def flip_lines(linee, altezza):
	'''
	flippa le y delle linee, perche' l'origine dei pixel e' in alto a sx, invece la voglio in basso a sx
	'''
	for l in linee:
		l[1] = altezza-l[1]
		l[3] = altezza-l[3]
	return linee

def flip_contorni(contours, altezza):
	'''
	flippa le y dei punti del contorno
	'''
	for c1 in contours:
		for c2 in c1:
			c2[0][1] = altezza - c2[0][1]
	return contours

def crea_muri(linee):
	'''
	trasforma le linee in oggetti di tipo Segmento, e ne restituisce la lista.
	'''
	walls = []
	for muro in linee:
		x1 = float(muro[0])
		y1 = float(muro[1])
		x2 = float(muro[2])
		y2 = float(muro[3])
		walls.append(sg.Segmento(x1,y1,x2,y2))
	return walls

def contorno_esterno(img_rgb, minVal, maxVal, xmin, xmax, ymin, ymax, apertureSize, t, m, metricMap,filepath):
#def contorno_esterno(img_rgb,parametri_obj, path_obj):

	#creo il contorno esterno facendo prima canny sulla mappa metrica.
	cannyEdges = cv2.Canny(img_rgb,minVal,maxVal,apertureSize)
	#t=1 #threshold di hough
	#m=20 #maxLineGap di hough
	hough_contorni, contours = im.trova_contorno(t,m,cannyEdges, metricMap)

	contours = flip_contorni(contours, img_rgb.shape[0]-1)

	#disegno contorno esterno
	#questo e' un grafico, lo posso anche eliminare, se non mi serve

	vertici = []
	for c1 in contours:
		for c2 in c1:
			vertici.append([float(c2[0][0]),float(c2[0][1])])

	#----terzo plot --> disegna il contorno esterno analizzando i vertici dell'immagine e le coordinate massime e minime
	#dsg.disegna_contorno(vertici,xmin,ymin,xmax,ymax,filepath = filepath)

	return (contours, vertici)

def contorno_esterno_versione_due(img_rgb):

	#imgray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
	#ret,thresh = cv2.threshold(imgray,127,255,0)


	gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
	gray = cv2.bilateralFilter(gray, 11, 17, 17)
	edged = cv2.Canny(gray, 30, 200)
	hough_contorni = cv2.HoughLines(edged,1,numpy.pi/180,threshold=2)[0]
	#dsg.disegna_canny(edged,savefig = False)
	# find contours in the edged image, keep only the largest
	# ones, and initialize our screen contour

	for x1,y1,x2,y2 in hough_contorni:
		cv2.line(bianca2,(x1,y1),(x2,y2),(0,0,0),2)
	ret,bianca = cv2.threshold(bianca2,253,255,cv2.THRESH_BINARY_INV)

	(cnts, _) = cv2.findContours(bianca.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10] #ottengo i dieci contorni piu' grandi
#	screenCnt = None

	# peri = cv2.arcLength(cnts[0], True)
# 	approx = cv2.approxPolyDP(cnts[0], 0.02 * peri, True)
# 	screenCnt = approx
#
# 	cv2.drawContours(img_rgb, [screenCnt], 0, (0, 255, 0), 3)
# 	cv2.imshow("Game Boy Screen", img_rgb)
# 	cv2.waitKey(5000)
#
	#max_len = 0
	# for c in cnts:
# 	# approximate the contour
# 		peri = cv2.arcLength(c, True)
# 		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
# 		if len(c) > max_len:
#  			max_len = len(c)
#  			screenCnt = approx


	#cv2.drawContours(img_rgb, [screenCnt], -1, (0, 255, 0), 3)
	#cv2.imshow("Game Boy Screen", img_rgb)
	#cv2.waitKey(0)

	contours = cnts
	contours = flip_contorni(contours, img_rgb.shape[0]-1)

	vertici = []
	for c1 in contours:
		print "\n"
		for c2 in c1:
			print c2
			vertici.append([float(c2[0][0]),float(c2[0][1])])


	plt.clf()
	plt.cla()
	plt.close()
	fig, ax = plt.subplots()
	plt.axis('equal')
	ax.axis('off')
	ax.set_xticks([])
	ax.set_yticks([])

	ascisse = []
	ordinate = []
	for c1 in contours:
		plt.clf()
		plt.cla()
		plt.close()
		fig, ax = plt.subplots()
		plt.axis('equal')
		ax.axis('off')
		ax.set_xticks([])
		ax.set_yticks([])
		for c2 in c1:
			ascisse.append(c2[0][0])
			ordinate.append(c2[0][1])
		ax.plot(ascisse,ordinate,color='0.8',linewidth=3.0)
		del ascisse[:]
		del ordinate[:]
		plt.show()

	return (contours, vertici)

def contorno_esterno_versione_tre(img_rgb):

	#faccio diventare tutto cio che e' bianco nero, quindi tutto cio' che era grigio diventa bianco
	imgray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,253,255,cv2.THRESH_BINARY_INV)
	contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# max_area = cv2.contourArea(contours[0])
# 	contorno_max = contours[0]
# 	for c in contours:
# 		if cv2.contourArea(c) > max_area:
# 			max_area = cv2.contourArea(c)
# 			contorno_max = c
	contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
	contorno_max = contours[1]
	peri = cv2.arcLength(contorno_max, True)
	approx = cv2.approxPolyDP(contorno_max, 0.0002 * peri, True)
	screenCnt = approx


	# cv2.drawContours(img_rgb, [screenCnt], 0, (0, 255, 0), 3)
# 	cv2.imshow("prova", img_rgb)
# 	cv2.waitKey(1000)
#
# 	print "ahdfaidf",len(contours)
#
#
#
# 	dsg.disegna_map(thresh,savefig = False)

	#contours = flip_contorni(contours, img_rgb.shape[0]-1)

	# vertici = []
# 	for c1 in contours:
# 		for c2 in c1:
# 			vertici.append([float(c2[0][0]),float(c2[0][1])])

	#flippo il contorno
	for c in screenCnt:
		c[0][1] = img_rgb.shape[0]-1 - c[0][1]

	vertici = []
	for c in screenCnt:
		vertici.append([float(c[0][0]),float(c[0][1])])

	# print contorno_max
# 	print screenCnt
# 	print len(contorno_max)
# 	print len(screenCnt)

	return screenCnt, vertici


def cluster_ang(h, minOffset, walls, num_min = 3, lunghezza_min = 3, diagonali= True):
	'''
	crea i cluster angolari
	'''

	#creo i cluster centers tramite mean shift
	cluster_centers = ms.mean_shift(h, minOffset, walls)

	#ci sono dei cluster angolari che sono causati da pochi e piccoli line_segments, che sono solamente rumore. Questi cluster li elimino dalla lista cluster_centers ed elimino anche i rispettivi segmenti dalla walls.
	indici = ms.indici_da_eliminare(num_min, lunghezza_min, cluster_centers, walls, diagonali)

	#ora che ho gli indici di clusters angolari e di muri da eliminare, elimino da walls e cluster_centers, partendo dagli indici piu alti
	for i in sorted(indici, reverse=True):
		del walls[i]
		del cluster_centers[i]

	#ci sono dei cluster che si somigliano ma non combaciano per una differenza infinitesima, e non ho trovato parametri del mean shift che rendano il clustering piu' accurato di cosi', quindi faccio una media normalissima, tanto la differenza e' insignificante.
	unito = ms.unisci_cluster_simili(cluster_centers)
	while(unito):
		unito = ms.unisci_cluster_simili(cluster_centers)

	#assegno i cluster ai muri di walls
	walls = sg.assegna_cluster_angolare(walls, cluster_centers)

	#creo lista di cluster_angolari
	cluster_angolari = []
	for muro in walls:
		cluster_angolari.append(muro.cluster_angolare)

	return (indici, walls, cluster_angolari)

def cluster_spaz(minLateralSeparation, walls):
	'''
	crea i cluester spaziali
	'''
	#setto i cluster spaziali a tutti i muri di walls
	walls = sg.spatialClustering(minLateralSeparation, walls)

	#creo lista di cluster spaziali
	cluster_spaziali = []
	for muro in walls:
		cluster_spaziali.append(muro.cluster_spaziale)

	#disegno cluster spaziali(posso anche eliminarlo, a me non servono tanto i disegni)
	#---- quarto plot --> disegno i cluster spaziali relativi ai segmenti
	#dsg.disegna_cluster_spaziali(cluster_spaziali, walls,filepath = filepath)

	return cluster_spaziali

def extend_line(cluster_spaziali, walls, xmin, xmax, ymin, ymax,filepath='.'):
	'''
	crea le extended line
	'''
	extended_lines = rt.crea_extended_lines(cluster_spaziali, walls, xmin, ymin)



	#da qui serve per disegnarle
	#extended_lines (credo parli delle rette) hanno un punto, un cluster_angolare ed un cluster_spaziale, per disegnarle pero' mi servono 2 punti. Creo lista di segmenti
	extended_segments = ext.crea_extended_segments(xmin,xmax,ymin,ymax, extended_lines)

	#----quinto plot --> disegno la mappa come era in partenza(con le linee) e ci aggiungo le rette.
	#disegno le extended_lines in rosso e la mappa in nero
	#dsg.disegna_extended_segments(extended_segments, walls,filepath = filepath)

	return (extended_lines, extended_segments)

def classificazione_superfici(vertici, celle):
	'''
	classificazione delle celle(superfici) che sono state individuate dai segmenti estesi
	'''
	contorno = Polygon(vertici)
	#aggiungo un buffer per far pulire il contorno
	contorno = contorno.buffer(0)#mio. aggiunto da me per pulire il contorno che ha dei self_interserctin, splitto il poligono e lo faccio diventare un MULTIPOLYGON

	celle_poligoni = []
	indici = []
	celle_out = []
	celle_parziali = []
	celle_par = []#mio
	for index,f in enumerate(celle):
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		#ottengo i vertici della cella senza ripetizioni
		punti = sort_and_deduplicate(punti)
		#ora li ordino in senso orario
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		#dopo averli ordinati in senso orario, creo il poligono della cella.
		cella = Polygon(punti)
		#se il poligono della cella non interseca quello del contorno esterno della mappa, la cella e' fuori.
		if cella.intersects(contorno)==False:
			#indici.append(index)
			f.set_out(True)
			f.set_parziale(False)
			celle_out.append(f)
		#se il poligono della cella interseca il contorno esterno della mappa
		if (cella.intersects(contorno)):
			#se l'intersezione e' piu' grande di una soglia la cella e' interna
			# print "vediamo se sono validi"
# 			print "contorno", contorno.is_valid
# 			print "cella", cella.is_valid
			if(cella.intersection(contorno).area >= cella.area/5): #era 5 #TODO: fai diventare la divisione per 6 della cella un parametro, inizialmente era 2
				f.set_out(False)
				#f.set_parziale(True)#mio aggiunto io
			#altrimenti e' esterna
			else:
				f.set_out(True)
				f.set_parziale(False)
				celle_out.append(f)

	'''
	#le celle che non sono state messe come out, ma che sono adiacenti al bordo dell'immagine (hanno celle adiacenti < len(bordi)) sono per forza parziali
	a=0
	for f in celle:
		for f2 in celle:
			if (f!=f2) and (fc.adiacenti(f,f2)):
				a += 1
		if (a<len(f.bordi)):
			#print("ciao")
			if not (f.out):
				f.set_out(False) #se una cella e' parziale, non e' out per me. lui aveva messo True
				f.set_parziale(True)
				celle_parziali.append(f)
		a = 0

	#le celle adiacenti ad una cella out tramite un edge che pesa poco, sono parziali.
	a = 1
	while(a!=0):
		a = 0
		for f in celle:
			for f2 in celle:
				if (f!=f2) and (f.out==False) and (f2.out==True) and (fc.adiacenti(f,f2)):
					if(fc.edge_comune(f,f2)[0].weight < 0.2):
						f.set_out(True)
						f.set_parziale(True)
						celle_parziali.append(f)
						a = 1

	'''
	#tolgo dalle celle out le parziali
	celle_out = list(set(celle_out)-set(celle_parziali))
	#tolgo dalle celle quelle out e parziali
	celle = list(set(celle)-set(celle_out))
	celle = list(set(celle)-set(celle_parziali)) #per ora non tolgo dalle celle quelle parziali

	return (celle, celle_out, celle_poligoni, indici, celle_parziali, contorno, centroid, punti)

def algo(p):
	'''
	riordina i punti in senso orario
	'''
	return (math.atan2(p[0] - centroid[0], p[1] - centroid[1]) + 2 * math.pi) % (2*math.pi)

def sort_and_deduplicate(l):
	'''
elimina i doppioni da una lista di coppie
	'''
	return list(uniq(sorted(l, reverse=True)))

def uniq(lst):
	last = object()
	for item in lst:
		if item == last:
			continue
		yield item
		last = item

def crea_poligoni_da_celle(celle, celle_out, celle_parziali):
	'''
	crea i poligoni a partire dalle celle classificate, e' equivalente all'oggetto Spazio(non ancora creato), infatti appena riesci sposta questo metodo in quella classe.
	'''
	#adesso creo i poligoni delle celle (celle = celle interne) e delle celle esterne e parziali

	#poligoni celle interne
	celle_poligoni = []
	for f in celle:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		celle_poligoni.append(cella)

	#poligoni celle esterne
	out_poligoni = []
	for f in celle_out:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		out_poligoni.append(cella)

	#poligoni celle parziali
	parz_poligoni = []
	for f in celle_parziali:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		parz_poligoni.append(cella)

	return (celle_poligoni, out_poligoni, parz_poligoni, centroid)

def crea_matrici(celle,sigma=0.00000125,val=0): #prima sigma era 0.1


	matrice_l = mtx.crea_matrice_l(celle, sigma, val)

	matrice_d = mtx.crea_matrice_d(matrice_l)

	matrice_d_inv = matrice_d.getI()

	matrice_m = matrice_d_inv.dot(matrice_l)
	matrice_m = mtx.simmetrizza(matrice_m)

	X = 1-matrice_m

	return (matrice_l, matrice_d, matrice_d_inv, X)

def DB_scan(eps, minPts, X, celle, celle_poligoni, xmin, ymin, xmax, ymax, edges, contours,filepath):
#def DB_scan(eps, minPts, X, celle_poligoni):
	clustersCelle = []
	clustersCelle = clustering_dbscan_celle(eps, minPts, X)

	#---- sesto plot --> disegno la mappa con le diverse celle classificate.
	colori, fig, ax = dsg.disegna_dbscan(clustersCelle, celle, celle_poligoni, xmin, ymin, xmax, ymax, edges, contours,filepath = filepath)
	'''
	#se lo voglio usare devo andare a commentare in disegna.py in disegna_dbscan lo #show() alla fine del metodo
	#plotto le celle parziali
	for f_poly in parz_poligoni:
		f_patch = PolygonPatch(f_poly,fc='#d3d3d3',ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
		ax.text(f_poly.representative_point().x,f_poly.representative_point().y,str("parz"),fontsize=8)
	plt.show()
	'''


	return colori, fig, ax, clustersCelle
	#return clustersCelle

def clustering_dbscan_celle(eps, min_samples, X):
	'''
	esegue il dbscan clustering sulle celle, prendendo in ingresso eps (massima distanza tra 2 campioni per essere considerati nello stesso neighborhood), min_samples (numero di campioni in un neighborhood per un punto per essere considerato un core point) e X (1-matrice di affinita' locale tra le celle).
	'''
	af = DBSCAN(eps, min_samples, metric="precomputed").fit(X)

	#print("num of clusters = ")
	#print len(set(af.labels_))
	return af.labels_

def crea_spazio(clustersCelle, celle, celle_poligoni, colori, xmin, ymin, xmax, ymax,filepath = '.'):
	'''
	questo e' un metodo che andrebbe inserito nella classe Spazio, vedi se ha senso farlo
	'''
	#creo i poligoni delle stanze (unione dei poligoni delle celle con stesso cluster).
	stanze = []
	spazi = []
	stanze, spazi = unisciCelle(clustersCelle, celle, celle_poligoni, False)

	#---- settimo plot --> serve a disegnare il plot della mappa con le stanze separate.
	#disegno layout stanze.
	#dsg.disegna_stanze(stanze, colori, xmin, ymin, xmax, ymax,filepath = filepath)

	return stanze, spazi

def unisciCelle(clusters, celle, celle_poligoni, False):
	'''
	i poligoni delle celle dello stesso cluster vengono uniti in un unico poligono, che e' il poligono della stanza.
	'''

	#gli spazi sono la stessa cosa delle stanze ma in realta' ho creato un oggetto spazio
	stanze = []
	spazi = []

	for l in set(clusters):
		poligoni = []
		celle_corrispondenti = []
		for index,cluster in enumerate(clusters):
			if (l == cluster) and not (celle[index].out):
				poligoni.append(celle_poligoni[index])
				celle_corrispondenti.append(celle[index])#mio aggiunto per (oggetto Spazio)
		stanza = cascaded_union(poligoni)
		stanze.append(stanza)

		spazio = sp.Spazio(poligoni, stanza,celle_corrispondenti, index)#mio(oggetto Spazio)
		spazi.append(spazio) #mio


	return stanze, spazi



def get_layout_parziale(metricMap, minVal, maxVal, rho, theta, thresholdHough, minLineLength, maxLineGap, eps, minPts, h, minOffset, minLateralSeparation, diagonali=True):
	'''
prende in input la mappa metrica, i parametri di canny, hough, mean-shift, dbscan, distanza per clustering spaziale. Genera il layout delle stanze e ritorna la lista di poligoni shapely che costituiscono le stanze, la lista di cluster corrispondenti, la lista estremi che contiene [minx,maxx,miny,maxy] e la lista di colori.
	'''

	img_rgb = cv2.imread(metricMap)
	ret,thresh1 = cv2.threshold(img_rgb,127,255,cv2.THRESH_BINARY)


	#------------------CANNY E HOUGH PER TROVARE MURI----------------------------------

	#canny
	cannyEdges = cv2.Canny(thresh1,minVal,maxVal,apertureSize = 5)
	#hough
	walls = cv2.HoughLinesP(cannyEdges,rho,theta,thresholdHough,minLineLength,maxLineGap)

	if cv2.__version__[0] == '3' :
		walls = [i[0]for i in walls]
	elif cv2.__version__[0] == '2' :
		walls = walls[0]
	else :
		raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*')

	dsg.disegna_hough(img_rgb,walls)

	lines = flip_lines(walls, img_rgb.shape[0]-1)

	walls = crea_muri(lines)

	#disegno i muri
	sg.disegna_segmenti(walls)


	#------------SETTO XMIN YMIN XMAX YMAX DI walls--------------------------------------------

	#tra tutti i punti dei muri trova l'ascissa e l'ordinata minima e massima.
	estremi = sg.trova_estremi(walls)
	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]
	offset = 20
	xmin -= offset
	xmax += offset
	ymin -= offset
	ymax += offset


	#---------------CONTORNO ESTERNO-------------------------------------------------------

	#creo il contorno esterno facendo prima canny sulla mappa metrica.
	cannyEdges = cv2.Canny(img_rgb,minVal,maxVal,apertureSize = 5)
	t=1 #threshold di hough
	m=21 #maxLineGap di hough
	hough_contorni, contours = im.trova_contorno(t,m,cannyEdges, metricMap)

	#dsg.disegna_hough(cannyEdges, hough_contorni)

	contours = flip_contorni(contours, img_rgb.shape[0]-1)

	#disegno contorno esterno
	vertici = []
	for c1 in contours:
		for c2 in c1:
			vertici.append([float(c2[0][0]),float(c2[0][1])])
	dsg.disegna_contorno(vertici,xmin,ymin,xmax,ymax)


	#-------------------MEAN SHIFT PER TROVARE CLUSTER ANGOLARI---------------------------------------

	#creo i cluster centers tramite mean shift
	cluster_centers = ms.mean_shift(h, minOffset, walls)


	#ci sono dei cluster angolari che sono causati da pochi e piccoli line_segments, che sono solamente rumore. Questi cluster li elimino dalla lista cluster_centers ed elimino anche i rispettivi segmenti dalla walls.
	num_min = 3
	lunghezza_min = 3
	indici = ms.indici_da_eliminare(num_min, lunghezza_min, cluster_centers, walls, diagonali)


	#ora che ho gli indici di clusters angolari e di muri da eliminare, elimino da walls e cluster_centers, partendo dagli indici piu alti
	for i in sorted(indici, reverse=True):
		del walls[i]
		del cluster_centers[i]


	#ci son dei cluster che si somigliano ma non combaciano per una differenza infinitesima, e non ho trovato parametri del mean shift che rendano il clustering piu' accurato di cosi', quindi faccio una media normalissima, tanto la differenza e' insignificante.
	unito = ms.unisci_cluster_simili(cluster_centers)
	while(unito):
		unito = ms.unisci_cluster_simili(cluster_centers)


	#assegno i cluster ai muri di walls
	walls = sg.assegna_cluster_angolare(walls, cluster_centers)


	#creo lista di cluster_angolari
	cluster_angolari = []
	for muro in walls:
		cluster_angolari.append(muro.cluster_angolare)


	#---------------CLUSTER SPAZIALI--------------------------------------------------------------------

	#setto i cluster spaziali a tutti i muri di walls
	walls = sg.spatialClustering(minLateralSeparation, walls)

	#disegno i cluster angolari
	#sg.disegna_cluster_angolari(cluster_centers, walls, cluster_angolari)

	#creo lista di cluster spaziali
	cluster_spaziali = []
	for muro in walls:
		cluster_spaziali.append(muro.cluster_spaziale)

	#disegno cluster spaziali
	sg.disegna_cluster_spaziali(cluster_spaziali, walls)


	#-------------------CREO EXTENDED_LINES---------------------------------------------------------

	extended_lines = rt.crea_extended_lines(cluster_spaziali, walls, xmin, ymin)


	#extended_lines hanno punto, cluster_angolare e cluster_spaziale, per disegnarle pero' mi servono 2 punti. Creo lista di segmenti
	extended_segments = ext.crea_extended_segments(xmin,xmax,ymin,ymax, extended_lines)


	#disegno le extended_lines in rosso e la mappa in nero
	ext.disegna_extended_segments(extended_segments, walls)


	#-------------CREO GLI EDGES TRAMITE INTERSEZIONI TRA EXTENDED_LINES-------------------------------

	edges = sg.crea_edges(extended_segments)

	#sg.disegna_segmenti(edges)


	#----------------------SETTO PESI DEGLI EDGES------------------------------------------------------

	edges = sg.setPeso(edges, walls)

	#sg.disegna_pesanti(edges, peso_min)


	#----------------CREO LE CELLE DAGLI EDGES----------------------------------------------------------

	print("creando le celle")

	celle = fc.crea_celle(edges)

	print("celle create")

	#fc.disegna_celle(celle)


	#----------------CLASSIFICO CELLE----------------------------------------------

	#creo poligono del contorno
	contorno = Polygon(vertici)

	celle_poligoni = []
	indici = []
	celle_out = []
	celle_parziali = []
	for index,f in enumerate(celle):
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		#ottengo i vertici della cella senza ripetizioni
		punti = sort_and_deduplicate(punti)
		#ora li ordino in senso orario
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		#dopo averli ordinati in senso orario, creo il poligono della cella.
		cella = Polygon(punti)
		#se il poligono della cella non interseca quello del contorno esterno della mappa, la cella e' fuori.
		if cella.intersects(contorno)==False:
			#indici.append(index)
			f.set_out(True)
			f.set_parziale(False)
			celle_out.append(f)
		#se il poligono della cella interseca il contorno esterno della mappa
		if (cella.intersects(contorno)):
			#se l'intersezione e' piu' grande di una soglia la cella e' interna
			if(cella.intersection(contorno).area >= cella.area/2):
				f.set_out(False)
			#altrimenti e' esterna
			else:
				f.set_out(True)
				f.set_parziale(False)
				celle_out.append(f)

	#le celle che non sono state messe come out, ma che sono adiacenti al bordo dell'immagine (hanno celle adiacenti < len(bordi)) sono per forza parziali
	a=0
	for f in celle:
		for f2 in celle:
			if (f!=f2) and (fc.adiacenti(f,f2)):
				a += 1
		if (a<len(f.bordi)):
			#print("ciao")
			if not (f.out):
				f.set_out(True)
				f.set_parziale(True)
				celle_parziali.append(f)
		a = 0

	#le celle adiacenti ad una cella out tramite un edge che pesa poco, sono parziali.
	a = 1
	while(a!=0):
		a = 0
		for f in celle:
			for f2 in celle:
				if (f!=f2) and (f.out==False) and (f2.out==True) and (fc.adiacenti(f,f2)):
					if(fc.edge_comune(f,f2)[0].weight < 0.1):  #qua nella funzione normale c'e' 0.2
						f.set_out(True)
						f.set_parziale(True)
						celle_parziali.append(f)
						a = 1


	#tolgo dalle celle out le parziali
	celle_out = list(set(celle_out)-set(celle_parziali))
	#tolgo dalle celle quelle out e parziali
	celle = list(set(celle)-set(celle_out))
	celle = list(set(celle)-set(celle_parziali))


	#--------------------------POLIGONI CELLE-------------------------------------------------

	#adesso creo i poligoni delle celle (celle = celle interne) e delle celle esterne e parziali

	#poligoni celle interne
	celle_poligoni = []
	for f in celle:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		celle_poligoni.append(cella)

	#poligoni celle esterne
	out_poligoni = []
	for f in celle_out:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		out_poligoni.append(cella)

	#poligoni celle parziali
	parz_poligoni = []
	for f in celle_parziali:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		parz_poligoni.append(cella)



	#------------------CREO LE MATRICI L, D, D^-1, ED M = D^-1 * L---------------------------------------

	sigma = 0.1
	val = 0
	matrice_l = mtx.crea_matrice_l(celle, sigma, val)

	matrice_d = mtx.crea_matrice_d(matrice_l)

	matrice_d_inv = matrice_d.getI()

	matrice_m = matrice_d_inv.dot(matrice_l)
	matrice_m = mtx.simmetrizza(matrice_m)

	X = 1-matrice_m


	#----------------DBSCAN PER TROVARE CELLE NELLA STESSA STANZA-----------------------------------------

	clustersCelle = []
	clustersCelle = clustering_dbscan_celle(eps, minPts, X)


	colori, fig, ax = dsg.disegna_dbscan(clustersCelle, celle, celle_poligoni, xmin, ymin, xmax, ymax, edges, contours)
	'''
	#plotto le celle esterne
	for f_poly in out_poligoni:
		f_patch = PolygonPatch(f_poly,fc='#ffffff',ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
		ax.text(f_poly.representative_point().x,f_poly.representative_point().y,str("out"),fontsize=8)
	'''

	#plotto le celle parziali
	for f_poly in parz_poligoni:
		f_patch = PolygonPatch(f_poly,fc='#d3d3d3',ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
		ax.text(f_poly.representative_point().x,f_poly.representative_point().y,str("parz"),fontsize=8)
	plt.show()


	#------------------POLIGONI STANZE-------------------------------------------------------------------

	#creo i poligoni delle stanze (unione dei poligoni delle celle con stesso cluster).
	stanze = []
	stanze = unisciCelle(clustersCelle, celle, celle_poligoni, False)

	#disegno layout stanze.
	fig, ax = dsg.disegna_stanze(stanze, colori, xmin, ymin, xmax, ymax)
	#plotto le celle parziali, questo per funzionare ha bisogno che si commenti riga 127 di disegna.py (#plt.show()).

	for f_poly in parz_poligoni:
		f_patch = PolygonPatch(f_poly,fc='#d3d3d3',ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
	plt.show()

	return (stanze, clustersCelle, estremi, colori)

def classifica_celle_con_percentuale(vertici, celle, img_ini):
	#----------------CLASSIFICO CELLE---------------------------------------------------
	#creo poligono del contorno
	contorno = Polygon(vertici)

	#secondo me tutta sta roba la si puo' elimminare dato che tanto dopo si fanno le stesse cose
	#TODO guarda se si puo' unire il pezzo dopo con questo.
	celle_poligoni = []
	indici = []
	celle_out = []
	celle_parziali = []
	for index,f in enumerate(celle):
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		#ottengo i vertici della cella senza ripetizioni
		punti = sort_and_deduplicate(punti)
		#ora li ordino in senso orario
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		#TODO:dopo averli ordinati in senso orario, creo il poligono della cella.#VALERIO: a me sembrano salvato in senso antiorario, ho provato a printarlo ed effetivamente prima erano in senso orario e poi in senso antiorario
		cella = Polygon(punti)
		#se il poligono della cella non interseca quello del contorno esterno della mappa, la cella e' fuori.

		#VALERIO:tento di classificare le celle out che pero' stanno all'interno del convexHull, come out.
		#idea: prendo la posizione di tutte le celle rimaste e controllo che all'interno della mappa originaria non ci siano parti grigie.

		bordo = cella.bounds #restituisce una tupla del tipo (minx, miny, maxx, maxy)

		#bordo[1]:bordo[3], bordo[0]:bordo[2]
		#il problema principale in questo punto e' che ci sono ancora le righe rosse e non so il perche'
		#plt.close("all")

		#TODO: problema risolto, non so perche' ma l'immagine era capovolta, quindi andavo a prendere celle strane
		#-------flippo immagine, penso sia quello il problema principale
		#plt.imshow(img_ini)
		#plt.show()

		img_flipt= cv2.flip(img_ini,0)#questo secondo me lo devo solo fare con le mappe del survey
		#plt.imshow(img_flipt)
		#plt.show()

		#se sono sul quadrante in alto a destra
		if bordo[1]>=0 and bordo[0]>=0:
			immagine_cella = img_flipt[bordo[1]:bordo[3], bordo[0]:bordo[2]]
			#plt.imshow(immagine_cella)
			#plt.show()
			altezza = len(immagine_cella)
			larghezza = len(immagine_cella[0])
			total_count_pixel = 0
			pixel_bianco = 0
			pixel_grigio = 0
			pixel_nero = 0
			for i in xrange(0, altezza):
				for j in xrange( 0, larghezza):
					r = immagine_cella[i][j][0]
					g = immagine_cella[i][j][1]
					b = immagine_cella[i][j][2]
					total_count_pixel += 1
					if (r<=210 and g<=210 and b<=210)and(r>=70 and g>=70 and b>=70):
						pixel_grigio += 1
					elif r<70 and g<70 and b<70:
						pixel_nero += 1
					else:
						pixel_bianco += 1

			if total_count_pixel != 0:
				percentuale_bianco = (float(pixel_bianco)/float(total_count_pixel))
				percentuale_grigio = (float(pixel_grigio)/float(total_count_pixel))
				percentuale_nero =  (float(pixel_nero)/float(total_count_pixel))

				if percentuale_grigio >=0.3:
					f.set_out(True)
					celle_out.append(f)

				elif percentuale_bianco <= 0.5:
					f.set_out(True)
					celle_out.append(f)
				else:
					f.set_out(False)

			else:
				f.set_out(True)
				celle_out.append(f)
		else:
			#TODO: capire perche'. Non ne conosco il motivo ma ci sono delle parti sotto il primo quadrante
			f.set_out(True)
			celle_out.append(f)





	'''
	#le celle che non sono state messe come out, ma che sono adiacenti al bordo dell'immagine (hanno celle adiacenti < len(bordi)) sono per forza parziali
	a=0
	for f in celle:
		for f2 in celle:
			if (f!=f2) and (fc.adiacenti(f,f2)):
				a += 1
		if (a<len(f.bordi)):
			#print("ciao")
			if not (f.out):
				f.set_out(True)
				f.set_parziale(True)
				celle_parziali.append(f)
		a = 0

	#le celle adiacenti ad una cella out tramite un edge che pesa poco, sono parziali.
	a = 1
	while(a!=0):
		a = 0
		for f in celle:
			for f2 in celle:
				if (f!=f2) and (f.out==False) and (f2.out==True) and (fc.adiacenti(f,f2)):
					if(fc.edge_comune(f,f2)[0].weight < 0.2):
						f.set_out(True)
						f.set_parziale(True)
						celle_parziali.append(f)
						a = 1
	'''

	#tolgo dalle celle out le parziali
	celle_out = list(set(celle_out)-set(celle_parziali))
	#tolgo dalle celle quelle out e parziali
	celle = list(set(celle)-set(celle_out))
	celle = list(set(celle)-set(celle_parziali))


	return celle_out, celle, centroid, punti,celle_poligoni, indici, celle_parziali


# def elimina_celle_insensate(celle_poligoni, celle, parametri_obj):
# 	'''
# 	questo mi permette di eliminare tutte le celle che sono il risultato di muri troppo spessi e che quindi non rispecchiano veramente una stanza
#
# 	'''
# 	for cella in celle_poligoni:
# 		bordo = cella.bounds #restituisce una tupla del tipo (minx, miny, maxx, maxy)
# 		latoX = bordo[2]-bordo[0]
# 		latoY = bordo[3]-bordo[1]
#
# 		latoMax = max(latoX,latoY)
# 		latoMin = min(latoX,latoY)
#
# 		proporzione = latoMin/latoMax
#
# 		#elimino celle che hanno un lato molto piccolo
# 		if latoMin < parametri_obj.minimaLunghezzaParete:
# 			#index = clusterCelle.index(cella)
# 			print index
# 			print latoX
# 			print latoY
# 			print latoMin
# 			clusterCelle_inutili.append(cella)
# 			celle_inutili.append(celle[index])
# 			# del celle[index]
# 			celle_poligoni.remove(cella)
# 		index+=1
#
#
# 	celle = list(set(celle)-set(celle_inutili))
# 	clusterCelle = list(set(clusterCelle)- set(clusterCelle_inutili))
# 	return clusterCelle, celle
#
def get_stanze_reali(stanze, stanze_non_collegate, colori):

	stanze_reali = list(stanze)
	colori_da_eliminare = []
	#colleziono i colori da eliminare
	for stanza_no in stanze_non_collegate:
		indice_colore = stanze.index(stanza_no)
		colori_da_eliminare.append(colori[indice_colore])

	#elimino la stanza non collegate
	for stanza_no in stanze_non_collegate:
		stanze_reali.remove(stanza_no) #rimuovo dalla lista delle stanze tutte quelle che non hanno ragione di esistere, poiche' non collegate

	#prima pero' devo togliere dei colori dalla lista dei colori
	colori_reali = list(colori)
	for c in colori_da_eliminare:
		colori_reali.remove(c)


	return stanze_reali, colori_reali


def get_distance_matrix(walls, minLateralSeparation= 7):
	'''
	calcola la matrice delle distanze tra tutti i segmenti
	'''

	#questo per metodo di classicazione=2
	matrix = []
	min=0
	for segmento1 in walls:
		row= []
		for segmento2 in walls:
			min = sg.segments_distance(segmento1.x1, segmento1.y1, segmento1.x2, segmento1.y2, segmento2.x1, segmento2.y1, segmento2.x2, segmento2.y2)
			#if segmento1.cluster_angolare == segmento2.cluster_angolare and min <= minLateralSeparation :
			row.append(min)
			# if min > minLateralSeparation:
# 				min = 9999
# 				row.append(min)
# 			else:
# 				row.append(min)
#

		matrix.append(row)

	return matrix

def compute_clustering(matrix):
	'''
	hierarchical clustering
	'''
	#af = AgglomerativeClustering(n_clusters=n_clusters , affinity ='precomputed', linkage='average').fit(matrix)
	#af = AffinityPropagation(damping=0.5,affinity='precomputed').fit(matrix)
	af = DBSCAN(eps=7, min_samples= 2, metric="precomputed").fit(matrix) #eps=10
	return af.labels_

def compute_affinity_propagation(matrix):

	#normalizzo matrice
	matrix_normalizzata = []
	for raw in matrix:
		norm = [float(i)/sum(raw) for i in raw]
		matrix_normalizzata.append(norm)

	affinity =[]
	for raw in matrix_normalizzata:
		r = []
		for element in raw:
			element = 1- element
			r.append(element)
		affinity.append(r)
	print affinity
	af = AffinityPropagation(damping=0.75,affinity='precomputed').fit(affinity)
	return af.labels_


def get_cluster_mura(walls, cluster_angolari, parametri_obj):
	'''
	ottengo un il cluster del muro.
	'''
	#ottengo i cluster angolari
	ang = set(cluster_angolari)

	#e' una matrice del tipo [[..,..,..], [..,..,..,..]] in base al numero di cluster angolari
	angolar_ordered = []
	for c in ang:
		row = []
		for w in walls:
			if w.cluster_angolare == c:
				row.append(w)
		angolar_ordered.append(row)

	#ottengo la matrice di affinita' dei segmenti per ogni cluster angolare
	#ogni elemento di M contiene una matrice delle distanze su cui andro' a fare il clustering
	M= []
	for ang in angolar_ordered:
		matrix = get_distance_matrix(ang)
		M.append(matrix)

	#per ogni cluster angolare ottengo un insieme di label, ottenuti dal clustering mura.
	label =[]
	for mat in M:
		label.append(compute_clustering(mat))
		#label.append(compute_affinity_propagation(mat))


	#setto le label a tutti i segmenti(ogni segmento ha una label mura)
	walls = sg.set_segment_label2(angolar_ordered, label)


	#creo lista di cluster mura
	cluster_mura = []
	for segmento in walls:
		cluster_mura.append(segmento.cluster_muro)
	return cluster_mura


def get_rappresentanti(walls,cluster_mura):
	'''
	ottedo i segmenti rappresentatni di un cluster
	'''
	rappresentanti = []

	for cluster in set(cluster_mura):
		lista = []
		distance_vector = []
		#creo la lista di elemnti che hanno cluater muro uguale
		for m in walls:
			if m.cluster_muro == cluster:
				lista.append(m)


		candidato = lista[0] #prendo il primo elemento del cluster e lo uso per proittare tutti gli altri elementi dello stesso cluster sulla retta passante per il centro di questo elemento.
		x= (candidato.x1+candidato.x2)/2
		y= (candidato.y1+candidato.y2)/2
		angolo = candidato.cluster_angolare * (180/math.pi)

		#raccolgo tutte le proiezioni sulla retta ortogonale di candidato e faccio una rototraslazione dei punti.
		X=[]
		Y=[]
		for i in lista:
			(x_proietteato, y_proiettato) = sg.get_punti_proiettati(candidato,i)
			X.append(x_proietteato)
			Y.append(y_proiettato)

		myfunction=rotot.transformPoints(x,y,angolo)
		for px,py in zip(X,Y):
			distance_vector.append(myfunction(px,py)[0])#prendo solo la coordinata x, la y tanto o e' 0 o e molto vicino allo zero(non mi interessa poiche ho fatto una rototraslazione)


		#ora raccolgo il mediano della lista distance_vector
		index_rappresentante = numpy.argsort(distance_vector)[len(distance_vector)//2]#TODO: secondo me qua ci vuole (len(distance_vector)//2)-1  perche' altrimenti prendo l'indice sbagliato. controllare.

		rappresentanti.append(lista[index_rappresentante])#solo questo deve rimanere


	return rappresentanti

	'''
	#in questo momento prendo un segmento a caso tra tutti quelli che appartengono allo stesso cluster_muro.
	#in realta' devo andare a prendere il mediano. Il mediano lo ottengo in questo modo: prendo a caso un segmento(il primo della lista), calcolo lista di distance vector usando la funzione lateral_separation_distance(muro1,muro2) di segmento.

	rappresentanti = []
	for cluster in set(cluster_mura):
		lista = []
		#creo la lista di elementi che hanno cluster muro uguale
		for m in walls:
			if m.cluster_muro == cluster:
				lista.append(m)
		#prendo un segmento a caso con lo stesso cluster
		num = random.random() * len(lista)
		rappresentanti.append(lista[int(num)])
	return rappresentanti
	'''
def new_cluster_spaziale(walls, segmenti_rappresentanti, parametri_obj):
	'''
	creo la lista di tutti i cluster spaziali e la restituisco. Inoltre Per ogni segmento
	in walls il cui cluster spaziale non e' ancora stato settato,lo setto controllando che appartenga allo stesso cluster_muro del rappresentante.

	'''
	#creo lista di cluster spaziali
	cluster_spaziali = []
	for muro in walls:
		if muro.cluster_spaziale !=None:
			cluster_spaziali.append(muro.cluster_spaziale)

	for spaz in list(set(cluster_spaziali)):
		#raccolgo i cluster muri che hanno stesso cluster spaziale
		cluster_mura_uguali = []
		for segmento in segmenti_rappresentanti:
			if segmento.cluster_spaziale == spaz:
				cluster_mura_uguali.append(segmento.cluster_muro)

		cluster_mura_uguali = list(set(cluster_mura_uguali))

		for segmento in walls:
			if segmento.cluster_muro in cluster_mura_uguali:
				segmento.set_cluster_spaziale(spaz)

	#gestire gli outliers

	#in sostanza devo unire al cluster piu' vicino ogni segmento di outlier, se non c'e' un cluster vicino, allora ne creo uno anche se ha un solo segmento
	#ottengo gli outliers
	outliers = []
	for s in walls:
		if s.cluster_muro == -1:
			outliers.append(s)
	#set_cluster_spaziale_to_outliers(walls, outliers, segmenti_rappresentanti, parametri_obj.sogliaLateraleClusterMura)
	set_cluster_spaziale_to_outliers_versione_2(walls, outliers, segmenti_rappresentanti, parametri_obj.sogliaLateraleClusterMura)


	cluster_spaz = []
	for s in walls:
		cluster_spaz.append(s.cluster_spaziale)

	return cluster_spaz

#TODO: se la versione 2 funziona perfettamente questa non serve piu'
def set_cluster_spaziale_to_outliers(walls, outliers, segmenti_rappresentanti, sogliaLateraleClusterMura):
	'''
	setto il cluster spaziale a quei segmenti che sono stati classificati come outliers da DBSCAN. Li voglio unire a cluster spaziali che esistono gia'
	'''
	#se un segmento outlier e' molto vicino ad un cluster, allora lo unisco al cluster, altrimenti ne creo uno nuovo.

	for o in outliers:
		min_distance_to_cluster = 999999
		rappresentante_selezionato = segmenti_rappresentanti[0]
		for r in segmenti_rappresentanti:
			dist = sg.lateral_separation(o,r)
			if o.cluster_angolare == r.cluster_angolare:
				if dist <= min_distance_to_cluster:
					min_distance_to_cluster = dist
					rappresentante_selezionato = r
		#assegno all'outliers lo stesso cluster spaziale del rappresentante selezionato
		if min_distance_to_cluster <= sogliaLateraleClusterMura:
			o.cluster_spaziale = rappresentante_selezionato.cluster_spaziale
			o.cluster_muro = rappresentante_selezionato.cluster_muro
		else:
			#creo un nuovo cluster (prendo come indice la posizione in walls dell'outlier)
			new_clust = walls.index(o)
			o.cluster_spaziale = new_clust
			#TODO: se qua qualcosa non va e' perche' non hai cambiato il cluter muro. CAMBIALO

def set_cluster_spaziale_to_outliers_versione_2(walls, outliers, segmenti_rappresentanti, sogliaLateraleClusterMura):
	'''
	setto il cluster spaziale a quei segmenti che sono stati classificati come outliers da DBSCAN. Li voglio unire a cluster spaziali che esistono gia'
	'''
	#se un segmento outlier e' molto vicino ad un cluster, allora lo unisco al cluster, altrimenti ne creo uno nuovo.

	for o in outliers:
		min_distance_to_cluster = 999999
		rappresentante_selezionato = segmenti_rappresentanti[0]
		for r in segmenti_rappresentanti:
			dist = sg.lateral_separation(o,r)
			if o.cluster_angolare == r.cluster_angolare:
				if dist <= min_distance_to_cluster:
					min_distance_to_cluster = dist
					rappresentante_selezionato = r
		#assegno all'outliers lo stesso cluster spaziale del rappresentante selezionato
		if min_distance_to_cluster <= sogliaLateraleClusterMura:
			o.cluster_spaziale = rappresentante_selezionato.cluster_spaziale
			o.cluster_muro = rappresentante_selezionato.cluster_muro
		else:
			#creo un nuovo cluster (prendo come indice la posizione in walls dell'outlier)
			new_clust = walls.index(o)
			o.cluster_spaziale = new_clust
			#vado ad inserire il nuovo cluster tra i rappresentanti perche' altrimenti gli outliers non vengono uniti come gruppo ma solo associati ad altri gruppi
			segmenti_rappresentanti.append(o)
			#TODO: se qua qualcosa non va e' perche' non hai cambiato il cluter muro. CAMBIALO




def get_celle_parziali(celle, celle_out, coordinate_bordi):
	'''
	ottengo le celle parziali
	'''
	celle_parziali = []
	#le celle che non sono state messe come out, ma che sono adiacenti al bordo dell'immagine (hanno celle adiacenti < len(bordi)) sono per forza parziali
	'''
	a=0
	for f in celle:
		for f2 in celle:
			if (f!=f2) and (fc.adiacenti(f,f2)):
				a += 1
		if (a<len(f.bordi)):
			#print("ciao")
			if not (f.out):
				f.set_out(False) #se una cella e' parziale, non e' out per me. lui aveva messo True
				f.set_parziale(True)
				celle_parziali.append(f)
		a = 0
	'''
	#trovo circa tutte le celle out il problema e' che purtroppo se per caso c'e' una cella piccola che non tocca il suo peso e' basso
	for c in celle:
		for co in celle_out:
			if fc.adiacenti(c,co):
				if(fc.edge_comune(c,co)[0].weight < 0.05):
					c.set_out(False)#se una cella e' parziale, non e' out per me. lui aveva messo True
					c.set_parziale(True)
					celle_parziali.append(c)
		#se la cella ha un bordo attaccato al bordo dell'imagine vuol dire che e' per forza parziale
		for bordo in c.bordi:
			xlist = [coordinate_bordi[0], coordinate_bordi[2]]
			ylist = [coordinate_bordi[1], coordinate_bordi[3]]
			if (bordo.x1 or bordo.x2) in xlist or (bordo.y1 or bordo.y2) in ylist :
				c.set_out(False)#se una cella e' parziale, non e' out per me. lui aveva messo True
				c.set_parziale(True)
				celle_parziali.append(c)


	'''
	#le celle adiacenti ad una cella out tramite un edge che pesa poco, sono parziali.
	a = 1
	while(a!=0):
		a = 0
		for f in celle:
			for f2 in celle:
				if (f!=f2) and (f.out==False) and (f2.out==True) and (fc.adiacenti(f,f2)):
					if(fc.edge_comune(f,f2)[0].weight < 0.1):
						f.set_out(False)#se una cella e' parziale, non e' out per me. lui aveva messo True
						f.set_parziale(True)
						celle_parziali.append(f)
						a = 1
	'''
	#poligoni celle parziali
	parz_poligoni = []
	for f in celle_parziali:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		parz_poligoni.append(cella)


	return celle_parziali, parz_poligoni


def get_poligoni_out(celle_out):
	'''
	ottengo i poligoni relativi a celle esterne
	'''
	#poligoni celle esterne
	out_poligoni = []
	for f in celle_out:
		punti = []
		for b in f.bordi:
			punti.append([float(b.x1),float(b.y1)])
			punti.append([float(b.x2),float(b.y2)])
		punti = sort_and_deduplicate(punti)
		x = [p[0] for p in punti]
		y = [p[1] for p in punti]
		global centroid
		centroid = (sum(x) / len(punti), sum(y) / len(punti))
		punti.sort(key=algo)
		cella = Polygon(punti)
		out_poligoni.append(cella)

	return out_poligoni


def calcola_copertura_extended_segment(extended_segments, spazi):
	'''
	per ogni extended segment calcolo la copertura. cioe' quante sono le stanze che tocca
	'''

	for ext_seg in extended_segments:
		#tocca = False
		n_stanze_coperte = 0
		for s in spazi:
			tocca = False
			for cella in s.cells:
				extended_cella = ext.estrai_extended_segment_da_cella(cella.c, extended_segments)

				for e in extended_cella:
					if e == ext_seg:
						tocca=True

			if tocca == True:
				n_stanze_coperte+=1

		ext_seg.set_copertura(n_stanze_coperte)
