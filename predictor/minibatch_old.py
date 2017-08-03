from __future__ import division
import datetime as dt
import numpy as np
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
warnings.warn("Settare i parametri del lateralLine e cvThresh")

def start_main(parametri_obj, path_obj):
	start_time_main = time.time()
	#----------------------------1.0_LAYOUT DELLE STANZE----------------------------------
	#------inizio layout
	#leggo l'immagine originale in scala di grigio e la sistemo con il thresholding
	img_rgb = cv2.imread(path_obj.metricMap)
	img_ini = img_rgb.copy() #copio l'immagine
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

	#walls , canny = lay.start_canny_ed_hough(img_rgb,parametri_obj)
	
	if par.DISEGNA:
		#disegna mappa iniziale, canny ed hough
		dsg.disegna_map(img_rgb,filepath = path_obj.filepath, format='pdf')
		dsg.disegna_canny(canny,filepath = path_obj.filepath, format='pdf')
		dsg.disegna_hough(img_rgb,walls,filepath = path_obj.filepath, format='pdf')
		
	lines = lay.flip_lines(walls, img_rgb.shape[0]-1)
	walls = lay.crea_muri(lines)
	print "lines", len(lines), len(walls)
	if par.DISEGNA:
		#disegno linee
		dsg.disegna_segmenti(walls,filepath = path_obj.filepath, format='png')#solo un disegno poi lo elimino
	
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
	#-------------------------------------------------------------------------------------
	#---------------1.3_CONTORNO ESTERNO--------------------------------------------------
	
	#(contours, vertici) = lay.contorno_esterno(img_rgb, parametri_obj, path_obj)
	(contours, vertici) = lay.contorno_esterno_versione_tre(img_rgb)#MIO METODO
	if par.DISEGNA:
		dsg.disegna_contorno(vertici,xmin,ymin,xmax,ymax,filepath = path_obj.filepath, format='pdf')
	#-------------------------------------------------------------------------------------
	#---------------1.4_MEAN SHIFT PER TROVARE CLUSTER ANGOLARI---------------------------
	(indici, walls, cluster_angolari) = lay.cluster_ang(parametri_obj.h, parametri_obj.minOffset, walls, diagonali= parametri_obj.diagonali)
	if par.DISEGNA:	
		#dsg.disegna_cluster_angolari(walls, cluster_angolari, filepath = path_obj.filepath,savename = '5b_cluster_angolari')
		dsg.disegna_cluster_angolari_corretto(walls, cluster_angolari, filepath = path_obj.filepath,savename = '5b_cluster_angolari',format='pdf')
	
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
			dsg.disegna_segmenti(segmenti_rappresentanti,filepath = path_obj.filepath, savename = "5c_segmenti_rappresentanti", format='pdf')

		#classifico i rappresentanti
		#qui va settata la soglia con cui voglio separare i cluster muro
		
		#segmenti_rappresentanti = segmenti_rappresentanti
		segmenti_rappresentanti = sg.spatialClustering(parametri_obj.sogliaLateraleClusterMura, segmenti_rappresentanti)
		#in questo momento ho un insieme di segmenti rappresentanti che hanno il cluster_spaziale settato correttamente, ora setto anche gli altri che hanno lo stesso cluster muro
		cluster_spaziali = lay.new_cluster_spaziale(walls, segmenti_rappresentanti, parametri_obj)
			
	if par.DISEGNA:
		dsg.disegna_cluster_spaziali(cluster_spaziali, walls,filepath = path_obj.filepath, format='pdf')
		dsg.disegna_cluster_mura(cluster_mura, walls,filepath = path_obj.filepath, savename= '5d_cluster_mura', format='pdf')
	#-------------------------------------------------------------------------------------

	#-------------------1.6_CREO EXTENDED_LINES-------------------------------------------
	(extended_lines, extended_segments) = lay.extend_line(cluster_spaziali, walls, xmin, xmax, ymin, ymax,filepath = path_obj.filepath)
	
	if par.DISEGNA:
		dsg.disegna_extended_segments(extended_segments, walls,filepath = path_obj.filepath, format='pdf')	
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
	
	dsg.disegna_poligoni_interni_esterni(celle_poligoni, out_poligoni, parz_poligoni, xmin, ymin, xmax, ymax, format='png', filepath = path_obj.filepath, savename = '8_d_celle_in_out')
	
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
		colori, fig, ax = dsg.disegna_dbscan(clustersCelle, celle, celle_poligoni, xmin, ymin, xmax, ymax, edges, contours,filepath = path_obj.filepath, format='pdf')
	else:
		colori = dsg.get_colors(clustersCelle, format='pdf')
	#-------------------------------------------------------------------------------------

	#------------------POLIGONI STANZE(spazio)--------------------------------------------
	stanze, spazi = lay.crea_spazio(clustersCelle, celle, celle_poligoni, colori, xmin, ymin, xmax, ymax, filepath = path_obj.filepath) 
	if par.DISEGNA:
		dsg.disegna_stanze(stanze, colori, xmin, ymin, xmax, ymax,filepath = path_obj.filepath, format='pdf')
	#-------------------------------------------------------------------------------------
		
	#cerco le celle parziali
	coordinate_bordi = [xmin, ymin, xmax, ymax]
	celle_parziali, parz_poligoni = lay.get_celle_parziali(celle, celle_out, coordinate_bordi)#TODO: non ho controllato bene ma mi pare che questa cosa possa essere inserita nel metodo 1 che crca le celle parziali, TODO: verifica, ma mi pare che sta cosa non faccia nulla
	#creo i poligoni relativi alle celle_out
	out_poligoni = lay.get_poligoni_out(celle_out)
 			
	#--------------------------------fine layout------------------------------------------
	dsg.disegno_mura_segmenti_stanze(stanze, colori, xmin, ymin, xmax, ymax, cluster_spaziali, walls, format='pdf', filepath = path_obj.filepath, savename = '14_tutto')
	dsg.disegna_pareti(edges, format='pdf', filepath =path_obj.filepath, savename = '14_pareti')
	#-------------------------------------------------------------------------------------
	
	
	#DA QUI PARTE IL NUOVO PEZZO(da qui parte la parte che costruisce l'oggetto Plan e fa la predizione)
	
	'''
	#questa parte l'ho aggiuta dove faccio la parte di sistemaUnderEdOversegmentazione TODO: verificare che in quel punto non si rompa nulla
	#---------------------------ottengo le porte------------------------------------------
	#disegno le porte
	distanceMap, points, b3, b4, critical_points = mdl.critical_points(path_obj.metricMap)
	#b4 rappresentano i punti del medial axis che sono potenzialmente delle porte, e sono messi nella lista critical_points
	if par.DISEGNA:
		dsg.disegna_distance_transform(distanceMap, filepath = path_obj.filepath, format='png')
		dsg.disegna_medial_axis(points, b3, filepath = path_obj.filepath, format='png')
		dsg.disegna_medial_axis(points, b4, filepath = path_obj.filepath, format='png', savename='12_porte')
	#-------------------------------------------------------------------------------------
	'''
	
	#IDEA:
	#1) trovo le celle parziali(uno spazio e' parziali se almeno una delle sue celle e' parziale) e creo l'oggetto Plan
	#2) postprocessing per capire se le celle out sono realmente out
	#3) postprocessing per unire gli spazi che dovrebbero essere uniti 
	#4) separare gli spazi che non dovevano essere uniti.
	#creo l'oggetto plan che contiene tutti gli spazi, ogni stanza contiene tutte le sue celle, settate come out, parziali o interne. 	


	#---------------------------trovo le cellette parziali--------------------------------
	#se voglio il metodo che controlla le celle metto 1, 
	#se voglio il confronto di un intera stanza con l'esterno metto 2
	#se volgio il confronto di una stanza con quelli che sono i pixel classificati nella frontiera metto 3
	trova_parziali=3 
	
	if par.mappa_completa ==False and trova_parziali==1:
		#QUESTO METODO OGNI TANTO SBAGLIA PER VIA DELLA COPERTURA DEI SEGMANTI, verifico gli errori con il postprocessing per le stanze parziali.
		#TODO: Questo deve essere fatto solo se sono in presenza di mappe parziali
		sp.set_cellette_parziali(spazi, parz_poligoni)#trovo le cellette di uno spazio che sono parziali 
		spazi = sp.trova_spazi_parziali(spazi)#se c'e' almeno una celletta all'interno di uno spazio che e' parziale, allora lo e' tutto lo spazio.
		
	#creo l'oggetto Plan
	#faccio diventare la lista di out_poligoni delle cellette
	cellette_out = []
	for p,c in zip(out_poligoni, celle_out):	
		celletta = sp.Celletta(p,c)
		celletta.set_celletta_out(True)
		cellette_out.append(celletta)
	
	
	plan_o = plan.Plan(spazi, contorno, cellette_out) #spazio = oggetto Spazio. contorno = oggetto Polygon, cellette_out = lista di Cellette
	dsg.disegna_spazi(spazi, colori, xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13_spazi', format='png')
	
	#preprocessing del layout(unisco stanze erroneamente separate e viceversa)
	sistemaUnderEdOversegmentazione = False
	if sistemaUnderEdOversegmentazione == True:
		
		#---------------------------ottengo le porte------------------------------------------
		#TODO: questo metodo per ottenere le porte impiega troppo tempo per essere processato, non va bene
		#disegno le porte
		distanceMap, points, b3, b4, critical_points = mdl.critical_points(path_obj.metricMap)
		#b4 rappresentano i punti del medial axis che sono potenzialmente delle porte, e sono messi nella lista critical_points
		if par.DISEGNA:
			dsg.disegna_distance_transform(distanceMap, filepath = path_obj.filepath, format='png')
			dsg.disegna_medial_axis(points, b3, filepath = path_obj.filepath, format='png')
			dsg.disegna_medial_axis(points, b4, filepath = path_obj.filepath, format='png', savename='12_porte')
		#-------------------------------------------------------------------------------------
	
	
		#-----------------------------separo spazi undersegmentati ---------------------------
		#separo gli spazi che sono stati segmentati male
		separaStanzeUndersegmentate=1
		if separaStanzeUndersegmentate ==1:
			plan.separaUndersegmentazione(plan_o, critical_points, parametri_obj, path_obj, xmin, ymin, xmax, ymax)
			dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13a_UNDERSEGMETAZIONE', format='png')
		#-------------------------------------------------------------------------------------
		#---------------------------unisco spazi oversegmentati ------------------------------
	
		#unisco le spazi che sono state divisi erroneamente
		#fa schifissimo come metodo(nel caso lo utilizziamo per MCMCs)
		uniciStanzeOversegmentate = 2
		#1) primo controlla cella per cella 
		#2) unisce facendo una media pesata
		#3) non unisce le stanze, non fa assolutamente nulla, usato per mappe parziali se non voglio unire stanze
		if uniciStanzeOversegmentate ==1:
			#fa schifissimo come metodo(nel caso lo utilizziamo per MCMCs)

			#unione stanze
			#provo ad usare la distance transforme
			#dsg.disegna_distance_transform_e_stanze(distanceMap,stanze,colori, filepath = path_obj.filepath, savename = 'distance_and_stanze')
		
			#se esistono due spazi che sono collegati tramite un edge di una cella che ha un peso basso allora unisco quegli spazi
			plan.unisci_stanze_oversegmentate(plan_o)
			#cambio anche i colori
			dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13b_OVERSEGMENTAZIONE', format='png')	
		elif uniciStanzeOversegmentate == 2:
			#TODO: questo metodo funziona meglio del primo, vedere se vale la pena cancellare il primo
			#metodo molto simile a quello di Mura per il postprocessing		
			plan.postprocessing(plan_o, parametri_obj)#TODO: rinomina la funzione unisciOversegmentazione()
			dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13b_OVERSEGMENTAZIONE', format='png')	
		else:
			#se non voglio unire le stanze, ad esempio e' utile quando sto guardando le mappe parziali
			dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13b_OVERSEGMENTAZIONE', format='png')	
		#-------------------------------------------------------------------------------------	

	
	
	if par.mappa_completa ==False and trova_parziali==2:
		#secondo metodo per trovare gli spazi parziali. Fa una media pesata. migliore rispetto al primo ma bisogna fare tuning del parametro
		plan.trova_spazi_parziali_due(plan_o)
		
	if par.mappa_completa == False and trova_parziali==3:
		#terzo metodo per trovare le celle parziali basato sulla ricerca delle frontiere.
		start_time_frontiere = time.time()
		immagine_cluster, frontiere, labels, lista_pixel_frontiere = fr.ottieni_frontire_principali(img_ini)
		
		
		if len(labels) > 0:
			plan.trova_spazi_parziali_da_frontiere(plan_o, lista_pixel_frontiere, immagine_cluster, labels)
			#plan.trova_spazi_parziali_da_frontiere_v2(plan_o, lista_pixel_frontiere, immagine_cluster, labels)
			spazi = sp.trova_spazi_parziali(plan_o.spazi)
			
			
		end_time_frontiere = time.time()
		print "le frontiere impiegano:", end_time_frontiere - start_time_frontiere
		if par.DISEGNA:
			dsg.disegna_map(immagine_cluster,filepath = path_obj.filepath, savename = '0a_frontiere', format='png')
			dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13c_spazi_parziali', format='png')
			
			
	#------------------------------fine ricerca cella parziali-------------------------------------------------------	
	
	#-----------------------------calcolo peso per extended_segments----------------------
	
	#calcolo il peso di un extended segment in base alla copertura sei segmenti. Ovviamente non potra' mai essere 100%.
	extended_segments = sg.setPeso(extended_segments, walls)#TODO:controllare che sia realmente corretto
	#calcolo per ogni extended segment quante sono le stanze che tocca(la copertura)
	lay.calcola_copertura_extended_segment(extended_segments, plan_o.spazi)
	plan_o.set_extended_segments(extended_segments)
	
	#-------------------------------------------------------------------------------------	

	'''
	#---------------------------unisco spazi oversegmentati ------------------------------
	
	#unisco le spazi che sono state divisi erroneamente
	#fa schifissimo come metodo(nel caso lo utilizziamo per MCMCs)
	uniciStanzeOversegmentate = 2
	#1) primo controlla cella per cella 
	#2) unisce facendo una media pesata
	#3) non unisce le stanze, non fa assolutamente nulla, usato per mappe parziali se non voglio unire stanze
	if uniciStanzeOversegmentate ==1:
		#fa schifissimo come metodo(nel caso lo utilizziamo per MCMCs)

		#unione stanze
		#provo ad usare la distance transforme
		#dsg.disegna_distance_transform_e_stanze(distanceMap,stanze,colori, filepath = path_obj.filepath, savename = 'distance_and_stanze')
		
		#se esistono due spazi che sono collegati tramite un edge di una cella che ha un peso basso allora unisco quegli spazi
		plan.unisci_stanze_oversegmentate(plan_o)
		#cambio anche i colori
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13b_OVERSEGMENTAZIONE', format='png')	
	elif uniciStanzeOversegmentate == 2:
		#TODO: questo metodo funziona meglio del primo, vedere se vale la pena cancellare il primo
		#metodo molto simile a quello di Mura per il postprocessing		
		plan.postprocessing(plan_o, parametri_obj)
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13b_OVERSEGMENTAZIONE', format='png')	
	else:
		#se non voglio unire le stanze, ad esempio e' utile quando sto guardando le mappe parziali
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '13b_OVERSEGMENTAZIONE', format='png')	
	#-------------------------------------------------------------------------------------	
	'''
	
	copia_spazi=copy.deepcopy(plan_o.spazi)#copio la lista degli spazi(mi serve solo alla fine per stampare la predizione sopra questa)
	#------------------------------PREDIZIONE GEOMETRICA----------------------------------	
	#da qui comincia la parte di predizione, io la sposterei in un altro file
	
	#ricavo gli spazi parziali
	cellette_out = plan_o.cellette_esterne
	spazi_parziali = []
	for s in plan_o.spazi:
		if s.parziale == True:
			spazi_parziali.append(s)	
	
	#setto la parte di area predetta ottunuta gia' dal layout. e l'area originale di ogni stanza
	for s in plan_o.spazi:
		if s.parziale == True:
			area_predetta_lay = s.spazio.area -(s.spazio.intersection(contorno)).area
			area_originale_stanza = (s.spazio.intersection(contorno)).area
			s.set_area_originale(area_originale_stanza)
			s.set_area_predetta(s.area_predetta+area_predetta_lay)
			print "area predetta",s.area_predetta
			
	
		
	plan_o_2 = copy.deepcopy(plan_o)#copio l'oggetto per poter eseguire le azioni separatamente
	plan_o_3 = copy.deepcopy(plan_o)
	
	
	#metodo di predizione scelto. 
	#se MCMC == True si vuole predirre con il MCMC, altrimenti si fanno azioni geometriche molto semplici
	
	if par.MCMC ==True:
		# TODO:da eliminare, mi serviva solo per delle immagini e per controllare di aver fatto tutto giusto
		
		
		#TODO: MCMC rendilo una funzione privata o di un altro modulo, che se continui a fare roba qua dentro non ci capisci piu' nulla.
		
		#guardo quali sono gli extended che sto selezionando
		for index,s in enumerate(spazi_parziali):
			celle_di_altre_stanze = []
			for s2 in plan_o.spazi:
				if s2 !=s:
					for c in s2.cells:
						celle_di_altre_stanze.append(c)	
			
			#-----non serve(*)
			celle_circostanti = celle_di_altre_stanze + cellette_out #creo una lista delle celle circostanti ad una stanza
	
			a = sp.estrai_extended_da_spazio(s, plan_o.extended_segments, celle_circostanti)
			tot_segment = list(set(a))
			#dsg.disegna_extended_segments(tot_segment, walls,filepath = path_obj.filepath, format='png', savename = '7a_extended'+str(index))	
		
			#extended visti di una stanza parziale.
			b= sp.estrai_solo_extended_visti(s, plan_o.extended_segments, celle_circostanti)#estraggo solo le extended sicuramente viste
			tot_segment_visti = list(set(b))
			#dsg.disegna_extended_segments(tot_segment_visti, walls,filepath = path_obj.filepath, format='png', savename = '7b_extended'+str(index))	
			#-----fine(*)
			
			
			#computo MCMC sulla stanza in considerazione
			mcmc.computa_MCMC(s, plan_o, celle_di_altre_stanze, index,  xmin, ymin, xmax, ymax, path_obj)
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '14_MCMC', format='png')	

	
	if par.azione_complessa == True:
		#1) FACCIO AZIONE SEMPLICE 1 PER AGGIUNGERE CELLE VISTE DAL LASER
		#2) FACCIO AZIONE COMPLESSA: nel quale vado a creare l'intero spazio degli stati fino ad una certa iterazione.
		
		#-------------------------------AZIONE GEOMETRICA 1)----------------------------------
		#-----AGGIUNGO CELLE OUT A CELLE PARZIALI SOLO SE QUESTE CELLE OUT SONO STATE TOCCANTE DAL BEAM DEL LASER
		start_time_azione_1 = time.time()
		i=0
		nuovi_spazi = []
		for s in spazi_parziali:
		
			celle_confinanti = pgeom.estrai_celle_confinanti_alle_parziali(plan_o, s)#estraggo le celle confinanti alle celle interne parziali delle stanze parziali.
			print "le celle confinanti sono: ", len(celle_confinanti)	
	
			#unisco solo se le celle sono state toccate dal beam del laser
			celle_confinanti = plan.trova_celle_toccate_dal_laser_beam(celle_confinanti, immagine_cluster)
	
			#delle celle confinanti non devo unire quelle che farebbero sparire una parete.
			celle_confinanti, celle_elimina_pareti = pgeom.elimina_celle_con_parete_vista(celle_confinanti, s)
		
		
			'''
			#-----inizio parte aggiunta
			print "----------adf-asdfa--f-f-da-g-ad-asg-a-dg-ad-g-adf-g-----ga---a-f", len(celle_elimina_pareti)
		
			#creo delle nuove stanze se ho delle celle che mi eliminano delle pareti ma che comunque sono state colpite dal laserbean oltre che aggiungere all'oggetto plan_o metto quelle stanze ache in coda alla lista spazi_parziali per farli processare anche loro in seguito.
			ids=[]
			for spazio in plan_o.spazi:
				ids.append(spazio.id)
			max_id = np.amax(ids)
		
			nuovi_spazi = []
			for index,cella_parete in enumerate(celle_elimina_pareti):
				cella_poli = [cella_parete.cella]#per ora metto nella lista solo la cella poligono
				cella_corri = [cella_parete.c]#per ora metto nella lista solo la cella poligono
				stanza = cella_parete.cella #la stanza e' la cella stessa
				new_spazio = sp.Spazio(cella_poli, stanza, cella_corri, max_id+1+index)#creo il nuovo spazio
				new_spazio.set_out(False)
				new_spazio.set_parziale(True)
			
				#aggiungo lo spazio a nuovi_spazi
				nuovi_spazi.append(new_spazio)
	
			#vedo se ci sono spazi da unire
			uniti = nuovi_spazi[:]	
			sta = []
			for u in uniti:
				sta.append(u.spazio)
			i+=1
			dsg.disegna_stanze(sta, dsg.get_colors(uniti), xmin, ymin, xmax, ymax, format='png', filepath = path_obj.filepath, savename = '30_prova'+str(i))
		
			for index1,s1 in enumerate(nuovi_spazi):
				s1_temp = s1
				for index2, s2 in enumerate(uniti):	
					s2_temp = s2
					fatto = False
					if not s1.spazio.equals(s2.spazio):	
						print "mai1????"		
						for c1 in s1.cells:
							for c2 in s2.cells:
								if fc.adiacenti(c1.c,c2.c):
									print "mai2????"
									edge_com = fc.edge_comune(c1.c, c2.c)
									if edge_com.weight < 0.5:
										#unisco queste due stanze
										nuovo_spazio = unisci_spazi(s1_temp,s2_temp)
										fatto = True
										print "mai3????"
			
				if fatto==True:
					uniti.remove(s1_temp)
					uniti.remove(s2_temp)
					uniti.append(nuovo_spazio)
		
			print "----------adf-asdfa--f-f-daff-g-ad-asg-a-dg-ad-g-adf-g-----ga---a-f", len(set(uniti))
			for spazio in uniti:
				spazio.set_area_predetta(spazio.spazio.area-(spazio.spazio.intersection(contorno)).area)
				#spazio.set_cluster_frontiera()#non so 
				#spazio.set_tocco_bordo()#non so 
				spazio.set_area_originale((spazio.spazio.intersection(contorno)).area)
			
			#-----fine parte aggiunta
	
			'''
				
			#faccio una prova per unire una cella che e' toccata dal beam del laser.
			print "le celle confinanti che vorrei aggiungere con l'azione geometrica 1 sono: ", len(set(celle_confinanti))
			if len(celle_confinanti)>0:
				#unisco la cella allo spazio
				area_aggiunta = 0
				for cella in celle_confinanti:
					if cella.vedo_frontiera == True:
						sp.aggiungi_cella_a_spazio(s, cella, plan_o)
						area_aggiunta += cella.cella.area
				#assegno alla stanza l'area aggiunta
				s.set_area_predetta(s.area_predetta+area_aggiunta)
			
			
			#---------------------nuovo pezzo per creare stanze

			#provo a creare stanze nuove sulle celle che non sono state prese	
			#creo nuove stanze con una cella esterne se queste celle sono toccate dal laser bean
			crea_nuove_stanze = False
			if crea_nuove_stanze== True:
				ids=[]
				for spazio in plan_o.spazi:
					ids.append(spazio.id)
				max_id = np.amax(ids)
				celle_confinanti = []
				celle_confinanti = pgeom.estrai_celle_confinanti_alle_parziali(plan_o, s)#estraggo le celle confinanti alle celle interne parziali delle stanze parziali.
				print "le celle confinanti sono: ", len(celle_confinanti)	
	
				#unisco solo se le celle sono state toccate dal beam del laser
				celle_confinanti = plan.trova_celle_toccate_dal_laser_beam(celle_confinanti, immagine_cluster)
				print "le celle confinanti che vorrei aggiungere con l'azione geometrica 1 sono: ", len(set(celle_confinanti))
				
				celle_corrette = []
				for cella in celle_confinanti:
					if cella.vedo_frontiera == True:
						celle_corrette.append(cella)
				
				if len(celle_corrette)>0:
					for index,cella_parete in enumerate(celle_corrette):
						if cella_parete.vedo_frontiera ==True:
							cella_poli = [cella_parete.cella]#per ora metto nella lista solo la cella poligono
							cella_corrisp = [cella_parete.c]#per ora metto nella lista solo la facce
							stanza = copy.deepcopy(cella_parete.cella)
													
							#stanza = cella_parete.cella #la stanza e' la cella stessa
							new_spazio = sp.Spazio(cella_poli, stanza, cella_corrisp, max_id+1+index)#creo il nuovo spazio
							new_spazio.set_out(False)
							new_spazio.set_parziale(True)
							new_spazio.set_area_predetta(new_spazio.area_predetta+(new_spazio.spazio.area-(new_spazio.spazio.intersection(contorno)).area))
						
							plan.assegna_a_spazio_cluster_frontiera(new_spazio, lista_pixel_frontiere, immagine_cluster, labels)#cluster forntiera 
							#new_spazio.set_tocco_bordo() 
						
							trovato = False
							for cellette in new_spazio.cells:
								bordi = cellette.c.bordi
								for b in bordi:
									if b.cluster_spaziale == 'bordo1' or b.cluster_spaziale == 'bordo2' or b.cluster_spaziale == 'bordo3' or b.cluster_spaziale == 'bordo4': 
										new_spazio.set_tocco_bordo(True)
										trovato = True
							if trovato==False:
								new_spazio.set_tocco_bordo(False)
						
							
							new_spazio.set_area_originale((new_spazio.spazio.intersection(contorno)).area)
					
							#aggiungo lo spazio a nuovi_spazi
							if new_spazio.spazio.area >0:
								nuovi_spazi.append(new_spazio)
								spazi_parziali.append(new_spazio)
								plan_o.spazi.append(new_spazio)
								plan_o.cellette_esterne.remove(cella_parete)
				
			
				#-----------------------fine nuovo pezzo
				 
		end_time_azione_1 = time.time()	
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '14_azione_geom_1', format='png')
		
		
		
	
		
		
		#-----------------------------AZIONE COMPLESSA--------------------------------
		
		#---creo una struttura per calcolare il tempo necessario ad eseguire l'azione complessa
		lista_n_elementi = [] #inserisco il numero di elementi confinanti di ogni stanza
		lista_n_disposizioni_totali = [] #inserisco il numeri di disposizioni totali per ogni stanza
		lista_n_disposizioni_reali = [] #inserisco il numero di disposizioni legali per stanza
		lista_tempi = [] #tempo necessario a completare la stanza
		#---
		
		start_time_azione_complessa = time.time()
		for index,s in enumerate(spazi_parziali):
			start_time_stanza= time.time()
			
			#estraggo le celle delle altre stanze
			celle_di_altre_stanze = plan.estrai_celle_di_altre_stanze(s,plan_o)
									
			#creo il mio spazio degli stati
			level= 1 #questa e la profondita' con la quale faccio la mia ricerca, oltre al secondo livello non vado a ricercare le celle.
			
			elementi = pgeom.estrai_spazio_delle_celle(s, plan_o, level)
			elementi = pgeom.elimina_spazi_sul_bordo_da_candidati(elementi, plan_o) #per ora non considero elementi che toccano il bordo, perche' tanto non voglio aggiungerli e mi ingrandiscono lo spazio degli stati per nulla.
			lista_n_elementi.append(len(elementi))
			
			print "gli elementi sono:", len(elementi)
			print "-------inizio calcolo permutazioni-------"
			permutazioni = pgeom.possibili_permutazioni(elementi)
			lista_n_disposizioni_totali.append(len(permutazioni))
			print "-------fine calcolo permutazioni-------"
			print "il numero di permutazioni sono:", len(permutazioni)
			
			permutazioni_corrette = []
			if len(permutazioni)>0:
				#per ogni permutazione degli elementi devo controllare il costo che avrebbe il layout con l'aggiunta di tutte le celle di quella permutazione.
				#permutazioni_corrette = []
				score_permutazioni_corrette = []
				for indice,permutazione in enumerate(permutazioni):
					ok=False
				
					pgeom.aggiunge_celle_permutazione(permutazione, plan_o, s)#aggiungo le celle della permutazione corrente alla stanza
				
					#calcolo score
					score2_dopo = val.score2(s, plan_o, celle_di_altre_stanze)
					#calcolo penalita'
					penal1_dopo = val.penalita1(s)#piu' questo valore e' alto peggio e', valori prossimi allo zero indicano frome convesse.
					penal4_dopo = val.penalita4(s, plan_o, celle_di_altre_stanze)#conto il numero di extended che ci sono dopo aver aggiungere la permutazione, sfavorisce i gradini
				
					# il risultato potrebbe portare ad una stanza non Polygon, allora quella permutazione non e' valida 
					if type(s.spazio)== Polygon:
						ok = True
						permutazioni_corrette.append(permutazione)
						
						#elimino dalla lista delle permutazioni tutte quelle permutazioni che hanno gli stessi elementi
						for p in permutazioni:
							vuoto= list(set(p)-set(permutazione))
							if len(vuoto)==0 and len(p)== len(permutazione) and p!= permutazione:
								permutazioni.remove(p)
						
						#------------valuto il layout con permutazione aggiunta---------------
				
						score = val.score_function(score2_dopo, penal1_dopo, penal4_dopo)#non ancora implementata fino alla fine
						score_permutazioni_corrette.append(score)
				
						#----------------------fine valutazione-----------------------------------
					
						#disegno 
						#dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = 'permutazioni/14_stanza'+str(index)+'permutazioni_'+str(indice)+'_a', format='png')#TODO:DECOMMENTA SE NON SEI IN BATCH
					else:
						#elimina la permutazione perche' non e' valida
						permutazioni.remove(permutazione)
				
					#------			
					pgeom.elimina_celle_permutazione(permutazione, plan_o, s)
					if ok ==True:
						a=0
						#dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = 'permutazioni/14_stanza'+str(index)+'permutazioni_'+str(indice)+'_b', format='png')#TODO:DECOMMENTA SE NON SEI IN BATCH
					#------	
					print "permutazione", indice
				
				
				#valuto la permutazione che mi permette di minimizzare lo score
				if len(score_permutazioni_corrette)>0:
					#min_score = np.amin(score_permutazioni_corrette)
					max_score = np.amax(score_permutazioni_corrette)#ADDED
					#print "min_core", min_score
					print "max_score", max_score
					#posizione_permutazione = score_permutazioni_corrette.index(min_score)
					posizione_permutazione = score_permutazioni_corrette.index(max_score)#ADDED
					permutazione_migliore = permutazioni_corrette[posizione_permutazione]
			
					#ottenuto lo score migliore lo confronto con lo score del layout originale e guardo quale a' migliore
					#calcolo score del layout originale, senza previsioni
					score2_prima = val.score2(s, plan_o, celle_di_altre_stanze)
					penal1_prima = val.penalita1(s)#piu' questo valore e' alto peggio e', valori prossimi allo zero indicano frome convesse.	
					penal4_prima = val.penalita4(s, plan_o, celle_di_altre_stanze)#conto il numero di extended che ci sono prima di aggiungere la permutazione
					score_originale = val.score_function(score2_prima, penal1_prima, penal4_prima)#non ancora implementata fino alla fine
					print "score_originale", score_originale
			
					# if min_score<=score_originale:
# 						#preferisco fare una previsione
# 						permutazione_migliore = permutazione_migliore
# 						pgeom.aggiunge_celle_permutazione(permutazione_migliore, plan_o, s)
# 					else:
# 						#il layout originale ottenuto e' migliore di tutti gli altri, non faccio nessuana previsione per la stanza corrente
# 						pass
					if max_score >= score_originale:
						#preferisco fare una previsione
						permutazione_migliore = permutazione_migliore
						#calcolo l'area della permutazione (che non e' altro che l'area della predizione)
						area_predetta = 0
						for el in permutazione_migliore:
							area_predetta += el.cella.area
						#assegno alla stanza l'area predetta
						s.set_area_predetta(s.area_predetta+area_predetta)
						#aggiungo le celle della permutazione alla stanza
						pgeom.aggiunge_celle_permutazione(permutazione_migliore, plan_o, s)
					else:
						#il layout originale ottenuto e' migliore di tutti gli altri, non faccio nessuana previsione per la stanza corrente
						pass
				else:
					#non ho trovato permutazioni che hanno senso, allora lascio tutto come e'
					pass
				
			end_time_stanza = time.time()
			lista_tempi.append(end_time_stanza - start_time_stanza) #tempo necessario a computare questa stanza parziale
			lista_n_disposizioni_reali.append(len(permutazioni_corrette))
			
			#disegno le computazioni migliori TODO: momentaneo, solo perche' in questo momento uso solo la penalita' della convessita'		
			#dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '14_stanza'+str(index)+'azione_complessa', format='png') #TODO: se voglio vedere quale stanza e'  stata fatta devo decommentare questa riga
			
			#---------------------------FINE AZIONE COMPLESSA-----------------------------		
			
# 			for r in permutazioni:
# 				print r
# 			print "\n\n"
# 			
# 			poligoni= []
# 			colori=[]
# 			pari =0
# 			for ele in elementi:
# 				poligoni.append(ele.cella)
# 				if pari%2 ==0:
# 					colori.append('#800000')
# 				else:
# 					colori.append('#A00000')
# 			print "il nuemro di poligoni all'esterno sono: ", len(poligoni)
# 			dsg.disegna_stanze(poligoni,colori , xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '15_poligoni_esterni_stanza'+str(index), format='png')	
		end_time_azione_complessa = time.time()
	#stampo il layout finale
	dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '15_azione_complessa', format='png')
	dsg.disegna_spazi_con_pareti_nascoste(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,edges,filepath = path_obj.filepath, savename = '15_azione_complessa_con_pareti_nascoste', format='png')

			
		
	if par.azioni_semplici==True:
		#------------------------------AZIONE GEOMETRICA 1)+2)--------------------------------	
	
		#-------------------------------AZIONE GEOMETRICA 1)----------------------------------
		#-----AGGIUNGO CELLE OUT A CELLE PARZIALI SOLO SE QUESTE CELLE OUT SONO STATE TOCCANTE DAL BEAM DEL LASER
		
		celle_candidate = []
		for s in spazi_parziali:
			celle_confinanti = pgeom.estrai_celle_confinanti_alle_parziali(plan_o, s)#estraggo le celle confinanti alle celle interne parziali delle stanze parziali.
			print "le celle confinanti sono: ", len(celle_confinanti)	
		
			#unisco solo se le celle sono state toccate dal beam del laser
			celle_confinanti = plan.trova_celle_toccate_dal_laser_beam(celle_confinanti, immagine_cluster)
		
			#delle celle confinanti non devo unire quelle che farebbero sparire una parete.
			celle_confinanti, celle_elimina_pareti = pgeom.elimina_celle_con_parete_vista(celle_confinanti, s)
			
		
			#faccio una prova per unire una cella che e' toccata dal beam del laser.
			if len(celle_confinanti)>0:
				#unisco la cella allo spazio
				for cella in celle_confinanti:
					if cella.vedo_frontiera == True:
						sp.aggiungi_cella_a_spazio(s, cella, plan_o)
				
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '14_azione_geom_1', format='png')	

		#-------------------------------AZIONE GEOMETRICA 2)-----------------------------------	
		#--UNISCO LE CELLE IN BASE ALLE PARETI CHE CONDIVIDONO CON ALTRE STANZE 
	
		for s in spazi_parziali:
			#estraggo le celle out che confinano con le celle parziali
			celle_confinanti = pgeom.estrai_celle_confinanti_alle_parziali(plan_o, s)#estraggo le celle confinanti alle celle interne parziali delle stanze parziali.
			print "le celle confinanti sono: ", len(celle_confinanti)
		
			#delle celle confinanti appena estratte devo prendere solamente quelle che hanno tutti i lati supportati da una extended line
			celle_confinanti = pgeom.estrai_celle_supportate_da_extended_segmement(celle_confinanti, s, plan_o.extended_segments)
		
			#delle celle confinanti non devo unire quelle che farebbero sparire una parete.
			celle_confinanti, celle_elimina_pareti = pgeom.elimina_celle_con_parete_vista(celle_confinanti, s)
		
		
			#unisco solo quelle selezionate
			#TODO questa parte e' da cancellare
			if len(celle_confinanti)>0:
				#unisco la cella allo spazio
				for cella in celle_confinanti:
					sp.aggiungi_cella_a_spazio(s, cella, plan_o)
		
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '14_azione_geom_1_piu_geom_2', format='png')	


		#----------------------------------FINE 1)+2)-----------------------------------------
		
	
		#----------------------------FACCIO SOLO AZIONE GEOM 2)-------------------------------
		#questa azione la faccio su una copia di plan
	
		#ricavo gli spazi parziali dalla copia di plan_o che sono esattamente una copia di spazi_parziali precedente.
		cellette_out = plan_o_2.cellette_esterne
		spazi_parziali = []
		for s in plan_o_2.spazi:
			if s.parziale == True:
				spazi_parziali.append(s)
		
		cella_prova =None
		spp = None#eli
		for s in spazi_parziali:
			#estraggo le celle out che confinano con le celle parziali
			celle_confinanti = pgeom.estrai_celle_confinanti_alle_parziali(plan_o_2, s)#estraggo le celle confinanti alle celle interne parziali delle stanze parziali.
			print "le celle confinanti sono: ", len(celle_confinanti)
		
			#delle celle confinanti appena estratte devo prendere solamente quelle che hanno tutti i lati supportati da una extended line
			celle_confinanti = pgeom.estrai_celle_supportate_da_extended_segmement(celle_confinanti, s, plan_o_2.extended_segments)
			print "le celle confinanti sono2: ", len(celle_confinanti)
			#delle celle confinanti non devo unire quelle che farebbero sparire una parete.
			celle_confinanti, celle_elimina_pareti = pgeom.elimina_celle_con_parete_vista(celle_confinanti, s)
			print "le celle confinanti sono3: ", len(celle_confinanti)
			#unisco solo quelle selezionate
			#TODO questa parte e' da cancellare
			if len(celle_confinanti)>0:
				#unisco la cella allo spazio
				for cella in celle_confinanti:
					sp.aggiungi_cella_a_spazio(s, cella, plan_o_2)
					cella_prova = cella#elimina
					spp = s#elimina
		
		dsg.disegna_spazi(plan_o_2.spazi, dsg.get_colors(plan_o_2.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '14_azione_geom_2', format='png')	
		#----------------------------------FINE SOLO AZIONE GEOM 2)--------------------------
		
	
	#inserisco alle stanze parziali l'informazione sul toccare il bordo dell'immagine (solo se e' una stanza parziale)
	for spazio in plan_o.spazi:
		if spazio.parziale == True:	
			trovato = False
			for cellette in spazio.cells:
				bordi = cellette.c.bordi
				for b in bordi:
					if b.cluster_spaziale == 'bordo1' or b.cluster_spaziale == 'bordo2' or b.cluster_spaziale == 'bordo3' or b.cluster_spaziale == 'bordo4': 
						spazio.set_tocco_bordo(True)
						trovato = True
			if trovato==False:
				spazio.set_tocco_bordo(False)
		else:
			spazio.set_tocco_bordo(False)
		
					
	
	
	
	'''
	#------------------------------GRAFO TOPOLOGICO---------------------------------------
	
	#questa parte commentata (GRAFO TOPOLOGICO)la devo fare alla fine di tutto. 
	
	#riottengo tutti i dati che mi  servono (dato che ho cambiato la struttura dati)
	stanze = []
	for s in plan_o.spazi:
		if s.parziale != False:
			stanze.append(s.spazio)
	
	#costruisco il grafo 
	(stanze_collegate, doorsVertices, distanceMap, points, b3) = gtop.get_grafo(path_obj.metricMap, stanze, estremi, colori, parametri_obj)
	(G, pos) = gtop.crea_grafo(stanze, stanze_collegate, estremi, colori)
	#ottengo tutte quelle stanze che non sono collegate direttamente ad un'altra, con molta probabilita' quelle non sono stanze reali
	stanze_non_collegate = gtop.get_stanze_non_collegate(stanze, stanze_collegate)
	
	#ottengo le stanze reali, senza tutte quelle non collegate
	stanze_reali, colori_reali = lay.get_stanze_reali(stanze, stanze_non_collegate, colori)#TODO: questo non serve piu'(verifica)
	
	#setto gli spazi come out se non sono collegati a nulla.	
	spazi = sp.get_spazi_reali_v2(spazi, stanze_reali) #elimino dalla lista di oggetti spazio quegli spazi che non sono collegati a nulla.
	
	if par.DISEGNA:
		#sto disegnando usando la lista di colori originale, se voglio la lista della stessa lunghezza sostituire colori con colori_reali
		dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '16_spazi_collegati', format='png')
		#dsg.disegna_stanze(stanze_reali, colori_reali, xmin, ymin, xmax, ymax,filepath = path_obj.filepath, savename = '8_Stanze_reali', format='png')	
	#------------------------------------------------------------------------------------
	if par.DISEGNA:
		dsg.disegna_distance_transform(distanceMap, filepath = path_obj.filepath, format='png')
		dsg.disegna_medial_axis(points, b3, filepath = path_obj.filepath, format='png')
		dsg.plot_nodi_e_stanze(dsg.get_colors(plan_o.spazi),estremi, G, pos, stanze, stanze_collegate, filepath = path_obj.filepath, format='png')
	
	#-----------------------------fine GrafoTopologico------------------------------------
	'''
	if par.DISEGNA:
		#disegno la mappa parziale segmentata con sovrapposta la mappa predetta ed il contorno
		dsg.disegna_sovrapposizione_predizione(copia_spazi, plan_o.spazi, contours , dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax, filepath = path_obj.filepath, format='png')

	
	
	'''
	#per ora non creo i pickle tanto non li sto usando
	start_time_pickle = time.time()	
	#------------------------CREO PICKLE--------------------------------------------------
	#creo i file pickle per il layout delle stanze
	print("creo pickle layout")
	pk.crea_pickle((stanze, clustersCelle, estremi, colori, spazi, stanze_reali, colori_reali), path_obj.filepath_pickle_layout)
	print("ho finito di creare i pickle del layout")
	#creo i file pickle per il grafo topologico
	print("creo pickle grafoTopologico")
	pk.crea_pickle((stanze, clustersCelle, estremi, colori), path_obj.filepath_pickle_grafoTopologico)
	print("ho finito di creare i pickle del grafo topologico")
	
	end_time_pickle = time.time()
	print "il tempo necessatrio a creare i pickle e': ", end_time_pickle - start_time_pickle
	'''
	
	#-----------------------CALCOLO ACCURACY----------------------------------------------

	if par.mappa_completa:
		#funzione per calcolare accuracy fc e bc
		print "Inizio a calcolare metriche"
		results, stanze_gt = ac.calcola_accuracy(path_obj.nome_gt,estremi,stanze_reali, path_obj.metricMap,path_obj.filepath, parametri_obj.flip_dataset)	
		#results, stanze_gt = ac.calcola_accuracy(path_obj.nome_gt,estremi,stanze, path_obj.metricMap,path_obj.filepath, parametri_obj.flip_dataset)	

		if par.DISEGNA:
			dsg.disegna_grafici_per_accuracy(stanze, stanze_gt, filepath = path_obj.filepath, format='png')
		print "Fine calcolare metriche"
	
	else:
		#setto results a 0, giusto per ricordarmi che non ho risultati per le mappe parziali 
		results_accuracy = 0 #TODO: ricordati che devi eliminarlo una volta che inserisci i veri valori
		#stanze_gt = ac.get_stanze_gt(path_obj.nome_gt, estremi, flip_dataset = False)
		stanze_gt, ids_gt = acpar.get_stanze_gt(path_obj.nome_gt) #prelevo tutte le stanze gt dall'xml, nella lista ids_gt ci sono tutti gli id delle stanze gt
		

		#ottenute le stanze gt provo ad adattare le due immagini
		stanze_complete = [] #in questa lista ci sono solo le stanze del mio layout che non sono parziali
		stanze = []
		spazi = []
		indici_stanze_parziali = []
		for s in plan_o.spazi:
			if s.out == False: #se la stanza e' collegata a qualcosa
				stanze.append(s.spazio)
				spazi.append(s)
			if s.parziale == False:
				stanze_complete.append(s.spazio)
		#creo xml stanze 			
		id_stanze = xmlutils.crea_xml(path_obj.filepath+'18_xml_segmentazione.xml',spazi)#id stanze e' ordinato come spazi e possiede l'id univo assegnato alla stanza
			
		#stanze_simili, stanze_gt_simili, lista_gt_proporzionata = acpar.adatta_scala_stanze_gt(stanze_gt, stanze_complete)
		lista_gt_proporzionata = acpar.adatta_scala_stanze_gt_v2(stanze_gt, stanze_complete) #questa versione crea tutte le combinazioni di mappa gt proporzionate, diverse per ogni stanza completa
		
		#innanzitutto elimina dalla lista_gt_proporzionata alcune configurazioni scorrette al 100% e ne lascio solo alcune
		#se ad esempio una stanza reale non e' coperta da una stanza per una certa percentuale elimino quella configurazione
		lista_gt_proporzionata = acpar.elimina_configurazioni_errate(stanze_complete, lista_gt_proporzionata) #TODO: secondo me usando tutte le stanze invece che solo le stanze complete funziona meglio(mettere al posto di stanza_complete la lista di tutte le stanze)
		
		#calcolo percentuali di completamento della mappa ed indici tra gt e mappa segmentata queste sono liste di liste
		lista_percentuali_completamento_mappa_bwd, lista_percentuali_completamento_mappa_fwd, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd, lista_indici_corrispondenti_fwd, lista_indici_corrispondenti_bwd, lista_precisions, lista_recalls = acpar.calcola_percentuali_completamento_mappa(spazi, lista_gt_proporzionata)
		
		'''
		#cerco la massima percentuale bwd e fwd che ci sono nelle liste delle percentuali
		#questa porzione mi serve per sfoltire il numero di configurazioni lasciano solo le migliori
		max_bwd = max(lista_percentuali_completamento_mappa_bwd)
		max_fwd = max(lista_percentuali_completamento_mappa_fwd)
		indice_conf_bwd = lista_percentuali_completamento_mappa_bwd.index(max_bwd)
		indice_conf_fwd = lista_percentuali_completamento_mappa_fwd.index(max_fwd)
		#TODO: devo sistemare la lunghezza delle liste correlate a lista_gt_proporzionata con solo le due configurazioni corrette, in questo momento stampo solo quelle importanti
		#lista_gt_proporzionata = [lista_gt_proporzionata[indice_conf_bwd], lista_gt_proporzionata[indice_conf_fwd]] 
		'''
		
				
		#per ogni configurazione creo il dizionario con le informazioni delle stanze parziali 
		lista_dizionari_configurazione = acpar.calcolo_informazioni(spazi, lista_gt_proporzionata, lista_indici_corrispondenti_fwd, ids_gt, id_stanze, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd, lista_percentuali_completamento_mappa_bwd, lista_percentuali_completamento_mappa_fwd, lista_precisions, lista_recalls, contorno)


		#per ogni accuracy che ho trovato, prendo solo quelle che hanno 0.5*bwd + 0.5*fwd maggiori. I primi tre
		lista_indici_tre_accuracy_migliori = [] #in questa lista ci sono i tre indici in lista_gt_proporzionata che possiedono le migliori accuracy
		max_val_1 = 0
		indice = 0
		i=0
		for perc_mappa_bwd, perc_mappa_fwd, perc_GT_bwd, perc_GT_fwd in zip(lista_percentuali_completamento_mappa_bwd,lista_percentuali_completamento_mappa_fwd, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd):
			valore_mappa = (perc_mappa_bwd*0.5)+(perc_mappa_fwd * 0.5)
			valore_gt = (perc_GT_bwd*0.5) + (perc_GT_fwd*0.5)
			valore = valore_mappa*0.5 + valore_gt*0.5
			if valore >max_val_1:
				max_val_1 = valore
				indice = i
			i+=1
		lista_indici_tre_accuracy_migliori.append(indice)
		
		max_val_2 = 0
		indice = 0
		i=0
		for perc_mappa_bwd, perc_mappa_fwd, perc_GT_bwd, perc_GT_fwd in zip(lista_percentuali_completamento_mappa_bwd,lista_percentuali_completamento_mappa_fwd, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd):
			valore_mappa = (perc_mappa_bwd*0.5)+(perc_mappa_fwd * 0.5)
			valore_gt = (perc_GT_bwd*0.5) + (perc_GT_fwd*0.5)
			valore = valore_mappa*0.5 + valore_gt*0.5
			if valore > max_val_2 and valore < max_val_1:
				max_val_2 = valore
				indice = i
			i+=1
		lista_indici_tre_accuracy_migliori.append(indice)
		
		max_val_3 = 0
		indice = 0
		i=0
		for perc_mappa_bwd, perc_mappa_fwd, perc_GT_bwd, perc_GT_fwd in zip(lista_percentuali_completamento_mappa_bwd,lista_percentuali_completamento_mappa_fwd, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd):
			valore_mappa = (perc_mappa_bwd*0.5)+(perc_mappa_fwd * 0.5)
			valore_gt = (perc_GT_bwd*0.5) + (perc_GT_fwd*0.5)
			valore = valore_mappa*0.5 + valore_gt*0.5
			if valore > max_val_3 and valore < max_val_2:
				max_val_3 = valore
				indice = i
			i+=1
		lista_indici_tre_accuracy_migliori.append(indice)			
			
		if par.DISEGNA:
			
			SAVE_FOLDER = os.path.join(path_obj.filepath, 'accuracy_imm')
			if not os.path.exists(SAVE_FOLDER):
				os.mkdir(SAVE_FOLDER)
			for index, gt_prorp in enumerate(lista_gt_proporzionata):
				if index == lista_indici_tre_accuracy_migliori[0] or index == lista_indici_tre_accuracy_migliori[1] or index == lista_indici_tre_accuracy_migliori[2]:
					#disegno la configurazione
					if index == lista_indici_tre_accuracy_migliori[0]:
						posizione = 'pos0'
					elif index == lista_indici_tre_accuracy_migliori[1]:
						posizione = 'pos1'
					else:
						posizione = 'pos2'
					dsg.disegna_grafici_per_accuracy(stanze, gt_prorp, filepath = path_obj.filepath, format='png', savename = 'accuracy_imm/9_accuracy_'+str(index)+posizione)
			#disegno anche il contorno sopra 
			dsg.disegna_stanze_stanzeGt_contorno(stanze, lista_gt_proporzionata[lista_indici_tre_accuracy_migliori[0]], contours, filepath = path_obj.filepath, format='png', savename = '19_St_Gt_contorno')
			#dsg.disegna_stanza_vuote(stanze, filepath = path_obj.filepath, format='png', savename = '19_b_stanze', nero=True)
			#dsg.disegna_stanza_vuote(lista_gt_proporzionata[lista_indici_tre_accuracy_migliori[0]], filepath = path_obj.filepath, format='png', savename = '19_b_GT', nero=False)

			
			i = 0
			for perc_mappa_bwd, perc_mappa_fwd, perc_GT_bwd, perc_GT_fwd in zip(lista_percentuali_completamento_mappa_bwd, lista_percentuali_completamento_mappa_fwd, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd):
				if i == lista_indici_tre_accuracy_migliori[0] or i == lista_indici_tre_accuracy_migliori[1] or i == lista_indici_tre_accuracy_migliori[2]:
					if i == lista_indici_tre_accuracy_migliori[0]:
						posizione = 'pos0'
					elif i == lista_indici_tre_accuracy_migliori[1]:
						posizione = 'pos1'
					else:
						posizione = 'pos2'
					
					#creo il file con i dati che voglio visualizzare
					f = open(path_obj.filepath+'accuracy_imm/9_accuracy_'+str(i)+posizione+'.txt','a')
					f.write(path_obj.filepath+'/'+ path_obj.metricMap+'\n')
					f.write('n_configurazione = '+str(i)+'\n')
					f.write('perc_mappa_bwd = '+str(perc_mappa_bwd)+'%\n')
					f.write('perc_mappa_fwd = '+str(perc_mappa_fwd)+'%\n')
					f.write('perc_GT_bwd = '+str(perc_GT_bwd)+'%\n')
					f.write('perc_GT_fwd = '+str(perc_GT_fwd)+'%\n\n')
					f.close()
				i+=1
				
			for index, dizionario in enumerate(lista_dizionari_configurazione):
				if index == lista_indici_tre_accuracy_migliori[0] or index == lista_indici_tre_accuracy_migliori[1] or index == lista_indici_tre_accuracy_migliori[2]:
					if index == lista_indici_tre_accuracy_migliori[0]:
						posizione = 'pos0'
					elif index == lista_indici_tre_accuracy_migliori[1]:
						posizione = 'pos1'
					else:
						posizione = 'pos2'
					chiavi = dizionario.keys()
					f = open(path_obj.filepath+'accuracy_imm/9_accuracy_'+str(index)+posizione+'.txt','a')
					print "chiavi", len(chiavi)
					for chiave in chiavi:
						f.write('------------------------\n informazioni stanza parziale\n')
						f.write('id_della_stanza_XML_GT = '+str(chiave)+'\n')
						f.write('id_della_stanza_XML_predizione = '+str(dizionario[chiave][0])+'\n')
						f.write('area_predetta = '+str(dizionario[chiave][1])+'\n')
						f.write('area_vera= '+str(dizionario[chiave][2])+'\n')
						f.write('area_vera_esplorata = '+str(dizionario[chiave][3])+'\n')
						f.write('percentuale_area_vera_esplorata = '+str(dizionario[chiave][4])+'\n')
						f.write('percentuale_area_totale_ambiente_esplorata_bwd = '+str(dizionario[chiave][5])+'\n')
						f.write('percentuale_area_totale_ambiente_esplorata_fwd = '+str(dizionario[chiave][6])+'\n')
						f.write('percentuale_matching_mappa_bwd = '+str(dizionario[chiave][7])+'\n')
						f.write('percentuale_matching_mappa_fwd = '+str(dizionario[chiave][8])+'\n')
						f.write('area_intersezione_tra_stanza_originale_e_stanza_predetta = '+str(dizionario[chiave][9])+'\n')
						
						#nuove metriche
						f.write('area_unione_tra_stanza_originale_e_stanza_predetta = '+str(dizionario[chiave][10])+'\n')
						f.write('IoU = '+str(dizionario[chiave][11])+'\n')
						f.write('area_stanza_GT_esplorata = '+str(dizionario[chiave][12])+'\n')#percentuale esplorata della stanza calcolata come intersezione con il contorno
						f.write('area_mappa_GT_intersezione_contorno = '+str(dizionario[chiave][13])+'\n')#percentuale esplorata della mappa calcolata come intersezione di tutta la mappa Gt con il contorno.
						f.write('IoU filtrato dal contorno = '+str(dizionario[chiave][14])+'\n')
						f.write('tocco bordo = '+str(dizionario[chiave][15])+'\n')#tocca il bordo?
						f.write('IoU_filtrata_2 = '+str(dizionario[chiave][16])+'\n')#IoU_filtrata_ con il secondo metodo, quello in cui tolgo alla stanza parziale tutte le altre stanze GT che non centrano
						

					f.flush()
					
					#salvo il dizionario delle tra migliori configurazioni in un pickle
					#creo i file pickle per il layout delle stanze
					print("creo pickle del dizionario")
					pk.crea_pickle((dizionario), path_obj.filepath+'accuracy_imm/9_accuracy_'+str(index)+posizione+'pickle.pkl')
					print("ho finito di creare il pickle dei dizionari")
		
		calcolo_metriche_frontiere = False			
		if calcolo_metriche_frontiere ==True:		
			#-----------------------CALCOLO METRICHE FORNTIERE-------------------------------
			#calcolo metriche sulle frontiere metchando la frontiera sulla stanza GT corrispondednte(questo rappresenta il valore con cui mi devo confrontare)
			best_stanze_gt = lista_gt_proporzionata[lista_indici_tre_accuracy_migliori[0]]#non e' una copia
		
			#stanze_gt_con_frontiera, ordinamento_frontiere = mf.trova_spazi_gt_da_frontiere(best_stanze_gt, lista_pixel_frontiere, immagine_cluster, labels) #estraggo le stanze gt che hanno una frontiera
			stanze_gt_con_frontiera, ordinamento_frontiere, lista_pixel_frontiere = mf.trova_spazi_gt_da_frontiere_versione_2(best_stanze_gt, lista_pixel_frontiere, immagine_cluster, labels) #estraggo le stanze gt che hanno una frontiera

			print "provo a vedere se e' vuota: ", len(stanze_gt_con_frontiera)
			print "deve essere uguale", len(ordinamento_frontiere)
			trovato = False
			for index,fro in enumerate(ordinamento_frontiere):
				for index2,fr2 in enumerate(ordinamento_frontiere):
					if fro == fr2 and index != index2:
						trovato = True
			print "trovato deve essere False", trovato
				
		
			dsg.disegna_GT_parziali(best_stanze_gt, stanze_gt_con_frontiera, format='png', filepath = path_obj.filepath, savename = '20_stanzeGT')
			dsg.disegna_area_reale_GT_parziali(best_stanze_gt, stanze_gt_con_frontiera,contorno,xmin,ymin,xmax,ymax, format='png', filepath = path_obj.filepath, savename = '20_a_stanzeGT_contorno')
		
			#---METRICA MIO METODO: seleziona la frontiera con il mio metodo
		
			frontiera_scelta_mio_metodo=None #il mio metodo sceglie una sola frontiera o nessuna
			frontiere_sul_bordo = []
		
			spazi = plan_o.spazi
			spazi_parziali = []
			for s in spazi:	
				if s.parziale == True:
					spazi_parziali.append(s)
			'''
			for stanza_parziale in spazi_parziali:
				for celletta in stanza_parziale.cells:
					bordi = celletta.c.bordi
					for b in bordi:
						if b.cluster_spaziale == 'bordo1' or b.cluster_spaziale == 'bordo2' or b.cluster_spaziale == 'bordo3' or b.cluster_spaziale == 'bordo4':
							#ho trovato la stanza con la frontiera che tocca il bordo dell'immagine
							frontiera_scelta_mio_metodo = stanza_parziale.cluster_frontiera
			'''
			for stanza_parziale in spazi_parziali:
				lunghezza = 0
				for celletta in stanza_parziale.cells:
					bordi = celletta.c.bordi	
					for b in bordi:
						x1=b.x1
						y1=b.y1
						x2=b.x2
						y2=b.y2
						if b.cluster_spaziale == 'bordo1' or b.cluster_spaziale == 'bordo2' or b.cluster_spaziale == 'bordo3' or b.cluster_spaziale == 'bordo4':
							#ho trovato la stanza con la frontiera che tocca il bordo dell'immagine
							lunghezza = lunghezza + sg.lunghezza(x1,y1,x2,y2)
				if lunghezza>0:
					frontiere_sul_bordo.append((stanza_parziale.cluster_frontiera, lunghezza))		#e' una lista con una tupla (cluster_frontiera, lunghezza_bordo)					
			#seleziono la mia migliore forntiera
			print "frontiere sul bordo: ", frontiere_sul_bordo
			
			if len(frontiere_sul_bordo) >0:
				max = 0	
				for coppia in frontiere_sul_bordo: #coppia = (cluster_frontiera, lunghezza_bordo)
					if 	coppia[1]>max:
						max=coppia[1]
				for coppia in frontiere_sul_bordo:
					if coppia[1]==max:
						frontiera_scelta_mio_metodo = coppia[0]		
					
			print "il cluster della frontiera che ho trovato e': ", frontiera_scelta_mio_metodo
			print "le forntiera che ho sono"
			for frontiera in ordinamento_frontiere:
				print frontiera
			
			#questa parte associa ad ogni frontiera di una stanza parziale l'area predetta della stanza stessa
			#in teoria se una forntiera e' in piu' stanze parziali allora sommo le aree
			'''
			#senza sommare le aree
			area_predetta_mio_metodo = []
			for front in ordinamento_frontiere:
				for st_parziale in spazi_parziali:
					if st_parziale.cluster_frontiera == front:
						#in questa stanza c'e' questa frontiera
						area_predetta_mio_metodo.append(st_parziale.area_predetta)
			'''
			#sommando le aree
			area_predetta_mio_metodo = []
			for front in ordinamento_frontiere:
				area_predetta_totale = 0 
				for st_parziale in spazi_parziali:
					if st_parziale.cluster_frontiera == front:
						#in questa stanza c'e' questa frontiera
						area_predetta_totale += st_parziale.area_predetta
						print "area_predetta_totale", area_predetta_totale
				area_predetta_mio_metodo.append(area_predetta_totale)
			print area_predetta_mio_metodo	
			
			#---METRICA 1: FRONTIERA VERA
			#rappresenta l'area che non ho ancora esplorato della stanza Gt che possiede una frontiera. Sarebbe la vera area che posso trovare
			area_frontiera_vera = [] #questa lista e' ordinata come stanze_gt_con_frontiera. La froniera e' associata alla stanzaGT trovata
			for stanza_gt in stanze_gt_con_frontiera:
				intersezione = contorno.intersection(stanza_gt)
				area_totale_vera = stanza_gt.area - intersezione.area
				area_frontiera_vera.append(area_totale_vera)
				print "l'area che dovrei vedere e':", area_totale_vera
			
			#---METRICA 2: metodo cerchio 
			#ricerco centro delle frontiere
			area_metrica_2 = [] #lista con le aree ottenute con il metodo 2
			centri_frontiera = []
			centri_frontiere_non_flippati =[]
			pixel_coord_per_frontiera = []
		
			for cluster_frontiera in ordinamento_frontiere:
				centro_x = 0
				centro_y = 0
				conta = 0
				pixel_coord = []
				for pixel in lista_pixel_frontiere:
					if pixel.cluster  == cluster_frontiera:

						centro_x +=pixel.x
						centro_y +=pixel.y
						conta +=1
						pixel_coord.append([pixel.x, pixel.y])
			
				pixel_coord_per_frontiera.append(pixel_coord)			
				centro_x = centro_x /conta
				centro_y = centro_y /conta
			
				centri_frontiera.append([centro_x,centro_y])
				centri_frontiere_non_flippati.append([centro_x,centro_y])#serve dopo per andare sulla mappa rgb
				print "centro del pixel = ", centro_x, centro_y
			
			#flippo le coordinate della frontiera
			for fro in pixel_coord_per_frontiera:
				for c in fro:
					c[1] = img_rgb.shape[0]-1 - c[1]
			for fro in pixel_coord_per_frontiera:
				for c in fro:
					altezza = len(img_rgb)
					y_p2 = - c[0]+ altezza
					x_p2 = - c[1]+ altezza
					c[0] = x_p2
					c[1] = y_p2
		
			for c in centri_frontiera:
				c[1] = img_rgb.shape[0]-1 - c[1]
			for c in centri_frontiera:
				altezza = len(img_rgb)
				y_p2 = - c[0]+ altezza
				x_p2 = - c[1]+ altezza
				c[0] = x_p2
				c[1] = y_p2	
			for index, pixel_coord in enumerate(pixel_coord_per_frontiera):
				dsg.disegna_contorno_e_centro_frontiera(vertici,pixel_coord,xmin,ymin,xmax,ymax, format='png', filepath = path_obj.filepath, savename = '21_Contorno_e_frontiere_n_'+str(index))	
			dsg.disegna_contorno_e_centro_frontiera(vertici,centri_frontiera,xmin,ymin,xmax,ymax, format='png', filepath = path_obj.filepath, savename = '21_Contorno_e_centro_frontiere')	
		
			#disegno poligoni cerchio con centro nei centri delle frontiere e guardo le intersezioni con le stanze
			r = parametri_obj.raggio_azione #e' il raggio della circonferenza
		
			for index,centro in enumerate(centri_frontiera):
				linee = []
				punti=[]
				#primo quadrante
				for grado in xrange(0,90):
					#converto in radianti i gradi
					rad = (grado*math.pi)/180
					p_x = centro[0] + (r*math.cos(rad))
					p_y = centro[1] + (r*math.sin(rad))
					punti.append([p_x,p_y])
					#creo la linea che va dal centro al bordo trovato 
					#linea = LineString([(centro[0], centro[1]), (p_x, p_y)])
					#linee.append(linea)
				#secondo quadrante
				for grado in xrange(0,90):
					#converto in radianti i gradi
					rad = (grado*math.pi)/180
					p_x = centro[0] - (r*math.cos(rad))
					p_y = centro[1] + (r*math.sin(rad))
					punti.append([p_x,p_y])
				#terzo quadrante
				for grado in xrange(0,90):
					#converto in radianti i gradi
					rad = (grado*math.pi)/180
					p_x = centro[0] - (r*math.cos(rad))
					p_y = centro[1] - (r*math.sin(rad))
					punti.append([p_x,p_y])
				#quarto quadrante
		
				for grado in xrange(0,90):
					#converto in radianti i gradi
					rad = (grado*math.pi)/180
					p_x = centro[0] + (r*math.cos(rad))
					p_y = centro[1] - (r*math.sin(rad))
					punti.append([p_x,p_y])
			
				#ordino in senso orario i punti trovati sulla circonferenza
				global centroid
				centroid = (centro[0], centro[1])
				punti.sort(key=algo)
			
				#creo la linea che va dal centro al bordo trovato 
				for punto in punti:
					linea = LineString([(centro[0], centro[1]), (punto[0], punto[1])])
					linee.append(linea)	
			
				
				'''
				#elimino le linee che intersecano un segmento sicuramente visto
				linee_da_eliminare=[]
				for linea in linee:
					for segmento in walls:
						x11 = segmento.x1
						y11 = segmento.y1
						x12 = segmento.x2
						y12 = segmento.y2
						line_coords = linea.coords
						x21 = line_coords[0][0] 
						y21 = line_coords[0][1] 
						x22 = line_coords[1][0]
						y22 = line_coords[1][1]
						#elimino la linea se interseca un segmento
						if sg.segments_intersect(x11, y11, x12, y12, x21, y21, x22, y22):
							linee_da_eliminare.append(linea)
				'''
				#taglio le line se intersecano uno dei segmenti sicuramente visti
				linee_da_eliminare=[]
				linee_corrette=[]
				for linea in linee:
					incroci = []
					for i, segmento in enumerate(walls):
						x11 = segmento.x1
						y11 = segmento.y1
						x12 = segmento.x2
						y12 = segmento.y2
						line_coords = linea.coords
						x21 = line_coords[0][0] 
						y21 = line_coords[0][1] 
						x22 = line_coords[1][0]
						y22 = line_coords[1][1]
						linea2 = LineString([(x11, y11), (x12,y12)])
						if sg.segments_intersect(x11, y11, x12, y12, x21, y21, x22, y22):
							linee_da_eliminare.append(linea)
							punto_intersezione = linea.intersection(linea2)
							x_int = punto_intersezione.bounds[0]
							y_int = punto_intersezione.bounds[1]
							incroci.append(LineString([(centro[0], centro[1]), (x_int,y_int)]))
							#linee_corrette.append(LineString([(centro[0], centro[1]), (x_int,y_int)]))
					if len(incroci)>0:
						max = 0
						l= None
						for inc in incroci:
							if inc.length>max:
								max = inc.length
								l= inc
						linee_corrette.append(l)
							
							
				
				#elimino linee uguali
				for i,linea1 in enumerate(linee):
					for j, linea2 in enumerate(linee):
						if i!=j and linea1 == linea2:
							linee_da_eliminare.append(linea1)
							conta+=1		

				#elimino la linea se interseca un segmento dalla lista delle linee tanto ho inserito l'intesezione
				for linea in linee:
					trovata = False
					for elim in linee_da_eliminare:
						if linea == elim:
							trovata = True
					if trovata == False:
						linee_corrette.append(linea)
				
				del linee
				linee = copy.deepcopy(linee_corrette)
				 
				'''
				#elimino parte dei segmenti gia' all'interno del contorno
				for linea in linee:
					if contorno.intersection(linea).length > 0:
						linea = (linea - contorno.intersection(linea))
		
				#calcolo area come somma delle lunghezze
				area_cerchio = 0
				for linea in linee:
					area_cerchio += linea.length
			
				'''
				#calcolo area come somma della lunghezza delle linee
				area_cerchio = 0
				for linea in linee:
					if contorno.intersection(linea).length > 0:
						lung_linea = (linea - contorno.intersection(linea)).length
						area_cerchio += lung_linea
						bound = (contorno.intersection(linea)).bounds
					elif contorno.intersection(linea).length == 0:
						area_cerchio += linea.length

			
				#ci sono raggi che per un pezzo combaciano: TODO: questa cosa e' da verificare che sia giusta. probabilemnte e' sempre 400, verifica questa cosa, cosi' per velocizzare togli sto pezzo
				area_intersezione = 0
				for i,linea1 in enumerate(linee):
					for j, linea2 in enumerate(linee):
						if i!=j and linea1.intersection(linea2).length >0:
							area_intersezione+=linea1.intersection(linea2).length
				area_cerchio = area_cerchio-area_intersezione #tolgo all'area totale quella dei segmenti che si incrociano
			
					
			
				area_metrica_2.append(area_cerchio)
				print "l'area dell'intersezione:", area_intersezione
				print "l'area del cerchio: ",area_cerchio
				#dsg.disegna_segmenti_e_raggi_cerchio(walls, linee_corrette, format='png', filepath = path_obj.filepath, savename = '21_muri_e_raggi_frontiera'+str(index))	#da eliminare
				#dsg.disegna_segmenti_e_raggi_cerchio(walls, linee, format='png', filepath = path_obj.filepath, savename = '21_muri_e_raggi_frontiera'+str(index))	
				dsg.disegna_segmenti_raggi_cerchio_contorno(vertici,xmin,ymin,xmax,ymax, walls, linee, format='png', filepath =path_obj.filepath, savename = '21_muri_e_raggi_frontiera'+ str(index))
			'''
			#seleziono il centro ed il raggio e creo il cerchio 
			for index,c in enumerate(centri_frontiera):
		
				cerchio = Point(c[0], c[1]).buffer(parametri_obj.raggio_azione)
				dsg.disegna_contorno_e_area_vista(vertici,cerchio,xmin,ymin,xmax,ymax, format='png', filepath = path_obj.filepath, savename = '21_Contorno_ed_area_front_n_'+str(index))	
			
				#faccio differenza tra il cerchio creato e l'area del layout
				area = cerchio.difference(contorno).area
				area_metrica_2.append(area)
				print "l'area del cerchio senza l contorno: ",area
			'''
		
			#---METRICA 3: lunghezza della frontiera.
			#prendo coordinata massima e minima e tiro una retta.
			
			lunghezza_frontiere = []
			for index,fro in enumerate(pixel_coord_per_frontiera):
				list_x = []
				list_y = []
			
				punti = fro[:]
				for coord in fro:
					list_x.append(coord[0])
					list_y.append(coord[1])
			
				global centroid
				#bound = contorno.bounds # (minx, miny, maxx, maxy)
				#centroid = (bound[0]+((bound[2]-bound[0])/2),bound[1]+((bound[3]-bound[1])/2))#mi metto al centro dell'immagine
				centroid = (sum(list_x) / len(punti), sum(list_y) / len(punti))
				punti.sort(key=algo)

				#ora che possiedo i punti ordinati in senso orario, prendo quelli i due punti piu' lontani
				punto_lontano = []
				lunghezza_max = 0
				linea_corretta = None
				for i, p1 in enumerate(punti):
					for j,p2 in enumerate(punti):
						if j>i and j==i+1:
							line = LineString([(p1[0], p1[1]), (p2[0], p2[1])])
							if line.length > lunghezza_max:
								lunghezza_max = line.length
								punto_lontano.append(p1)
								punto_lontano.append(p2)
								linea_corretta = line
							
										

				print "la lunghezza della forntiera e':",linea_corretta.length
				dsg.disegna_contorno_e_retta_frontiera(vertici,linea_corretta,xmin,ymin,xmax,ymax, format='png', filepath = path_obj.filepath, savename = '21_Contorno_e_retta_frontiera_n_'+str(index))	
			
				lunghezza = linea_corretta.length
				lunghezza_frontiere.append(lunghezza)
		
			#delle metriche sulle frontiere sono i dati sono in:
			# sono tutte liste semplici ordinate per frontiera
			#mia metrica --> frontiera_scelta_mio_metodo (variabile singola)
			#mia mterica-->area_predetta_mio_metodo(lista)
			#metrica1--> area_frontiera_vera (lista)
			#metrica2-->area_metrica_2 (lista)
			#metrica3-->lunghezza_frontiere (lista)
			#ordinamento_frontiere --> lista con l'ordinamento delle frontiere a cui fanno riferimento le altre liste
		
			#crea un pickle per mappa con queste infomazioni
			print("creo pickle con info sulle forntiere")
			info_gain = (frontiera_scelta_mio_metodo,area_predetta_mio_metodo, area_frontiera_vera, area_metrica_2, lunghezza_frontiere, ordinamento_frontiere, frontiere_sul_bordo)
			pk.crea_pickle(info_gain, path_obj.filepath+'info_gain_frontiere_pickle.pkl')
			print("ho finito di creare il pickle dei dizionari")
		
							
	
	#in questa fase il grafo non e' ancora stato classificato con le label da dare ai vai nodi.
	#-------------------------------------------------------------------------------------	
	#creo il file xml dei parametri 
	par.to_XML(parametri_obj, path_obj)
	
	
	
	#-------------------------prova transitional kernels----------------------------------
	
	#splitto una stanza e restituisto la nuova lista delle stanze
	#stanze, colori = tk.split_stanza_verticale(2, stanze, colori,estremi) 
	#stanze, colori = tk.split_stanza_orizzontale(3, stanze, colori,estremi)
	#stanze, colori = tk.slit_all_cell_in_room(spazi, 1, colori, estremi) #questo metodo e' stato fatto usando il concetto di Spazio, dunque fai attenzione perche' non restituisce la cosa giusta.
	#stanze, colori = tk.split_stanza_reverce(2, len(stanze)-1, stanze, colori, estremi) #questo unisce 2 stanze precedentemente splittate, non faccio per ora nessun controllo sul fatto che queste 2 stanze abbiano almeno un muro in comune, se sono lontani succede un casino

	#-----------------------------------------------------------------------------------

	
	#-------------------------MAPPA SEMANTICA-------------------------------------------
	'''
	#in questa fase classifico i nodi del grafo e conseguentemente anche quelli della mappa.
	
	#gli input di questa fase non mi sono ancora molto chiari 
	#per ora non la faccio poi se mi serve la copio/rifaccio, penso proprio sia sbagliata.

	#stanze ground truth
	(stanze_gt, nomi_stanze_gt, RC, RCE, FCES, spaces, collegate_gt) = sema.get_stanze_gt(nome_gt, estremi)

	#corrispondenze tra gt e segmentate (backward e forward)
	(indici_corrispondenti_bwd, indici_gt_corrispondenti_fwd) = sema.get_corrispondenze(stanze,stanze_gt)

	#creo xml delle stanze segmentate
	id_stanze = sema.crea_xml(nomeXML,stanze,doorsVertices,collegate,indici_gt_corrispondenti_fwd,RCE,nomi_stanze_gt)

	#parso xml creato, va dalla cartella input alla cartella output/xmls, con feature aggiunte
	xml_output = sema.parsa(dataset_name, nomeXML)


	#classifico
	predizioniRCY = sema.classif(dataset_name,xml_output,'RC','Y',30)
	predizioniRCN = sema.classif(dataset_name,xml_output,'RC','N',30)
	predizioniFCESY = sema.classif(dataset_name,xml_output,'RCES','Y',30)
	predizioniFCESN = sema.classif(dataset_name,xml_output,'RCES','N',30)

	#creo mappa semantica segmentata e ground truth e le plotto assieme
	
	sema.creaMappaSemantica(predizioniRCY, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, RC, estremi, colori)
	plt.show()
	sema.creaMappaSemantica(predizioniRCN, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, RC, estremi, colori)
	plt.show()
	sema.creaMappaSemantica(predizioniFCESY, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, FCES, estremi, colori)
	plt.show()
	sema.creaMappaSemantica(predizioniFCESN, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, FCES, estremi, colori)
	plt.show()
	'''
	#-----------------------------------------------------------------------------------
	
	
	print "to be continued..."
	
	end_time_main = time.time()
	#scrivo su file i tempi
	SAVE_TIMEFILE = path_obj.filepath+'17_times.txt'
	
	time_results = []# elemenri confinanti, diaposizioni totali, diaposizioni legali, tempo di computazione (ogni elemento che rappresenta una stanza e' una tupla di 4 elementi)                     
	
	with open(SAVE_TIMEFILE,'w+') as TIMEFILE:
		print >>TIMEFILE,"il tempo necessario al main e'", end_time_main -start_time_main
		print >>TIMEFILE, "per trovare le frontiere ci vuole", end_time_frontiere- start_time_frontiere
		print >>TIMEFILE, "del tempo necessario al main, l'azione geometrica 1 occupa", end_time_azione_1 -start_time_azione_1
		print >>TIMEFILE, "del tempo necessario al main, l'azione complessa occupa:", end_time_azione_complessa-start_time_azione_complessa
		print >>TIMEFILE, "in particolare l'azione complessa per ogni stanza impiega"
	
		print len(lista_n_elementi), len(lista_n_disposizioni_totali), len(lista_n_disposizioni_reali), len(lista_tempi)
	
		indice_s = 0
		for e,dt,dr,t in zip(lista_n_elementi, lista_n_disposizioni_totali, lista_n_disposizioni_reali, lista_tempi):
			print >>TIMEFILE, "la stanza ", indice_s
			print >>TIMEFILE, "il numero di elementi dell'insieme delle celle confinanti e':", e
			print >>TIMEFILE, "il numero di disposizioni totali ottenuti sono: ", dt
			print >>TIMEFILE, "il numero di disposizioni legali sono: ", dr
			print >>TIMEFILE, "il tempo impiegato per processare questa stanza e': ", t
			print >>TIMEFILE, "---------------------------------"
			indice_s +=1
			tupla = (e, dt, dr, t)
			time_results.append(tupla)
	return results_accuracy, time_results
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

def main():
	start = time.time()
	print ''' PROBLEMI NOTI \n
	1] LE LINEE OBLIQUE NON VANNO;\n
	2] NON CLASSIFICA LE CELLE ESTERNE CHE STANNO DENTRO IL CONVEX HULL, CHE QUINDI VENGONO CONSIDERATE COME STANZE;\n
	OK 3] ACCURACY NON FUNZIONA;\n
	4] QUANDO VENGONO RAGGRUPPATI TRA DI LORO I CLUSTER COLLINEARI, QUESTO VIENE FATTO A CASCATA. QUESTO FINISCE PER ALLINEARE ASSIEME MURA MOLTO DISTANTI;\n
	5] IL SISTEMA E' MOLTO SENSIBILE ALLA SCALA. BISOGNEREBBE INGRANDIRE TUTTE LE IMMAGINI FACENDO UN RESCALING E RISOLVERE QUESTO PROBLEMA. \n
	[4-5] FANNO SI CHE I CORRIDOI PICCOLI VENGANO CONSIDERATI COME UNA RETTA UNICA\n
	6] BISOGNEREBBE FILTRARE LE SUPERFICI TROPPO PICCOLE CHE VENGONO CREATE TRA DEI CLUSTER;\n
	7] LE IMMAGINI DI STAGE SONO TROPPO PICCOLE; VANNO RIPRESE PIU GRANDI \n
	>> LANCIARE IN BATCH SU ALIENWARE\n
	>> RENDERE CODICE PARALLELO\n
	8] MANCANO 30 DATASET DA FARE CON STAGE\n
	9] OGNI TANTO NON FUNZIONA IL GET CONTORNO PERCHE SBORDA ALL'INTERNO\n
	>> PROVARE CON SCAN BORDO (SU IMMAGINE COPIA)\n
	>> PROVARE A SETTARE IL PARAMETRO O A MODIFICARE IL METODO DI SCAN BORDO\n
	>> CERCARE SOLUZIONI ALTERNATIVE (ES IDENTIFICARE LE CELLE ESTERNE)\n
	OK 10] VANNO TARATI MEGLIO I PARAMETRI PER IL CLUSTERING\n 
	>> I PARAMETRI DE CLUSTERING SONO OK; OGNI TANTO FA OVERSEGMENTAZIONE.\n
	>>> EVENTUALMENTE SE SI VEDE CHE OVERSEGMENTAZIONE SONO UN PROBLEMA CAMBIARE CLUSTERING O MERGE CELLE\n
	11] LE LINEE DELLA CANNY E HOUGH TALVOLTA SONO TROPPO GROSSE \n
	>> IN REALTA SEMBRA ESSERE OK; PROVARE CON MAPPE PIU GRANDI E VEDERE SE CAMBIA.
	12] BISOGNEREBBE AUMENTARE LA SEGMENTAZIONE CON UN VORONOI
	OK 13] STAMPA L'IMMAGINE DELLA MAPPA AD UNA SCALA DIVERSA RISPETTO A QUELLA VERA.\n
	OK 14] RISTAMPARE SCHOOL_GT IN GRANDE CHE PER ORA E' STAMPATO IN PICCOLO (800x600)\n
	OK  VEDI 10] 15] NOI NON CALCOLIAMO LA DIFFUSION DEL METODO DI MURA; PER ALCUNI VERSI E' UN BENE PER ALTRI NO\n
	OK VEDI 4] 16] NON FACCIAMO IL CLUSTERING DEI SEGMENTI IN MANIERA CORRETTA; DOVREMMO SOLO FARE MEANSHIFT\n
	17] LA FASE DEI SEGMENTI VA COMPLETAMENTE RIFATTA; MEANSHIFT NON FUNZIONA COSI';  I SEGMENTI HANNO UN SACCO DI "==" CHE VANNO TOLTI; SPATIAL CLUSTRING VA CAMBIATO;\n
	18] OGNI TANTO IL GRAFO TOPOLOGICO CONNETTE STANZE CHE SONO ADIACENTI MA NON CONNESSE. VA RIVISTA LA PARTE DI MEDIALAXIS;\n
	19] PROVARE A USARE L'IMMAGINE CON IL CONTORNO RICALCATO SOLO PER FARE GETCONTOUR E NON NEGLI ALTRI STEP.\n
	20] TOGLIERE THRESHOLD + CANNY -> USARE SOLO CANNY.\n
	21] TOGLIERE LE CELLE INTERNE CHE SONO BUCHI.\n
	>> USARE VORONOI PER CONTROLLARE LA CONNETTIVITA.\n
	>> USARE THRESHOLD SU SFONDO \n
	>> COMBINARE I DUE METODI\n
	22] RIMUOVERE LE STANZE ERRATE:\n
	>> STANZE "ESTERNE" INTERNE VANNO TOLTE IN BASE ALLE CELLE ESTERNE\n
	>> RIMUOVERE STANZE CON FORME STUPIDE (ES PARETI LUNGHE STRETTE), BISOGNA DECIDERE SE ELIMINARLE O INGLOBARLE IN UN ALTRA STANZA\n
	23] RISOLVERE TUTTI I WARNING.\n
	
	da chiedere: guardare il metodo clustering_dbscan_celle(...) in layout la riga 
	af = DBSCAN(eps, min_samples, metric="precomputed").fit(X) non dovrebbe essere cosi?
	af = DBSCAN(eps= eps, min_samples = min_samples, metric="precomputed").fit(X)
	'''

	print '''
	FUNZIONAMENTO:\n
	SELEZIONARE SU QUALI DATASETs FARE ESPERIMENTI (variabile DATASETs -riga165- da COMMENTARE / DECOMMENTARE)\n
	SPOSTARE LE CARTELLE CON I NOMI DEI DATASET CREATI DALL'ESPERIMENTO PRECEDENTE IN UNA SOTTO-CARTELLA (SE TROVA UNA CARTELLA CON LO STESSO NOME NON CARICA LA MAPPA)\n
	SETTARE I PARAMERI \n
	ESEGUIRE\n
	OGNI TANTO IL METODO CRASHA IN FASE DI VALUTAZIONE DI ACCURATEZZA. NEL CASO, RILANCIARLO\n
	SPOSTARE TUTTI I RISULTATI IN UNA CARTELLA IN RESULTS CON UN NOME SIGNIFICATIVO DEL TEST FATTO\n
	SALVARE IL MAIN DENTRO QUELLA CARTELLA\n
	'''



	#-------------------PARAMETRI-------------------------------------------------------
	#carico parametri di default
	parametri_obj = par.Parameter_obj()
	#carico path di default
	path_obj = par.Path_obj()
	#-----------------------------------------------------------------------------------	
	
	makeFolders(path_obj.OUTFOLDERS,path_obj.DATASETs)
	skip_performed = True
	
	#-----------------------------------------------------------------------------------
	#creo la cartella di log con il time stamp 
	our_time = str(dt.datetime.now())[:-10].replace(' ','@') #get current time
	SAVE_FOLDER = os.path.join('./log', our_time)
	if not os.path.exists(SAVE_FOLDER):
		os.mkdir(SAVE_FOLDER)
	SAVE_LOGFILE = SAVE_FOLDER+'/log.txt'
	#------------------------------------------------------------------------------------

	with open(SAVE_LOGFILE,'w+') as LOGFILE:
		print "AZIONE", par.AZIONE
		print >>LOGFILE, "AZIONE", par.AZIONE
		shutil.copy('./minibatch.py',SAVE_FOLDER+'/minibatch.py') #copio il file del main
		shutil.copy('./parameters.py',SAVE_FOLDER+'/parameters.py') #copio il file dei parametri
		
		if par.AZIONE == "batch":
			if par.LOADMAIN==False:
				print >>LOGFILE, "SONO IN MODALITA' START MAIN"
			else:
				print >>LOGFILE, "SONO IN MODALITA' LOAD MAIN"
			print >>LOGFILE, "-----------------------------------------------------------"
			for DATASET in path_obj.DATASETs :
				print >>LOGFILE, "PARSO IL DATASET", DATASET
				global_results = []
				global_times =[]
				print 'INIZIO DATASET ' , DATASET
				for metricMap in glob.glob(path_obj.INFOLDERS+'IMGs/'+DATASET+'/*.png') :
				
					print >>LOGFILE, "---parso la mappa: ", metricMap
					print 'INIZIO A PARSARE ', metricMap
					path_obj.metricMap =metricMap 
					map_name = metricMap.split('/')[-1][:-4]
					#print map_name
					SAVE_FOLDER = path_obj.OUTFOLDERS+DATASET+'/'+map_name
					SAVE_PICKLE = path_obj.OUTFOLDERS+DATASET+'_pickle/'+map_name.split('.')[0]
					if par.LOADMAIN==False:
						if not os.path.exists(SAVE_FOLDER):
							os.mkdir(SAVE_FOLDER)
							os.mkdir(SAVE_PICKLE)
						else:
							# evito di rifare test che ho gia fatto
							if skip_performed :
								print 'GIA FATTO; PASSO AL SUCCESSIVO'
								continue

					#print SAVE_FOLDER
					path_obj.filepath = SAVE_FOLDER+'/'
					path_obj.filepath_pickle_layout = SAVE_PICKLE+'/'+'Layout.pkl'
					path_obj.filepath_pickle_grafoTopologico = SAVE_PICKLE+'/'+'GrafoTopologico.pkl'

					
					add_name = '' if DATASET == 'SCHOOL' else ''
					
					if par.mappa_completa == False:
						nome = map_name.split('_updated')[0]
						path_obj.nome_gt = path_obj.INFOLDERS+'XMLs/'+DATASET+'/'+nome+'_updated.xml'
					else:
						path_obj.nome_gt = path_obj.INFOLDERS+'XMLs/'+DATASET+'/'+map_name+add_name+'.xml'				
					
					#--------------------new parametri-----------------------------------
					#setto i parametri differenti(ogni dataset ha parametri differenti)
					parametri_obj.minLateralSeparation = 7 if (DATASET=='SCHOOL' or DATASET=='PARZIALI' or DATASET=='SCHOOL_grandi') else 15	
					#parametri_obj.cv2thresh = 150 if DATASET == 'SCHOOL' else 200
					parametri_obj.cv2thresh = 150 if (DATASET=='SCHOOL' or DATASET=='PARZIALI' or DATASET == 'SCHOOL_grandi') else 200
					parametri_obj.flip_dataset = True if DATASET == 'SURVEY' else False
					#--------------------------------------------------------------------
					#-------------------ESECUZIONE---------------------------------------
					
					if par.LOADMAIN==False:
						print "start main"
						results, time_results = start_main(parametri_obj, path_obj)
						global_results.append(results);
						global_times.append(time_results);
			
						#calcolo accuracy finale dell'intero dataset, e times
						if metricMap == glob.glob(path_obj.INFOLDERS+'IMGs/'+DATASET+'/*.png')[-1]:
							
							#calcoli sul tempo
							print "singoli tempi per mappa"
							for tupla in global_times:
								print tupla
							
							
							'''
							#TODO: decommentare, questo serve per l'accuracy, per ora non mi serve
							accuracy_bc_medio = []
							accuracy_bc_in_pixels = []
							accuracy_fc_medio = []
							accuracy_fc_in_pixels=[]
		
		
							for i in global_results :
								accuracy_bc_medio.append(i[0])
								accuracy_fc_medio.append(i[2]) 
								accuracy_bc_in_pixels.append(i[4])
								accuracy_fc_in_pixels.append(i[5])
		
							filepath= path_obj.OUTFOLDERS+DATASET+'/'
							print filepath
							f = open(filepath+'accuracy.txt','a')
							#f.write(filepath)
							f.write('accuracy_bc = '+str(np.mean(accuracy_bc_medio))+'\n')
							f.write('accuracy_bc_pixels = '+str(np.mean(accuracy_bc_in_pixels))+'\n')
							f.write('accuracy_fc = '+str(np.mean(accuracy_fc_medio))+'\n')
							f.write('accuracy_fc_pixels = '+str(np.mean(accuracy_fc_in_pixels))+'\n\n')
							f.close()
							'''
						LOGFILE.flush()
					elif par.LOADMAIN==True:
						print "load main"
						print >>LOGFILE, "---parso la mappa: ", path_obj.metricMap
						load_main(path_obj.filepath_pickle_layout, path_obj.filepath_pickle_grafoTopologico, path_obj.filepath+"parametri.xml")
						LOGFILE.flush()
					
					
				else :
					continue
				break
			LOGFILE.flush()
		
		elif par.AZIONE =='mappa_singola':
			#-------------------ESECUZIONE singola mappa----------------------------------
			if par.LOADMAIN==False:
				print "start main"
				print >>LOGFILE, "SONO IN MODALITA' START MAIN"
				print >>LOGFILE, "---parso la mappa: ", path_obj.metricMap
				start_main(parametri_obj, path_obj)
				LOGFILE.flush()
			else:
				print "load main"
				print >>LOGFILE, "SONO IN MODALITA' LOAD MAIN"
				print >>LOGFILE, "---parso la mappa: ", path_obj.metricMap
				load_main(path_obj.filepath_pickle_layout, path_obj.filepath_pickle_grafoTopologico, path_obj.filepath+"parametri.xml")
				LOGFILE.flush()
			
	#-------------------TEMPO IMPIEGATO-------------------------------------------------
	fine = time.time()
	elapsed = fine-start
	print "la computazione ha impiegato %f secondi" % elapsed	
				
if __name__ == '__main__':
	main()