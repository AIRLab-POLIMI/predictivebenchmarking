import warnings 
warnings.warn('SISTEMARE I PROBLEMI A GET_CORRISPONDENZE')
import matplotlib.patches as patches
import sys
import matplotlib.colors as colors
import numpy as np
import math
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from descartes import PolygonPatch
import xml.etree.ElementTree as ET
from util import disegna as dsg

def flip_vertici(vertici, altezza):
	'''
	flippo le y dei vertici
	'''
	for v in vertici:
		v[1] = altezza - v[1]
	return vertici


def get_stanze_gt(nome_gt):
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

# 
# 	#lista dei nomi delle stanze gt che nell'xml corrispondono al campo label (classroom, stairs, lab, ecc).
# 	nomi_stanze_gt = []
# 	for space in spaces:
# 		nomi_stanze_gt.append(space.find('.//label').text)

	#coppie di stanze ground truth collegate tramite porta.
	collegate_gt = []
	for space in spaces:
		porte = space.findall('.//portal')
		for porta in porte:
			connessioni_porta = []
			for i in porta.findall('.//id'):
				connessioni_porta.append(ids_gt.index(str(i.text)))
			collegate_gt.append(connessioni_porta)


	
	#stanze_gt = update_gt(estremi, root, xs, ys)

	'''
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
	'''
	return stanze_gt, ids_gt#, spaces, collegate_gt
	
	
#TODO: questo metodo e' una cagata, cambiarlo con uno efficiente.
def adatta_scala_stanze_gt(stanze_gt, stanze, epsilon = 0.05):
	'''
	permette di adattare la scala delle stanze_gt con quella delle stanze reali. 
	tenta di trovare una stanza gt con parte vertivale ed orizzontale simile ad una reale e adatta il resto in base a quella
	'''
	stanze_simili=[]
	stanze_gt_simili=[]
	for stanza in stanze:
		row = [] #per ogni stanza creo una lista di stanze simili al quella presa dalle stanze gt
		#c=0
		for gt in stanze_gt:
			#se la stanza e' intera e la proporzione di rettangolarita' tra verticale e orizzontale piu' o meno e' la stessa seleziono quella stanza
			bound1 = stanza.bounds #(minx, miny, maxx, maxy)
			bound2 = gt.bounds
			x_dif1 = (bound1[2]-bound1[0])
			y_dif1 = (bound1[3]-bound1[1])
			proporzione1 = x_dif1/y_dif1
			x_dif_gt = (bound2[2]-bound2[0])
			y_dif_gt = (bound2[3]-bound2[1])
			proporzione2 = x_dif_gt/y_dif_gt
			if (proporzione1-proporzione2<=epsilon and proporzione1-proporzione2>=0) or (proporzione2-proporzione1<=epsilon and proporzione2-proporzione1>=0): 
			#if (stanza.area-gt.area<=epsilon and stanza.area-gt.area>=0) or (gt.area-stanza.area<=epsilon and gt.area-stanza.area>=0):
				#c+=1
				#s = stanza
				#sgt = gt
				row.append(gt)
		#if c==1:
		if len(row)>0:#esistono delle stanze simili a quella che sto considerando
			#ho trovato due stanze con area molto simile
			stanze_simili.append(stanza)#ci metto la stanza della mia mappa che sto considerando 
			stanze_gt_simili.append(row)# ci metto la lista di quelle stanze che potrebbero essere le candidate
	
	if len(stanze_gt_simili)>0:
	
		#prendo la prima stanza in stanze simili e la prima stanza in stanze_gt_simili corrispondente e faccio tutto in base a quella misura
		# bound = stanze_simili[0].bounds #(minx, miny, maxx, maxy)
# 		bound_gt = stanze_gt_simili[0][0].bounds #(minx, miny, maxx, maxy)
# 		estremi_stanza = [bound[0],bound[2], bound[1], bound[3]]
# 		estremi_stanza_gt = [bound_gt[0],bound_gt[2], bound_gt[1], bound_gt[3]]
# 		
# 		stanze_gt_new = update_gt(estremi_stanza,estremi_stanza_gt, stanze_gt) #aggiorno le stanze 
# 		stanze_gt=stanze_gt_new[:]#copio la nuova struttura dati
		
		
		#creo una lista di stanze gt proporzionate
		lista_gt_proporzionata = []
		for indice, ssgt_list in enumerate(stanze_gt_simili):
			for ssgt in ssgt_list:
				bound = stanze_simili[indice].bounds #(minx, miny, maxx, maxy)
				bound_gt = ssgt.bounds #(minx, miny, maxx, maxy)
				estremi_stanza = [bound[0],bound[2], bound[1], bound[3]]
				estremi_stanza_gt = [bound_gt[0],bound_gt[2], bound_gt[1], bound_gt[3]]
				temporanea_gt = stanze_gt[:]
				stanze_gt_new = update_gt(estremi_stanza,estremi_stanza_gt, temporanea_gt) #aggiorno le stanze 
				#stanze_gt = stanze_gt_new[:]#copio la nuova struttura dati
				lista_gt_proporzionata.append(stanze_gt_new)

	print "le stanze trovate con similarit' sono :", len(stanze_simili)
	for sgts in stanze_gt_simili:
		print "la lunghezza in questo caso e':" ,len(sgts)
		
	return stanze_simili, stanze_gt_simili, lista_gt_proporzionata #, stanze_gt


def adatta_scala_stanze_gt_v2(stanze_gt, stanze_complete):
	'''
	crea tutte le possibili combinazioni per adattare la mappa gt a quella parziale.
	'''
	lista_gt_proporzionata = []
	for stanza in stanze_complete:
		for stanza_gt in stanze_gt:
			bound = stanza.bounds #(minx, miny, maxx, maxy)
			bound_gt = stanza_gt.bounds #(minx, miny, maxx, maxy)
			estremi_stanza = [bound[0],bound[2], bound[1], bound[3]]
			estremi_stanza_gt = [bound_gt[0],bound_gt[2], bound_gt[1], bound_gt[3]]
			temporanea_gt = stanze_gt[:]
			stanze_gt_new = update_gt(estremi_stanza,estremi_stanza_gt, temporanea_gt) #aggiorno le stanze 
			#stanze_gt = stanze_gt_new[:]#copio la nuova struttura dati
			lista_gt_proporzionata.append(stanze_gt_new)
	
	return lista_gt_proporzionata


def update_gt(estremi_stanza, estremi_stanza_gt, spaces):
	'''
	spaces = stanze_gt
	'''

	xmin = estremi_stanza[0]
	xmax = estremi_stanza[1]
	ymin = estremi_stanza[2]
	ymax = estremi_stanza[3]
	xmin_gt = estremi_stanza_gt[0]
	xmax_gt = estremi_stanza_gt[1]
	ymin_gt = estremi_stanza_gt[2]
	ymax_gt = estremi_stanza_gt[3]
	# xmin_gt = min(xs)
# 	xmax_gt = max(xs)
# 	ymin_gt = min(ys)
# 	ymax_gt = max(ys)

	fattore_x = (xmax-xmin)/(xmax_gt-xmin_gt)
	fattore_y = (ymax-ymin)/(ymax_gt-ymin_gt)
	xmin_gt_scalato = xmin_gt*fattore_x
	ymin_gt_scalato = ymin_gt*fattore_y
	stanze_gt = []
	#spaces = root.findall('.//space')
	for space in spaces:
		#pol = space.find('.//bounding_polygon')
		punti = list(space.exterior.coords)
		new_points = []
		for p in punti:
			x = p[0]
			y = p[1]
			x_scalato = x*fattore_x
			y_scalato = y*fattore_y
			x_traslato = x_scalato+(xmin-xmin_gt_scalato)
			y_traslato = y_scalato+(ymin-ymin_gt_scalato)
			new_points.append((x_traslato,y_traslato))
			#punti.append((int(p.get('x')),ymax_gt+ymin_gt-int(p.get('y'))))
		stanze_gt.append(Polygon(new_points))
	return stanze_gt
	
	
def elimina_configurazioni_errate(stanze, lista_gt_proporzionata):
	'''
	elimina delle configurazioni all'interno di lista_gt_proporzionata che sono sicuramente errate.
	Ad esempio se esiste una stanza reale non coperta da una gt allora quella la elimino
	'''	
	
	da_eliminare = []
	
	for configurazione in lista_gt_proporzionata:
		for stanza in stanze:
			trovato = False
			for s in configurazione:
				if s.intersects(stanza):
					trovato = True
		
			if trovato== False:
				da_eliminare.append(configurazione)
				break
				
	new_list = lista_gt_proporzionata[:]
	for elem in da_eliminare:
		for configurazione in lista_gt_proporzionata:
			if elem == configurazione:
				new_list.remove(elem)

	return new_list


def calcola_percentuali_completamento_mappa(spazi, lista_gt_proporzionata):
	'''
	calcolo la percentuale di completamento della mappa nella configurazione in lista_gt_proporzionata
	'''
	#liste delle percentuali per ogni configurazione
	lista_percentuali_completamento_mappa_bwd = [] #percentuale di mappa reale che combacia se sovrappongo la mappa GT con quella reale (in modalita' bwd)
	lista_percentuali_completamento_GT_bwd = [] #percentuale esplorata dell'ambiente in modalita' bwd 
	lista_percentuali_completamento_mappa_fwd = [] #percentuale di mappa reale che combacia se sovrappongo la mappa reale a quella GT (modalita' fwd) 
	lista_percentuali_completamento_GT_fwd = [] #percentuale esplorata dell'ambiente in modalita' fwd 
	
	#liste precision e recall
	lista_precisions = []
	lista_recalls = []
	
	#calcolo l'area totale del mio layout
	area_layout = 0
	for s in spazi:
		area_layout = area_layout + s.spazio.area
	
	#calcolo backward
	lista_indici_corrispondenti_bwd = []
	
	for indice, stanze_gt in enumerate(lista_gt_proporzionata):
		#calcolo l'area della configurazione GT
		area_GT = 0
		for s in stanze_gt:
			area_GT = area_GT + s.area
			
		somma_area_intersezione = 0	
		recall_area = 0
		recalls_area = []
		recalls = []
		indici_corrispondenti_bwd = [] #in questa lista ci sono gli indici della stanza reale ottenuta(dalla lista delle stanze), in corrispondenza dell'indice della stanza gt della configurazione che sto considerando
		accuracy_bwd =[]
		dizionario={} 
		for index1, s in enumerate(stanze_gt):
			indice_stanza_corrispondente = -1
			max_overlap_recall = 0
			for index,s2 in enumerate(spazi):
				if (s2.spazio.intersects(s)):
					if(s2.spazio.intersection(s).area >= max_overlap_recall):
						max_overlap_recall = s2.spazio.intersection(s).area
						indice_stanza_corrispondente = index
						s_temp = s2.spazio
			#SISTEMAER QUI print "PLEASE FIXARE GET CORRISPONDENZE; MESSO QUICK FIX IO - MATTEO"
			if indice_stanza_corrispondente >-1 :
				#significa che ho trovato una stanza corrispondente
				somma_area_intersezione += max_overlap_recall
				
				
				#....
				recall_stanza = max_overlap_recall/s.area
				recall_area += s.area
				recalls_area.append(max_overlap_recall)
				if  s2.parziale==True:
					recalls.append(recall_stanza)
				else:
					recalls.append(-1)
				indici_corrispondenti_bwd.append(indice_stanza_corrispondente)
			else : pass#print "WARNING QUI NON VA NULLA 1"
		
		lista_indici_corrispondenti_bwd.append(indici_corrispondenti_bwd) #per ogni configurazione ho la lista degli indici corrispondenti bwc			
		percentuale_reale_bwd = (float(somma_area_intersezione)/float(area_layout))*100
		percentuale_GT_bwd = (float(somma_area_intersezione)/float(area_GT))*100
		lista_percentuali_completamento_mappa_bwd.append(percentuale_reale_bwd)
		lista_percentuali_completamento_GT_bwd.append(percentuale_GT_bwd)
		lista_recalls.append(recalls)	
	
	#calcolo forward	
	lista_indici_corrispondenti_fwd = []
	for indice, stanze_gt in enumerate(lista_gt_proporzionata):
		#calcolo l'area della configurazione GT
		area_GT = 0
		for s in stanze_gt:
			area_GT = area_GT + s.area
		
		somma_area_intersezione = 0
		precisions = []
		precision_area = 0
		precisions_area = []
		indici_gt_corrispondenti_fwd = []
		for index1,s in enumerate(spazi):
			#SISTEMAER QUI print "ANCHE QUI CAMBIARE" #indice_stanza_gt_corrispondente=-1 l'ho messo io ma va gestito
			indice_stanza_gt_corrispondente = -1
			max_overlap_precision = 0
			for index,s2 in enumerate(stanze_gt):
				if (s2.intersects(s.spazio)):
					if(s2.intersection(s.spazio).area >= max_overlap_precision):
						max_overlap_precision = s2.intersection(s.spazio).area
						indice_stanza_gt_corrispondente = index
						s_temp = s2
			#SISTEMAER QUI print "PLEASE FIXARE GET CORRISPONDENZE; MESSO QUICK FIX IO - MATTEO"
			if indice_stanza_gt_corrispondente >-1 :			
				somma_area_intersezione += max_overlap_precision
			
				#...
				precision_stanza = max_overlap_precision/s.spazio.area
				if s.parziale ==True:
					precisions.append(precision_stanza)
				else:
					precisions.append(-1)
				precision_area += s.spazio.area
				precisions_area.append(max_overlap_precision)
				indici_gt_corrispondenti_fwd.append(indice_stanza_gt_corrispondente)
			else : print "WARNING QUI NON VA NULLA 2"
		lista_indici_corrispondenti_fwd.append(indici_gt_corrispondenti_fwd) #per ogni configurazione ho la lista degli indici corrispondenti bwc	
		percentuale_GT_fwd = (float(somma_area_intersezione)/float(area_GT))*100
		percentuale_reale_fwd = (float(somma_area_intersezione)/float(area_layout))*100
		lista_percentuali_completamento_GT_fwd.append(percentuale_GT_fwd)
		lista_percentuali_completamento_mappa_fwd.append(percentuale_reale_fwd)
		lista_precisions.append(precisions)
			
	return lista_percentuali_completamento_mappa_bwd, lista_percentuali_completamento_mappa_fwd, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd, lista_indici_corrispondenti_fwd, lista_indici_corrispondenti_bwd, lista_precisions, lista_recalls


def calcolo_informazioni(spazi, lista_gt_proporzionata, lista_indici_corrispondenti_fwd, ids_gt, id_stanze, lista_percentuali_completamento_GT_bwd, lista_percentuali_completamento_GT_fwd, lista_percentuali_completamento_mappa_bwd, lista_percentuali_completamento_mappa_fwd, lista_precisions, lista_recalls, contorno):
	'''
	calcolo tutte le informazioni utili e le inserisco in un dizionario. restituisco la lista dei dizionari per ogni configurazione.
	'''
	#calcolo le percentuali esplorate della mappa Gt come intersezione con il contorno
	lista_percentuali_GT_intersezione_contorno = []
	for conf in lista_gt_proporzionata:
		area_conf = 0
		area_totale = 0
		for st_gt in conf:
			area_totale = area_totale + st_gt.area
			area_conf = area_conf +(st_gt.intersection(contorno)).area
		lista_percentuali_GT_intersezione_contorno.append(area_conf/area_totale)
	
	

	#lista dizionari. per ogni configurazione salvo un dizionario che ha un elemento per ogni stanza parziale
	lista_dizionari_configurazione=[]
	for indice, corrispondenti_fwd in enumerate(lista_indici_corrispondenti_fwd):
		#la lista corrispondenti_fwd e' ordinata come le stanze, nell'i-esimo elemento contiene l'indirizzo della stanza GT in stanze_gt
		dizionario={} 
		for indice_st, indice_gt in enumerate(corrispondenti_fwd):
			if spazi[indice_st].parziale ==True:
				id_della_stanza_XML_GT = ids_gt[indice_gt]
				id_della_stanza_XML_predizione = id_stanze[indice_st]
				area_predetta = spazi[indice_st].area_predetta
				area_vera = lista_gt_proporzionata[indice][indice_gt].area
				area_vera_esplorata = spazi[indice_st].area_originale
				percentuale_area_vera_esplorata = (area_vera_esplorata/area_vera)*100		
				percentuale_area_totale_ambiente_esplorata_bwd = lista_percentuali_completamento_GT_bwd[indice]
				percentuale_area_totale_ambiente_esplorata_fwd = lista_percentuali_completamento_GT_fwd[indice]		
				percentuale_matching_mappa_bwd = lista_percentuali_completamento_mappa_bwd[indice]
				percentuale_matching_mappa_fwd = lista_percentuali_completamento_mappa_fwd[indice]
				area_intersezione_tra_stanza_originale_e_stanza_predetta = (lista_gt_proporzionata[indice][indice_gt].intersection(spazi[indice_st].spazio)).area
				#Intersecton over union
				area_unione_tra_stanza_originale_e_stanza_predetta = (lista_gt_proporzionata[indice][indice_gt].union(spazi[indice_st].spazio)).area			
				IoU = area_intersezione_tra_stanza_originale_e_stanza_predetta/area_unione_tra_stanza_originale_e_stanza_predetta
				
				#faccio intersection over union filtrando alle stanze considerare(parziale e GT) il contorno
				st_parziale_filtrata = (spazi[indice_st].spazio).difference(contorno)
				st_Gt_filtrata = lista_gt_proporzionata[indice][indice_gt].difference(contorno)
				IoU_filtrato = (st_parziale_filtrata.intersection(st_Gt_filtrata)).area/(st_parziale_filtrata.union(st_Gt_filtrata)).area
				tocco_bordo = spazi[indice_st].tocco_bordo
				
				#Questa e' solo una prova
				#faccio intersection over union filtrando alle stanze parziali considerare tutte le stanze GT che non la riguardano.
				stanza_par_considerata = spazi[indice_st].spazio
				stanza_gt_considerata = lista_gt_proporzionata[indice][indice_gt]
				stanza_parziale_temp = stanza_par_considerata
				for st_gt in lista_gt_proporzionata[indice]:
					if stanza_gt_considerata != st_gt: #tolgo alla stanza parziale tutte quelle area date dalle altre stanza GT che non corrispondono alla stanza parziale considerata posso anche scrivere if i != indice_gt
						area1= stanza_parziale_temp.area
						stanza_parziale_temp = stanza_parziale_temp.difference(st_gt)#tolgo le atre stanze
						area2 = stanza_parziale_temp.area
						if area1 != area2:
							print "####################ho fatto qualcosa###############", area1, area2
				#ora calcola la nuova intersection over union
				
				IoU_filtrata_2 = stanza_gt_considerata.intersection(stanza_parziale_temp).area/stanza_gt_considerata.union(stanza_parziale_temp).area
						
						
				#nuove metriche per percentuali
				#area della stanza Gt realmente esplorata
				area_stanza_GT_esplorata = lista_gt_proporzionata[indice][indice_gt].intersection(contorno).area / lista_gt_proporzionata[indice][indice_gt].area #area realemte esplorata della stanza GT(interezione tra la stanza GT ed il contorno)
				area_mappa_GT_intersezione_contorno = lista_percentuali_GT_intersezione_contorno[indice] #rappresenta la vera percentuale di area esplorata della GT (questo perche' ho fatto l'intersezione con il contorno)
				
				#creo dizionario
				dizionario[id_della_stanza_XML_GT] = [id_della_stanza_XML_predizione, area_predetta, area_vera, area_vera_esplorata, percentuale_area_vera_esplorata, percentuale_area_totale_ambiente_esplorata_bwd, percentuale_area_totale_ambiente_esplorata_fwd, percentuale_matching_mappa_bwd, percentuale_matching_mappa_fwd, area_intersezione_tra_stanza_originale_e_stanza_predetta, area_unione_tra_stanza_originale_e_stanza_predetta,IoU, area_stanza_GT_esplorata, area_mappa_GT_intersezione_contorno, IoU_filtrato, tocco_bordo, IoU_filtrata_2]
	
			else : pass#print "WARNING QUI NON VA NULLA 1"
		lista_dizionari_configurazione.append(dizionario)
	
				
	'''			
	
	for indice, stanze_gt in enumerate(lista_gt_proporzionata):
			
		somma_area_intersezione = 0		
		dizionario={} 
		for index1, s in enumerate(stanze_gt):
			indice_stanza_corrispondente = -1
			max_overlap_recall = 0
			s2 = None
			for index,s2 in enumerate(spazi):
				if (s2.spazio.intersects(s)):
					if(s2.spazio.intersection(s).area >= max_overlap_recall):
						max_overlap_recall = s2.spazio.intersection(s).area
						indice_stanza_corrispondente = index
						s_temp = s2
			#SISTEMAER QUI print "PLEASE FIXARE GET CORRISPONDENZE; MESSO QUICK FIX IO - MATTEO"
			if indice_stanza_corrispondente >-1 :
				#significa che ho trovato una stanza corrispondente
				somma_area_intersezione += max_overlap_recall
				
				#se la stanza e' parziale aggiungo l'elemento nel dizionario
				if s_temp.parziale == True:
				
					id_della_stanza_XML_GT = ids_gt[index1]
					id_della_stanza_XML_predizione = id_stanze[index]
					area_predetta = s_temp.area_predetta
					area_vera = s.area
					area_vera_esplorata = s_temp.area_originale
					percentuale_area_vera_esplorata = (area_vera_esplorata/area_vera)*100
					percentuale_area_totale_ambiente_esplorata_bwd = lista_percentuali_completamento_GT_bwd[indice]
					percentuale_area_totale_ambiente_esplorata_fwd = lista_percentuali_completamento_GT_fwd[indice]		
					percentuale_matching_mappa_bwd = lista_percentuali_completamento_mappa_bwd[indice]
					percentuale_matching_mappa_fwd = lista_percentuali_completamento_mappa_fwd[indice]
				
					#creo dizionario
					dizionario[id_della_stanza_XML_GT] = [id_della_stanza_XML_predizione, area_predetta, area_vera, area_vera_esplorata, percentuale_area_vera_esplorata, percentuale_area_totale_ambiente_esplorata_bwd, percentuale_area_totale_ambiente_esplorata_fwd, percentuale_matching_mappa_bwd, percentuale_matching_mappa_fwd]
				
			else : print "WARNING QUI NON VA NULLA 1"
		
		lista_dizionari_configurazione.append(dizionario)
	'''
	return lista_dizionari_configurazione


	
#TODO: questo metodo mi serve solo come esempio	
def get_corrispondenze(stanze, stanze_gt, file_name,filepath = '.', plotta = False):
	'''
	Riceve stanze segmentate, gt, nome della mappa e scrive sul file accuracy.txt accuracy bc ed accuracy fc medie (+- var). 
	''' 
	#calcolo recall, salvando gli indici delle stanze segmentate corrispondenti alle gt.
	somma_recall = 0
	recall_area = 0
	recalls_area = []
	recalls = []
	indici_corrispondenti_bwd = []
	for index1, s in enumerate(stanze_gt):
		indice_stanza_corrispondente = -1
		max_overlap_recall = 0
		for index,s2 in enumerate(stanze):
			if (s2.intersects(s)):
				if(s2.intersection(s).area >= max_overlap_recall):
					max_overlap_recall = s2.intersection(s).area
					indice_stanza_corrispondente = index
					s_temp = s2
		#SISTEMAER QUI print "PLEASE FIXARE GET CORRISPONDENZE; MESSO QUICK FIX IO - MATTEO"
		if indice_stanza_corrispondente >-1 :
			recall_stanza = max_overlap_recall/s.area
			recall_area += s.area
			recalls_area.append(max_overlap_recall)
			recalls.append(recall_stanza)
			#-----prova----
			#print recall_stanza, max_overlap_recall, s.area
			if plotta:
				plt.clf()
				plt.cla()
				plt.close()
				fig, (ax,ax2,ax3) = plt.subplots(3,sharex=True,sharey=True)
				plt.axis('equal')
			
				ax.axis('off')
				ax.set_xticks([])
				ax.set_yticks([])
				ax2.axis('off')
				ax2.set_xticks([])
				ax2.set_yticks([])
				ax3.axis('off')
				ax3.set_xticks([])
				ax3.set_yticks([])
			

			
				for poly in stanze:
					x,y = poly.exterior.xy
					ax.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )	
					ax2.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
					ax3.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
				for poly in stanze_gt:
					x,y = poly.exterior.xy
					ax.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )	
					ax2.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
					ax3.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
			
				f_patch = PolygonPatch(s,fc='YELLOW',ec='BLACK') 
				ax.add_patch(f_patch)
				f_patch = PolygonPatch(s,fc='YELLOW',ec='BLACK') 
				ax2.add_patch(f_patch)
			
				#ax2.add_patch(f_patch)
				#ax.set_xlim(xmin,xmax)
				#ax.set_ylim(ymin,ymax)
			
				f_patch = PolygonPatch(s_temp,fc='GREEN',ec='BLACK') 
				ax.add_patch(f_patch)
				f_patch = PolygonPatch(s_temp,fc='GREEN',ec='BLACK') 
				ax3.add_patch(f_patch)
				#ax3.add_patch(f_patch)
				#ax.set_xlim(xmin,xmax)
				#ax.set_ylim(ymin,ymax)
				print index1,index
				plt.show()
					
			#---fine prova
			indici_corrispondenti_bwd.append(indice_stanza_corrispondente)
		else : pass#print "WARNING QUI NON VA NULLA 1"
	
	accuracy_bc_medio = np.mean(recalls)
	accuracy_bc_var = np.std(recalls)
	accuracy_bc_in_pixels = sum(recalls_area)/float(recall_area)
	#print "accuracy bc"
	#print accuracy_bc_medio, accuracy_bc_var, accuracy_bc_in_pixels
	
	#print recall
	

	#calcolo precision, salvando gli indici delle stanze ground truth corrispondenti a quelle segmentate
	indici_gt_corrispondenti_fwd = [] 
	somma_precision = 0
	precisions = []
	precision_area = 0
	precisions_area = []
	for index1,s in enumerate(stanze):
		#SISTEMAER QUI print "ANCHE QUI CAMBIARE" #indice_stanza_gt_corrispondente=-1 l'ho messo io ma va gestito
		indice_stanza_gt_corrispondente = -1
		max_overlap_precision = 0
		for index,s2 in enumerate(stanze_gt):
			if (s2.intersects(s)):
				if(s2.intersection(s).area >= max_overlap_precision):
					max_overlap_precision = s2.intersection(s).area
					indice_stanza_gt_corrispondente = index
					s_temp = s2
		#SISTEMAER QUI print "PLEASE FIXARE GET CORRISPONDENZE; MESSO QUICK FIX IO - MATTEO"
		if indice_stanza_gt_corrispondente >-1 :			
			precision_stanza = max_overlap_precision/s.area	
			precisions.append(precision_stanza)
			
			precision_area += s.area
			precisions_area.append(max_overlap_precision)

			#-----prova----
			#print precision_stanza, max_overlap_precision, s.area
			if plotta:
				plt.clf()
				plt.cla()
				plt.close()
				fig, (ax,ax2,ax3) = plt.subplots(3,sharex=True,sharey=True)
				plt.axis('equal')
			
				ax.axis('off')
				ax.set_xticks([])
				ax.set_yticks([])
				ax2.axis('off')
				ax2.set_xticks([])
				ax2.set_yticks([])
				ax3.axis('off')
				ax3.set_xticks([])
				ax3.set_yticks([])
			

			
				for poly in stanze:
					x,y = poly.exterior.xy
					ax.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )	
					ax2.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
					ax3.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
				for poly in stanze_gt:
					x,y = poly.exterior.xy
					ax.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )	
					ax2.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
					ax3.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
			
				f_patch = PolygonPatch(s,fc='YELLOW',ec='BLACK') 
				ax.add_patch(f_patch)
				f_patch = PolygonPatch(s,fc='YELLOW',ec='BLACK') 
				ax2.add_patch(f_patch)
			
				#ax2.add_patch(f_patch)
				#ax.set_xlim(xmin,xmax)
				#ax.set_ylim(ymin,ymax)
			
				f_patch = PolygonPatch(s_temp,fc='GREEN',ec='BLACK') 
				ax.add_patch(f_patch)
				f_patch = PolygonPatch(s_temp,fc='GREEN',ec='BLACK') 
				ax3.add_patch(f_patch)
				#ax3.add_patch(f_patch)
				#ax.set_xlim(xmin,xmax)
				#ax.set_ylim(ymin,ymax)
				print index1,index
				plt.show()
					
			#---fine prova
			indici_gt_corrispondenti_fwd.append(indice_stanza_gt_corrispondente)
		else : print "WARNING QUI NON VA NULLA 2"
		
	accuracy_fc_medio = np.mean(precisions)
	accuracy_fc_var = np.var(precisions)
	accuracy_fc_in_pixels=0
	accuracy_fc_in_pixels = sum(precisions_area)/float(precision_area)
	#print precision
	print('accuracy_bc = '+str(accuracy_bc_medio)+' +- '+str(accuracy_bc_var))
	print('accuracy_fc = '+str(accuracy_fc_medio)+' +- '+str(accuracy_fc_var))

	f = open(filepath+'accuracy.txt','a')
	f.write(filepath+'/'+file_name+'\n')
	f.write('accuracy_bc = '+str(accuracy_bc_medio)+' +- '+str(accuracy_bc_var)+'\n')
	f.write('accuracy_bc_pixels = '+str(accuracy_bc_in_pixels)+'\n')
	f.write('accuracy_fc = '+str(accuracy_fc_medio)+' +- '+str(accuracy_fc_var)+'\n')
	f.write('accuracy_fc_pixels = '+str(accuracy_fc_in_pixels)+'\n\n')

	
	f.close()

	#mettilo nel main
	#dsg.disegna_grafici_per_accuracy(stanze, stanze_gt, filepath = filepath)
	
	return indici_corrispondenti_bwd, indici_gt_corrispondenti_fwd, [accuracy_bc_medio, accuracy_bc_var,accuracy_fc_medio,accuracy_fc_var, accuracy_bc_in_pixels, accuracy_fc_in_pixels]

	