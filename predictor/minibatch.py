from __future__ import division
import datetime as dt
import numpy as np
import networkx as nx
import util.layout as lay
import util.GrafoTopologico as gtop
import util.transitional_kernels as tk
import util.MappaSemantica as sema
import util.frontiere as fr
from object import Segmento as sg
from util import pickle_util as pk
from util import accuracy as ac
from util import layout as lay
from util import disegna as dsg
from util import predizionePlan_geometriche as pgeom
from object import Superficie as fc
from object import Spazio as sp
from object import Plan as plan
from util import MCMC as mcmc
from util import valutazione as val
from util import medial as mdl
from util import accuracy_parziale as acpar
from util import util_XML as xmlutils
from util import metriche_frontiere as mf
from util import helper as  hp
from util import TopologicalGraph as tg
from shapely.geometry import Point
from shapely.geometry import LineString
import math
from shapely.geometry import Polygon
import parameters as par
import pickle
import os
import glob
import shutil
import time
import cv2
import warnings
import copy
import sys
warnings.warn("Settare i parametri del lateralLine e cvThresh")

def extractLayout(parametri_obj, path_obj):
	start_time_main = time.time()
	parametri_obj.minLateralSeparation=int(round(parametri_obj.minLateralSeparationFactor/parametri_obj.imageScale))
	parametri_obj.minLineLength=int(round(parametri_obj.minLineLengthFactor/parametri_obj.imageScale))
	parametri_obj.maxLineGap=int(round(parametri_obj.maxLineGapFactor/parametri_obj.imageScale))
	parametri_obj.sogliaLateraleClusterMura = int(round(parametri_obj.sogliaLateraleClusterMuraFactor/parametri_obj.imageScale))
	print parametri_obj.minLateralSeparation
	print parametri_obj.minLineLength
	print parametri_obj.maxLineGap
	print parametri_obj.sogliaLateraleClusterMura
	#----------------------------1.0_LAYOUT DELLE STANZE----------------------------------
	#------inizio layout
	#leggo l'immagine originale in scala di grigio e la sistemo con il thresholding
	img_rgb = cv2.imread(path_obj.metricMap)
	img_ini = img_rgb.copy() #copio l'immagine
	y_span,x_span,channels = img_rgb.shape
	# 127 per alcuni dati, 255 per altri

	#serve a pulire l'immagine (solo nel caso in cui sia sporca(mobili all'interno))
	pulisci_immagine = False
	if pulisci_immagine ==False:
		ret,thresh1 = cv2.threshold(img_rgb,parametri_obj.cv2thresh,255,cv2.THRESH_BINARY)#prova
	else:
		#utile a pulire l'immagine se e' sporca
		#minpoints = k
		k = 15
		l = 9
		ret,thresh1 = cv2.threshold(img_rgb,parametri_obj.cv2thresh,255,cv2.THRESH_BINARY)
		tmp2 = thresh1.copy()
		noisy_pixel =hp.cluster_img(tmp2,k,l,'after',2)
		img_d = img_rgb.copy()
		img_e = img_rgb.copy()
		for i in noisy_pixel:
			img_d[i[0],i[1]]= [255,0,0]
			img_e[i[0],i[1]] = [255,255,255]
		cv2.imwrite('00_'+str(k)+"_"+str(l)+'_removed.png',img_d)
		cv2.imwrite('00_'+str(k)+"_"+str(l)+'_postprocessing.png',img_e)
		ret,thresh1 = cv2.threshold(img_e,parametri_obj.cv2thresh,255,cv2.THRESH_BINARY)

	#prova
	#kernel = np.ones((3,3),np.uint8)
	#erosion = cv2.erode(thresh1,kernel,iterations = 10)
	#thresh1=erosion

	#------------------1.1_CANNY E HOUGH PER TROVARE MURI---------------------------------
	walls , canny = lay.start_canny_ed_hough(thresh1,parametri_obj)
	print "walls: ", len(walls)
	lines = lay.flip_lines(walls, img_rgb.shape[0]-1)
	old_walls = walls
	walls = lay.crea_muri(lines)
	print "lines", len(lines), len(walls)

	#walls , canny = lay.start_canny_ed_hough(img_rgb,parametri_obj)

	#------------1.2_SETTO XMIN YMIN XMAX YMAX DI walls-----------------------------------
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

	if par.DISEGNA:
		#disegna mappa iniziale, canny ed hough
		dsg.disegna_map(img_rgb,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
		dsg.disegna_canny(canny,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
		dsg.disegna_hough(img_rgb,old_walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

	if par.DISEGNA:
		#disegno linee
		dsg.disegna_segmenti(walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)#solo un disegno poi lo elimino

	#-------------------------------------------------------------------------------------
	#---------------1.3_CONTORNO ESTERNO--------------------------------------------------

	#(contours, vertici) = lay.contorno_esterno(img_rgb, parametri_obj, path_obj)
	(contours, vertici) = lay.contorno_esterno_versione_tre(img_rgb)#MIO METODO
	if par.DISEGNA:
		dsg.disegna_contorno(vertici,xmin,ymin,xmax,ymax,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span)
	#-------------------------------------------------------------------------------------
	#---------------1.4_MEAN SHIFT PER TROVARE CLUSTER ANGOLARI---------------------------
	(indici, walls, cluster_angolari) = lay.cluster_ang(parametri_obj.h, parametri_obj.minOffset, walls, diagonali= parametri_obj.diagonali)
	if par.DISEGNA:
		#dsg.disegna_cluster_angolari(walls, cluster_angolari, filepath = path_obj.filepath,savename = '5b_cluster_angolari')
		dsg.disegna_cluster_angolari_corretto(walls, cluster_angolari, filepath = path_obj.actualOutputFolder,savename = '5b_cluster_angolari',format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

	#-------------------------------------------------------------------------------------

	#---------------1.5_CLUSTER SPAZIALI--------------------------------------------------
	#questo metodo e' sbagliato, fai quella cosa con il hierarchical clustering per classificarli meglio.e trovare in sostanza un muro
	#cluster_spaziali = lay.cluster_spaz(parametri_obj.minLateralSeparation, walls)
	#inserisci qui il nuovo Cluster_spaz
	nuovo_clustering = 2 #1 metodo di matteo, 2 mio
	#in walls ci sono tutti i segmenti
	if nuovo_clustering == 1:
		cluster_spaziali = lay.cluster_spaz(parametri_obj.minLateralSeparation, walls)#metodo di matteo
	elif nuovo_clustering ==2:

		cluster_mura = lay.get_cluster_mura(walls, cluster_angolari, parametri_obj)#metodo di valerio

		cluster_mura_senza_outliers = []
		for c in cluster_mura:
			if c!=-1:
				cluster_mura_senza_outliers.append(c)
		# ottengo gli outliers
# 		outliers = []
# 		for s in walls:
# 			if s.cluster_muro == -1:
# 				outliers.append(s)
# 		dsg.disegna_segmenti(outliers, savename = "outliers")



		'''
		#-----------------------PARTE AGGIUNTA SOLO PER LA MAPPA BRUTTA-----------------------------------
		#elimino i cluster mura orizzontali troppo piccoli-----------------
		print "bla -0.0005539711144683633", set(cluster_angolari)
		da_eliminare= []
		cluster_piccoli = []
		for cm in cluster_mura_senza_outliers:
			clu = []
			for segmento in walls:
				if segmento.cluster_muro == cm and segmento.cluster_angolare ==-0.0005539711144683633:
					clu.append(segmento)

			if len(clu)<4:
				cluster_piccoli.append(cm)

		for w in walls:
			for clust in cluster_piccoli:
				if w.cluster_muro == clust:
					da_eliminare.append(w)

		print "prima", len(walls)
		VECCHIO_WALLS = copy.deepcopy(walls)
		walls = list(set(walls)-set(da_eliminare))
		cluster_mura_senza_outliers = list(set(cluster_mura_senza_outliers)-set(cluster_piccoli))
		print "dopo", len(walls), len(VECCHIO_WALLS)

		#-------------------------------------------------------------------------------------------------
		'''



		#ora che ho un insieme di cluster relativi ai muri voglio andare ad unire quelli molto vicini
		#ottengo i rappresentanti dei cluster (tutti tranne gli outliers)
		#segmenti_rappresentanti = lay.get_rappresentanti(walls, cluster_mura)
		segmenti_rappresentanti = lay.get_rappresentanti(walls, cluster_mura_senza_outliers)


		if par.DISEGNA:
			dsg.disegna_segmenti(segmenti_rappresentanti,filepath = path_obj.actualOutputFolder, savename = "5c_segmenti_rappresentanti", format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

		#classifico i rappresentanti
		#qui va settata la soglia con cui voglio separare i cluster muro

		#segmenti_rappresentanti = segmenti_rappresentanti
		segmenti_rappresentanti = sg.spatialClustering(parametri_obj.sogliaLateraleClusterMura, segmenti_rappresentanti)
		#in questo momento ho un insieme di segmenti rappresentanti che hanno il cluster_spaziale settato correttamente, ora setto anche gli altri che hanno lo stesso cluster muro
		cluster_spaziali = lay.new_cluster_spaziale(walls, segmenti_rappresentanti, parametri_obj)

	if par.DISEGNA:
		dsg.disegna_cluster_spaziali(cluster_spaziali, walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
		dsg.disegna_cluster_mura(cluster_mura, walls,filepath = path_obj.actualOutputFolder, savename= '5d_cluster_mura', format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
	#-------------------------------------------------------------------------------------

	#-------------------1.6_CREO EXTENDED_LINES-------------------------------------------
	(extended_lines, extended_segments) = lay.extend_line(cluster_spaziali, walls, xmin, xmax, ymin, ymax,filepath = path_obj.actualOutputFolder)

	if par.DISEGNA:
		dsg.disegna_extended_segments(extended_segments, walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
		#dsg.disegna_extended_segments_e_contorno(vertici,xmin,ymin,xmax,ymax,extended_segments, format='png', filepath =path_obj.filepath, savename = '7_Extended_cotorno')
	#-------------------------------------------------------------------------------------

	#-------------1.7_CREO GLI EDGES TRAMITE INTERSEZIONI TRA EXTENDED_LINES--------------
	edges = sg.crea_edges(extended_segments)
	#-------------------------------------------------------------------------------------

	#----------------------1.8_SETTO PESI DEGLI EDGES-------------------------------------
	edges = sg.setPeso(edges, walls)

	#-------------------------------------------------------------------------------------

	#----------------1.9_CREO LE CELLE DAGLI EDGES----------------------------------------
	celle = fc.crea_celle(edges)
	#-------------------------------------------------------------------------------------

	#----------------CLASSIFICO CELLE-----------------------------------------------------
	global centroid
	#verificare funzioni
	if par.metodo_classificazione_celle ==1:
		print "1.metodo di classificazione ", par.metodo_classificazione_celle
		(celle, celle_out, celle_poligoni, indici, celle_parziali, contorno, centroid, punti) = lay.classificazione_superfici(vertici, celle)
	elif par.metodo_classificazione_celle==2:
		print "2.metodo di classificazione ", par.metodo_classificazione_celle
		#sto classificando le celle con il metodo delle percentuali
		(celle_out, celle, centroid, punti,celle_poligoni, indici, celle_parziali) = lay.classifica_celle_con_percentuale(vertici, celle, img_ini)
	#-------------------------------------------------------------------------------------

	#--------------------------POLIGONI CELLE---------------------------------------------
	(celle_poligoni, out_poligoni, parz_poligoni, centroid) = lay.crea_poligoni_da_celle(celle, celle_out, celle_parziali)

	dsg.disegna_poligoni_interni_esterni(celle_poligoni, out_poligoni, parz_poligoni, xmin, ymin, xmax, ymax, format='png', x_span=x_span,y_span=y_span,filepath = path_obj.actualOutputFolder, savename = '8_d_celle_in_out')

	#ora vorrei togliere le celle che non hanno senso, come ad esempio corridoi strettissimi, il problema e' che lo vorrei integrare con la stanza piu' vicina ma per ora le elimino soltanto

	#RICORDA: stai pensando solo a celle_poligoni
	#TODO: questo metodo non funziona benissimo(sbagli ad eliminare le celle)
	#celle_poligoni, celle = lay.elimina_celle_insensate(celle_poligoni,celle, parametri_obj)#elimino tutte le celle che hanno una forma strana e che non ha senso siano stanze
	#-------------------------------------------------------------------------------------


	#------------------CREO LE MATRICI L, D, D^-1, ED M = D^-1 * L------------------------
	(matrice_l, matrice_d, matrice_d_inv, X) = lay.crea_matrici(celle, sigma = parametri_obj.sigma)
	#-------------------------------------------------------------------------------------

	#----------------DBSCAN PER TROVARE CELLE NELLA STESSA STANZA-------------------------
	clustersCelle = lay.DB_scan(parametri_obj.eps, parametri_obj.minPts, X, celle_poligoni)
	#questo va disegnato per forza perche' restituisce la lista dei colori
	if par.DISEGNA:
		colori, fig, ax = dsg.disegna_dbscan(clustersCelle, celle, celle_poligoni, xmin, ymin, xmax, ymax, edges, contours,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span)
	else:
		colori = dsg.get_colors(clustersCelle, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
	#-------------------------------------------------------------------------------------

	#------------------POLIGONI STANZE(spazio)--------------------------------------------
	stanze, spazi = lay.crea_spazio(clustersCelle, celle, celle_poligoni, colori, xmin, ymin, xmax, ymax, filepath = path_obj.actualOutputFolder)
	if par.DISEGNA:
		dsg.disegna_stanze(stanze, colori, xmin, ymin, xmax, ymax,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span)
	#-------------------------------------------------------------------------------------

	#cerco le celle parziali
	coordinate_bordi = [xmin, ymin, xmax, ymax]
	celle_parziali, parz_poligoni = lay.get_celle_parziali(celle, celle_out, coordinate_bordi)#TODO: non ho controllato bene ma mi pare che questa cosa possa essere inserita nel metodo 1 che crca le celle parziali, TODO: verifica, ma mi pare che sta cosa non faccia nulla
	#creo i poligoni relativi alle celle_out
	out_poligoni = lay.get_poligoni_out(celle_out)

	#--------------------------------fine layout------------------------------------------
	dsg.disegno_mura_segmenti_stanze(stanze, colori, xmin, ymin, xmax, ymax, cluster_spaziali, walls, format='png',x_span=x_span,y_span=y_span, filepath = path_obj.actualOutputFolder, savename = '14_tutto')
	dsg.disegna_pareti(edges, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax, filepath =path_obj.actualOutputFolder, savename = '14_pareti')
	wallEnlargement = parametri_obj.wallEnlargementFactor/parametri_obj.imageScale
	G,pos,connectedRooms = tg.createGraph(path_obj.metricMap,spazi,wallEnlargement)
	dsg.plot_nodi_e_stanze(colori,estremi,G,pos,spazi,connectedRooms,filepath =path_obj.actualOutputFolder,format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
	#creo xml stanze
	id_stanze = xmlutils.crea_xml(path_obj.outputFileName, spazi, parametri_obj.imageScale, vertici, connectedRooms)#id stanze e' ordinato come spazi e possiede l'id univo assegnato alla stanza

	#TODO

def algo(p):
	'''
	riordina i punti in senso orario
	'''
	return (math.atan2(p[0] - centroid[0], p[1] - centroid[1]) + 2 * math.pi) % (2*math.pi)

def load_main(filepath_pickle_layout, filepath_pickle_grafoTopologico, parXML):
	#carico layout
	pkl_file = open(filepath_pickle_layout, 'rb')
	data1 = pickle.load(pkl_file)
	stanze = data1[0]
	clustersCelle = data1[1]
	estremi = data1[2]
	colori = data1[3]
	spazi = data1[4]
	stanze_reali = data1[5]
	colori_reali= data1[6]

	#print "controllo che non ci sia nulla di vuoto", len(stanze), len(clustersCelle), len(estremi), len(spazi), len(colori)
	#carico il grafo topologico
	pkl_file2 = open( filepath_pickle_grafoTopologico, 'rb')
	data2 = pickle.load(pkl_file2)
	G = data2[0]
	pos = data2[1]
	stanze_collegate = data2[2]
	doorsVertices = data2[3]

	#creo dei nuovi oggetti parametri caricando i dati dal file xml
	new_parameter_obj, new_path_obj =  par.load_from_XML(parXML)

	#continuare il metodo da qui


def makeFolders(location,datasetList):
	for dataset in datasetList:
		if not os.path.exists(location+dataset):
			os.mkdir(location+dataset)
			os.mkdir(location+dataset+"_pickle")

def extractLayoutFromFile(metricMap):
	start = time.time()
	''' Initialize default parameters '''
	param_obj = par.Parameter_obj()
	path_obj = par.Path_obj()
	''' Make sure we have all the necessary folders created, otherwise create them '''
	makeFolders(path_obj.OUTFOLDERS, path_obj.DATASETs)
	map_name = metricMap.split('/')[-1][:-4]
	extractLayout(param_obj, path_obj)
	fine = time.time()
	elapsed = fine-start
	print "Computation lasted %f seconds" % elapsed

if __name__ == '__main__':
	extractLayoutFromFile(sys.argv[1])
