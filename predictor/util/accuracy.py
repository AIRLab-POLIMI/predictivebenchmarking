# -*- coding: utf-8 -*-
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


def calcola_accuracy(nome_gt,estremi,stanze, file_name,filepath ='.', flip_dataset = True):
	#stanze ground truth
	print "ottengo stanze GT"
	(stanze_gt) = get_stanze_gt(nome_gt, estremi, flip_dataset)
	#corrispondenze tra gt e segmentate (backward e forward)
	print "calcolo metriche"
	(indici_corrispondenti_bwd, indici_gt_corrispondenti_fwd,results) = get_corrispondenze(stanze,stanze_gt,file_name, filepath=filepath)

	return results, stanze_gt

def elimina_stanze(stanze,estremi):
	'''
	vengono mostrate le stanze segmentate con all'interno la loro posizione nella lista stanze. Da terminale viene chiesto se si vuole eliminare una stanza. Se la risposta è sì (s) viene chiesto il numero della stanza da eliminare. Dopo averla eliminata, viene rimostrato il layout e viene chiesto iterativamente se si vuole eliminare un'altra stanza.
	'''	
	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	for index,s in enumerate(stanze):
		f_patch = PolygonPatch(s,fc='WHITE',ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin-20,xmax+20)
		ax.set_ylim(ymin-20,ymax+20)
		ax.text(s.representative_point().x,s.representative_point().y,str(index),fontsize=8)
	plt.show()

	risposta = raw_input('vuoi eliminare stanze? s/n: ')

	while str(risposta) == 's':
		try:
		    da_eliminare=int(raw_input('numero stanza da eliminare:'))
		except ValueError:
		    print "Not a number"
		del stanze[int(da_eliminare)]
		print len(stanze)
		fig = plt.figure()
		ax = fig.add_subplot(111)
		for index,s in enumerate(stanze):
			f_patch = PolygonPatch(s,fc='WHITE',ec='BLACK')
			ax.add_patch(f_patch)
			ax.set_xlim(xmin-20,xmax+20)
			ax.set_ylim(ymin-20,ymax+20)
			ax.text(s.representative_point().x,s.representative_point().y,str(index),fontsize=8)
		plt.show()
		risposta = raw_input('vuoi eliminare stanze? s/n: ')
	
	return stanze


def get_stanze_gt(nome_gt, estremi,flip_dataset = True):
	'''
	Prende in input il nome dell'xml ground, gli estremi delle segmentate,
	e restituisce la lista di stanze ground truth (scalate e traslate in modo da rendere il layout gt sovrapponibile a quello segmentato) 
	'''

	tree = ET.parse(nome_gt)
	root = tree.getroot()

	xs = []
	ys = []
	for punto in root.findall('*//point'):
		xs.append(int(punto.get('x')))
		ys.append(int(punto.get('y')))	
	
	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]
	xmin_gt = min(xs)
	xmax_gt = max(xs)
	ymin_gt = min(ys)
	ymax_gt = max(ys)
	altezza = ymax + ymin

	stanze_gt = []
	#rendo layout mio e layout gt della stessa dimensione
	fattore_x = (xmax-xmin)/(xmax_gt-xmin_gt)
	fattore_y = (ymax-ymin)/(ymax_gt-ymin_gt)
	xmin_gt_scalato = xmin_gt*fattore_x
	ymin_gt_scalato = ymin_gt*fattore_y
	stanze_gt = []
	spaces = root.findall('.//space')
	for space in spaces:
		pol = space.find('.//bounding_polygon')
		punti = []
		bordi = pol.findall('./point')
		for p in bordi[:-1]:
			x = int(p.get('x'))
			y = int(p.get('y'))
			x_scalato = x*fattore_x
			y_scalato = y*fattore_y
			x_traslato = x_scalato+(xmin-xmin_gt_scalato)
			y_traslato = y_scalato+(ymin-ymin_gt_scalato)
			#da eseguire solo se il layout gt è capovolto rispetto a quello segmentato (con gli xml delle scuole non succede, con quelli del survey si)
			if flip_dataset :
				y_traslato = altezza - y_traslato
			punti.append((x_traslato,y_traslato))
		x = int(bordi[0].get('x'))
		y = int(bordi[0].get('y'))
		x_scalato = x*fattore_x
		y_scalato = y*fattore_y
		x_traslato = x_scalato+(xmin-xmin_gt_scalato)
		y_traslato = y_scalato+(ymin-ymin_gt_scalato)
		#come sopra
		if flip_dataset :
			y_traslato = altezza - y_traslato
		punti.append((x_traslato,y_traslato))
		poligono = Polygon(punti)
		if not poligono.is_valid:
			poligono = poligono.buffer(0)
		stanze_gt.append(poligono)

	#disegno stanze ground truth
	print "AGGIUNGERE PRINT DELLA STANZA GT"
	'''
	fig = plt.figure()
	plt.title('stanze_gt')
	ax = fig.add_subplot(111)
	for index,s in enumerate(stanze_gt):
		f_patch = PolygonPatch(s,fc='WHITE',ec='BLACK')
		ax.add_patch(f_patch)
		ax.set_xlim(xmin-20,xmax+20)
		ax.set_ylim(ymin-20,ymax+20)

	plt.show()'''

	return stanze_gt



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
		else : print "WARNING QUI NON VA NULLA 1"
	
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







