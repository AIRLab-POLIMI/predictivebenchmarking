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

''' Layout reconstruction '''
def extractLayout(parametri_obj, path_obj):
	start_time_main = time.time()
	# load parameters 
	parametri_obj.minLateralSeparation=int(round(parametri_obj.minLateralSeparationFactor/parametri_obj.imageScale))
	parametri_obj.minLineLength=int(round(parametri_obj.minLineLengthFactor/parametri_obj.imageScale))
	parametri_obj.maxLineGap=int(round(parametri_obj.maxLineGapFactor/parametri_obj.imageScale))
	parametri_obj.sogliaLateraleClusterMura = int(round(parametri_obj.sogliaLateraleClusterMuraFactor/parametri_obj.imageScale))
	#----------------------------1.0_COMPUTING LAYOUT----------------------------------
	# read the original image
	img_rgb = cv2.imread(path_obj.metricMap)
	img_ini = img_rgb.copy()
	y_span,x_span,channels = img_rgb.shape

	# cleaning
	ret,thresh1 = cv2.threshold(img_rgb,parametri_obj.cv2thresh,250,cv2.THRESH_BINARY)

	#------------------1.1_WALL IDENTIFICATION WITH CANNY AND HOUGH---------------------------------
	walls , canny = lay.start_canny_ed_hough(thresh1,parametri_obj)
	lines = lay.flip_lines(walls, img_rgb.shape[0]-1)
	old_walls = walls
	walls = lay.crea_muri(lines)
	
	#------------1.2_IDENTIFICATION OF WALL EXTREMES-----------------------------------
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
	# if drawing is enabled, draw the initial map and the results of the application of Canny and Hough
	if par.DISEGNA:
		dsg.disegna_map(img_rgb,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
		dsg.disegna_canny(canny,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
		dsg.disegna_hough(img_rgb,old_walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
	# if drawing is enabled, draw the image with the identified walls
	if par.DISEGNA:
		#disegno linee
		dsg.disegna_segmenti(walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

	#---------------1.3_EXTERNAL CONTOUR--------------------------------------------------
	(contours, vertici) = lay.contorno_esterno_versione_tre(img_rgb)
	if par.DISEGNA:
		dsg.disegna_contorno(vertici,xmin,ymin,xmax,ymax,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span)
	#---------------1.4_MEAN SHIFT FOR THE IDENTIFICATION OF ANGULAR CLUSTERS---------------------------
	(indici, walls, cluster_angolari) = lay.cluster_ang(parametri_obj.h, parametri_obj.minOffset, walls, diagonali= parametri_obj.diagonali)
	if par.DISEGNA:
		dsg.disegna_cluster_angolari_corretto(walls, cluster_angolari, filepath = path_obj.actualOutputFolder,savename = '5b_cluster_angolari',format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

	#---------------1.5_SPATIAL CLUSTERS IDENTIFICATION (Valerio Arcerito's method)------------------------------------------
	# cluster walls together, -1 denotes a false cluster that should not be considered for processing
	cluster_mura = lay.get_cluster_mura(walls, cluster_angolari, parametri_obj)
	cluster_mura_senza_outliers = []
	for c in cluster_mura:
		if c!=-1:
			cluster_mura_senza_outliers.append(c)
	# merge clusters that are very close to each other in a single representative
	segmenti_rappresentanti = lay.get_rappresentanti(walls, cluster_mura_senza_outliers)
	if par.DISEGNA:
		dsg.disegna_segmenti(segmenti_rappresentanti,filepath = path_obj.actualOutputFolder, savename = "5c_segmenti_rappresentanti", format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

	# segment classification
	segmenti_rappresentanti = sg.spatialClustering(parametri_obj.sogliaLateraleClusterMura, segmenti_rappresentanti)
	cluster_spaziali = lay.new_cluster_spaziale(walls, segmenti_rappresentanti, parametri_obj)

	if par.DISEGNA:
		dsg.disegna_cluster_spaziali(cluster_spaziali, walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
		dsg.disegna_cluster_mura(cluster_mura, walls,filepath = path_obj.actualOutputFolder, savename= '5d_cluster_mura', format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

	#-------------------1.6_EXTENDED_LINES CREATION-------------------------------------------
	(extended_lines, extended_segments) = lay.extend_line(cluster_spaziali, walls, xmin, xmax, ymin, ymax,filepath = path_obj.actualOutputFolder)
	if par.DISEGNA:
		dsg.disegna_extended_segments(extended_segments, walls,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

	#-------------1.7_CREATE EDGES BY INTERSECTION OF EXTENDED LINES--------------
	edges = sg.crea_edges(extended_segments)
	#----------------------1.8_SET EDGE WEIGHT-------------------------------------
	edges = sg.setPeso(edges, walls)
	#----------------1.9_IDENTIFY SPATIAL CELLS----------------------------------------
	celle = fc.crea_celle(edges)
	#----------------CELL CLASSIFICATION-----------------------------------------------------
	global centroid
	#verificare funzioni
	if par.metodo_classificazione_celle ==1:
		(celle, celle_out, celle_poligoni, indici, celle_parziali, contorno, centroid, punti) = lay.classificazione_superfici(vertici, celle)
	elif par.metodo_classificazione_celle==2:
		(celle_out, celle, centroid, punti,celle_poligoni, indici, celle_parziali) = lay.classifica_celle_con_percentuale(vertici, celle, img_ini)
	#--------------------------BUILD CELL POLYGONS---------------------------------------------
	(celle_poligoni, out_poligoni, parz_poligoni, centroid) = lay.crea_poligoni_da_celle(celle, celle_out, celle_parziali)

	dsg.disegna_poligoni_interni_esterni(celle_poligoni, out_poligoni, parz_poligoni, xmin, ymin, xmax, ymax, format='png', x_span=x_span,y_span=y_span,filepath = path_obj.actualOutputFolder, savename = '8_d_celle_in_out')

	(matrice_l, matrice_d, matrice_d_inv, X) = lay.crea_matrici(celle, sigma = parametri_obj.sigma)

	#----------------IDENTIFICATION OF CELLS BELONGING TO THE SAME SPACE/ROOM WITH DBSCAN-------------------------
	clustersCelle = lay.DB_scan(parametri_obj.eps, parametri_obj.minPts, X, celle_poligoni)
	if par.DISEGNA:
		colori, fig, ax = dsg.disegna_dbscan(clustersCelle, celle, celle_poligoni, xmin, ymin, xmax, ymax, edges, contours,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span)
	else:
		colori = dsg.get_colors(clustersCelle, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
	#------------------BUILD SPACE/ROOM POLYGONS--------------------------------------------
	stanze, spazi = lay.crea_spazio(clustersCelle, celle, celle_poligoni, colori, xmin, ymin, xmax, ymax, filepath = path_obj.actualOutputFolder)
	if par.DISEGNA:
		dsg.disegna_stanze(stanze, colori, xmin, ymin, xmax, ymax,filepath = path_obj.actualOutputFolder, format='png',x_span=x_span,y_span=y_span)

	#--------------------------------SUMMARY OUTPUT------------------------------------------
	dsg.disegno_mura_segmenti_stanze(stanze, colori, xmin, ymin, xmax, ymax, cluster_spaziali, walls, format='png',x_span=x_span,y_span=y_span, filepath = path_obj.actualOutputFolder, savename = '14_tutto')
	dsg.disegna_pareti(edges, format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax, filepath =path_obj.actualOutputFolder, savename = '14_pareti')
	wallEnlargement = parametri_obj.wallEnlargementFactor/parametri_obj.imageScale
	G,pos,connectedRooms = tg.createGraph(path_obj.metricMap,spazi,wallEnlargement)
	dsg.plot_nodi_e_stanze(colori,estremi,G,pos,spazi,connectedRooms,filepath =path_obj.actualOutputFolder,format='png',x_span=x_span,y_span=y_span,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
	# create XML
	id_stanze = xmlutils.crea_xml(path_obj.outputFileName, spazi, parametri_obj.imageScale, vertici, connectedRooms)
