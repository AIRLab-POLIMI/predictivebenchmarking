from matplotlib import pyplot as plt
from PIL import Image
import cv2
import random
from descartes import PolygonPatch
from matplotlib.path import Path
import matplotlib.path as mplPath
import matplotlib.patches as patches
import networkx as nx
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import os
import matplotlib
import random
from shapely.geometry import Point
from shapely.geometry import Polygon
from matplotlib.ticker import NullLocator


def setup_plot(x_span,y_span,xmin,xmax,ymin,ymax):

	plt.clf()
	plt.cla()
	plt.close()
	fig, ax = plt.subplots(figsize=(x_span/100,y_span/100),dpi=100)
	#fig = plt.figure(figsize=(x_span/100, y_span/100), dpi=100)
	# VERY IMPORTANT: if this is not set, the building will be stretched and lose its original proportion!
	plt.axis('equal')
	#ax = fig.add_subplot(111)
	ax.axis('off')
	#ax.set_xticks([])
	#ax.set_yticks([])
	ax.set_xlim(xmin-10,xmax+10)
	ax.set_ylim(ymin-10,ymax+10)
	ax.xaxis.set_major_locator(NullLocator())
	ax.yaxis.set_major_locator(NullLocator())
	return fig,ax

def disegna(lista):
	'''
	disegna una lista di Segmenti
	'''
	
	ascisse = []
	ordinate = []	
	for muro in lista:
		ascisse.append(muro.x1)
		ascisse.append(muro.x2)
		ordinate.append(muro.y1)
		ordinate.append(muro.y2)
		plt.plot(ascisse,ordinate, color='k', linewidth=2.0)
		del ascisse[:]
		del ordinate[:]
	plt.title('test')

def save_scaled(savename,x_span):
	plt.savefig(savename,bbox_inches = 'tight',pad_inches=0,dpi=100)
	actual_x_span=cv2.imread(savename).shape[1]
	dpi = 100*x_span/actual_x_span
	plt.savefig(savename,bbox_inches = 'tight',pad_inches=0,dpi=dpi)

def disegna_map(map,savefig = True, format='pdf', filepath = '.', savename = '0_Map',title=False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0) :
	'''
	Stampa la mappa di ingresso

	'''
	fig,ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	ax.imshow(map,interpolation='none')

	savename = os.path.join(filepath, savename+'.'+format)

	if title :
		ax.set_title('0.metric map')
	if savefig :
		save_scaled(savename,x_span)
	else:
		plt.show()

def disegna_hough(img, lines,savefig = True, format='pdf', filepath = '.', savename ='2_Hough', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	plotta le hough lines

	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)


	img2 = img.copy()
	if(len(img2.shape)==2):
		img2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2RGB)
	if title :
		ax.set_title('1.hough lines') #1.primo plot

	for x1,y1,x2,y2 in lines:
    		cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)
	ax.imshow(img2,cmap='Greys')
	if savefig :
		save_scaled(savename,x_span)
	else:
		plt.show()
	'''
	ascisse = []
	ordinate = []
	for l in lines[0]:
		ascisse.extend((l[0],l[2]))
		ordinate.extend((l[1],l[3]))
		plt.plot(ascisse,ordinate, color='k', linewidth=2.0)
		ascisse = []
		ordinate = []
	plt.show()
	'''
def disegna_grafici_per_accuracy(stanze, stanze_gt, savefig = True, format='pdf', filepath = '.', savename = '9_accuracy', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):

	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('accuracy')
		
	for poly in stanze:
		x,y = poly.exterior.xy
		ax.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
	for poly in stanze_gt:
		x,y = poly.exterior.xy
		ax.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )	
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
		
def disegna_GT_parziali(stanze_gt, stanze_gt_con_frontira, savefig = True, format='pdf', filepath = '.', savename = '20_stanzeGT', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna stanzeGT
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('stanzeGT')
		
	for poly in stanze_gt:
		trovato = False
		for p in stanze_gt_con_frontira:
			if p.equals(poly):
				trovato = True
		if trovato == True:
			x,y = poly.exterior.xy
			ax.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
		else:
			x,y = poly.exterior.xy
			ax.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_area_reale_GT_parziali(stanze_gt, stanze_gt_con_frontira,contorno,xmin,ymin,xmax,ymax, savefig = True, format='pdf', filepath = '.', savename = '20_stanzeGT', title = False,x_span=0,y_span=0):
	'''
	disegna stanzeGT
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)
	

	if title:
		ax.set_title('stanzeGT')
		
	for poly in stanze_gt:
		trovato = False
		for p in stanze_gt_con_frontira:
			if p.equals(poly):
				trovato = True
		if trovato == True:
			x,y = poly.exterior.xy
			ax.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2)
			p = poly - (poly.intersection(contorno))
			#p.buffer(0)
			max = 0
			best = None
			print type(p)
			if type(p) == Polygon:
				best = p
			else:
				for po in p.geoms:
					if po.area >max:
						max = po.area
						best = po
			f_patch = PolygonPatch(best,fc='#FF3300',ec='BLACK') 
			ax.add_patch(f_patch)
			#ax.set_xlim(xmin,xmax)
			#ax.set_ylim(ymin,ymax)	
		else:
			x,y = poly.exterior.xy
			ax.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()


def disegna_stanze_stanzeGt_contorno(stanze, stanze_gt, contours, savefig = True, format='pdf', filepath = '.', savename = '9_accuracy', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna stanze, stanzeGT ed il contorno tutto insieme.
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('accuracy')
		
	for poly in stanze:
		x,y = poly.exterior.xy
		ax.plot(x,y, color= 'BLACK', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
	for poly in stanze_gt:
		x,y = poly.exterior.xy
		ax.plot(x,y, color= 'RED', alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
	
	#contorno
	ascisse = []
	ordinate = []
	for c1 in contours:
		ascisse.append(c1[0][0])
		ordinate.append(c1[0][1])
	ax.plot(ascisse,ordinate,color='0.8',linewidth=3.0)
	del ascisse[:]
	del ordinate[:]
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_stanza_vuote(stanze, savefig = True, format='pdf', filepath = '.', savename = '9_accuracy', title = False, nero = True):
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('accuracy')
	
	if nero ==True:
		colore = 'BLACK'
	else:
		colore = 'RED'
	
	for poly in stanze:
		x,y = poly.exterior.xy
		ax.plot(x,y, color= colore, alpha = 0.7, linewidth = 3, solid_capstyle= 'round', zorder = 2 )
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_canny(edges_canny, savefig = True, format='pdf', filepath = '.', savename = '1_Canny', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	plotta gli edge individuati da canny
	'''

	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('canny')
	ax.imshow(edges_canny,cmap='Greys')
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_segmenti(lista,savefig = True, format='pdf', filepath = '.', savename = '3_Muri', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna i segmenti passati come lista
	'''
	fig,ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('3.Muri') #2.muri, plotta i muri 
	ascisse = []
	ordinate = []
	for s in lista:
		x1 = s.x1
		x2 = s.x2
		y1 = s.y1
		y2 = s.y2
		ascisse.extend((x1,x2))
		ordinate.extend((y1,y2))
		ax.plot(ascisse,ordinate, color='k',linewidth=2)
		del ascisse[:]
		del ordinate[:]
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_segmenti_e_raggi_cerchio(lista, linee, savefig = True, format='pdf', filepath = '.', savename = '3_Muri', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna i segmenti passati come lista e i raggi del cerchio attorno alla frontiera
	'''
	fig,ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('3.Muri') #2.muri, plotta i muri 
	ascisse = []
	ordinate = []
	for s in lista:
		x1 = s.x1
		x2 = s.x2
		y1 = s.y1
		y2 = s.y2
		ascisse.extend((x1,x2))
		ordinate.extend((y1,y2))
		ax.plot(ascisse,ordinate, color='k',linewidth=2)
		del ascisse[:]
		del ordinate[:]
	
	for line in linee:	
		x, y = line.xy
		ax.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
	
	#ax.set_xlim(xmin-1,xmax+1)
	#ax.set_ylim(ymin-1,ymax+1)
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
def disegna_segmenti_raggi_cerchio_contorno(vertici,xmin,ymin,xmax,ymax, lista, linee, savefig = True, format='pdf', filepath = '.', savename = '3_Muri', title = False,x_span=0,y_span=0):
	'''
	disegna i segmenti passati come lista e i raggi del cerchio attorno alla frontiera
	'''
	fig,ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title:
		ax.set_title('3.Muri') #2.muri, plotta i muri 
	
	
	#linee cerchio
	for line in linee:	
		x, y = line.xy
		ax.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=-5)
	#contorno
	bbPath = mplPath.Path(vertici)
	patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
	ax.add_patch(patch)
	ax.set_xlim(xmin-1,xmax+1)
	ax.set_ylim(ymin-1,ymax+1)
	'''
	#muri
	ascisse = []
	ordinate = []
	for s in lista:
		x1 = s.x1
		x2 = s.x2
		y1 = s.y1
		y2 = s.y2
		ascisse.extend((x1,x2))
		ordinate.extend((y1,y2))
		ax.plot(ascisse,ordinate, color='k',linewidth=2)
		del ascisse[:]
		del ordinate[:]
	'''
	
	#ax.set_xlim(xmin-1,xmax+1)
	#ax.set_ylim(ymin-1,ymax+1)
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def get_colors(labels):
	colori_assegnati = []
	#colors = []
	#colors.extend(('#800000','#DC143C','#FF0000','#FF7F50','#F08080','#FF4500','#FF8C00','#FFD700','#B8860B','#EEE8AA','#BDB76B','#F0E68C','#808000','#9ACD32','#7CFC00','#ADFF2F','#006400','#90EE90','#8FBC8F','#00FA9A','#20B2AA','#00FFFF','#4682B4','#1E90FF','#000080','#0000FF','#8A2BE2','#4B0082','#800080','#FF00FF','#DB7093','#FFC0CB','#F5DEB3','#8B4513','#808080'))
	cmap = matplotlib.cm.get_cmap('Paired')

	for label in set(labels):
		rgba = cmap(random.random())
		hex =matplotlib.colors.rgb2hex(rgba)
		#col = random.choice(colors)
		colori_assegnati.append(hex)
	return colori_assegnati

def disegna_dbscan(labels, facce, facce_poligoni, xmin, ymin, xmax, ymax, edges, contours,savefig = True, format='pdf', filepath = '.', savename = '6_DBSCAN', title = False,x_span=0,y_span=0):
	'''
	disegna le facce in base ai cluster ottenuti dal dbscan. Facce dello stesso cluster hanno stesso colore.
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	colori_assegnati = []
	#colors = []
	#colors.extend(('#800000','#DC143C','#FF0000','#FF7F50','#F08080','#FF4500','#FF8C00','#FFD700','#B8860B','#EEE8AA','#BDB76B','#F0E68C','#808000','#9ACD32','#7CFC00','#ADFF2F','#006400','#90EE90','#8FBC8F','#00FA9A','#20B2AA','#00FFFF','#4682B4','#1E90FF','#000080','#0000FF','#8A2BE2','#4B0082','#800080','#FF00FF','#DB7093','#FFC0CB','#F5DEB3','#8B4513','#808080'))
	#plt.subplot(224)
	cmap = matplotlib.cm.get_cmap('Paired')
	if title :
		ax.set_title('6.dbscan')
	for label in set(labels):
		rgba = cmap(random.random())
		col =matplotlib.colors.rgb2hex(rgba)#converto in esadecimale
		#col = random.choice(colors)
		colori_assegnati.append(col)
		for index,l in enumerate(labels):
			if (l == label):
				f = facce[index]
				f_poly = facce_poligoni[index]
				f_patch = PolygonPatch(f_poly,fc=col,ec='BLACK')
				ax.add_patch(f_patch)
				ax.set_xlim(xmin,xmax)
				ax.set_ylim(ymin,ymax)
				sommax = 0
				sommay = 0
				for b in f.bordi:
					sommax += (b.x1)+(b.x2)
					sommay += (b.y1)+(b.y2)
				xtesto = sommax/(2*len(f.bordi))
				ytesto = sommay/(2*len(f.bordi))
				ax.text(xtesto,ytesto,str(l),fontsize=8)
	ascisse = []
	ordinate = []
	for edge in edges:
		if (edge.weight>=0.3):#era 0.3
			ascisse.append(edge.x1)
			ascisse.append(edge.x2)
			ordinate.append(edge.y1)
			ordinate.append(edge.y2)
			ax.plot(ascisse,ordinate, color='k', linewidth=4.0)
			del ascisse[:]
			del ordinate[:]
	#questo pezzo se sto usando il suo modo di trovare il contorno va tolto 
	#----------------------da commentare
	
	ascisse = []
	ordinate = []
	for c1 in contours:
		
		ascisse.append(c1[0][0])
		ordinate.append(c1[0][1])
		
	ax.plot(ascisse,ordinate,color='0.8',linewidth=3.0)
	del ascisse[:]
	del ordinate[:]
	
	#-----------------------da decommentare se uso il suo metodo per riconoscere il contorno
	'''
	ascisse = []
	ordinate = []
	for c1 in contours:
		for c2 in c1:
			ascisse.append(c2[0][0])
			ordinate.append(c2[0][1])
		ax.plot(ascisse,ordinate,color='0.8',linewidth=3.0)
		del ascisse[:]
		del ordinate[:]
	'''
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
	return (colori_assegnati, fig, ax)

def disegna_sovrapposizione_predizione(spazi_iniziali, spazi_predetti, contours , colori, xmin, ymin, xmax, ymax, savefig  =  True, format='pdf', filepath = '.', savename = '17_sovrapposizione_di_tutto', title = False,x_span=0,y_span=0):
	'''
	disegna la stanze iniziali, il contorno, e le stanze predette, tutto spvrapposto.
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title :
		ax.set_title('17_sovrapposizione_di_tutto')
	
	#plotto le stanze parziali predette
	for index,s in enumerate(spazi_predetti):
		# if s.out == False and s.parziale == False:
# 			f_patch = PolygonPatch(s.spazio,fc=colori[index],ec='BLACK') 
# 			ax.add_patch(f_patch)
# 			ax.set_xlim(xmin,xmax)
# 			ax.set_ylim(ymin,ymax)
# 		elif s.out == True:
# 			f_patch = PolygonPatch(s.spazio,fc='white',ec='BLACK') 
# 			ax.add_patch(f_patch)
# 			ax.set_xlim(xmin,xmax)
# 			ax.set_ylim(ymin,ymax)
# 			#ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("out"),fontsize=8)
		if s.out == False and s.parziale == True:
			f_patch = PolygonPatch(s.spazio,fc='#C0C0C0',ec='BLACK',alpha = 0.5) 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
			#ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("parz"),fontsize=8)
	
	#plotto le stanze iniziali 
	for index,s in enumerate(spazi_iniziali):
		if s.out == False and s.parziale == False:
			f_patch = PolygonPatch(s.spazio,fc=colori[index],ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
		elif s.out == True:
			f_patch = PolygonPatch(s.spazio,fc='white',ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
			#ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("out"),fontsize=8)
		elif s.out == False and s.parziale == True:
			f_patch = PolygonPatch(s.spazio,fc='gray',ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
			#ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("parz"),fontsize=8)
	
	
	#plotto il contorno
	ascisse = []
	ordinate = []
	for c1 in contours:
		
		ascisse.append(c1[0][0])
		ordinate.append(c1[0][1])
		
	ax.plot(ascisse,ordinate,color='0.8',linewidth=3.0)
	del ascisse[:]
	del ordinate[:]
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
	return (fig, ax)

def disegna_stanze(stanze, colori, xmin, ymin, xmax, ymax,savefig  =  True, format='pdf', filepath = '.', savename = '8_Stanze', title = False,x_span=0,y_span=0):
	'''
	disegna il layout delle stanze.
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	#plt.subplot(224)
	if title :
		ax.set_title('7.stanze')
	
	for index,s in enumerate(stanze):
		f_patch = PolygonPatch(s,fc=colori[index],ec='BLACK') 
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
	return (fig, ax)
def disegna_poligoni_interni_esterni(celle_poligoni, out_poligoni, parz_poligoni, xmin, ymin, xmax, ymax,savefig  =  True, format='pdf', filepath = '.', savename = '8_b_poligoni_in_ed_out', title = False,x_span=0,y_span=0):
	'''
	disegna il layout delle stanze.
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	#plt.subplot(224)
	if title :
		ax.set_title('7.poli_in_out')
	
	for index,s in enumerate(celle_poligoni):
		
		f_patch = PolygonPatch(s,fc='orange',ec='BLACK') 
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
	for index,s in enumerate(parz_poligoni):
		
		f_patch = PolygonPatch(s,fc='orange',ec='BLACK') 
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
		
	for index,s in enumerate(out_poligoni):	
		f_patch = PolygonPatch(s,fc='#FFFFFF',ec='BLACK') 
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
	return (fig, ax)

def disegna_spazi(spazi,colori, xmin, ymin, xmax, ymax, savefig  =  True, format='pdf', filepath = '.', savename = '8_Stanze', title = False,x_span=0,y_span=0):
	'''
	disegna il layout delle stanze.
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	#plt.subplot(224)
	if title :
		ax.set_title('8.stanze')
	 
	for index,s in enumerate(spazi):
		if s.out == False and s.parziale == False:
			f_patch = PolygonPatch(s.spazio,fc=colori[index],ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
		elif s.out == True:
			f_patch = PolygonPatch(s.spazio,fc='white',ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
			ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("out"),fontsize=8)
		elif s.out == False and s.parziale == True:
			f_patch = PolygonPatch(s.spazio,fc='gray',ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
			ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("parz"),fontsize=8)
		#vado ad evidenziare i bordi di una stanza che toccano il bordo dell'immagine(questo per indicare che non posso proseguire da quella parte con la predizione)
		for cellette in s.cells:
			bordi = cellette.c.bordi
			ascisse = []
			ordinate = []
			for b in bordi:
				if b.cluster_spaziale == 'bordo1' or b.cluster_spaziale == 'bordo2' or b.cluster_spaziale == 'bordo3' or b.cluster_spaziale == 'bordo4':
					#se tocco le extended dei bordi
					x1 = b.x1
					x2 = b.x2
					y1 = b.y1
					y2 = b.y2
					ascisse.extend((x1,x2))
					ordinate.extend((y1,y2))
					ax.plot(ascisse,ordinate, color='r',linewidth=2)
					del ascisse[:]
					del ordinate[:]
	

	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
	return (fig, ax)

def disegna_spazi_con_pareti_nascoste(spazi,colori, xmin, ymin, xmax, ymax,edges, savefig  =  True, format='pdf', filepath = '.', savename = '8_Stanze', title = False,x_span=0,y_span=0):
	'''
	disegna il layout delle stanze.
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	#plt.subplot(224)
	if title :
		ax.set_title('8.stanze')
	 
	for index,s in enumerate(spazi):
		if s.out == False and s.parziale == False:
			f_patch = PolygonPatch(s.spazio,fc=colori[index],ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
		elif s.out == True:
			f_patch = PolygonPatch(s.spazio,fc='white',ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
			ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("out"),fontsize=8)
		elif s.out == False and s.parziale == True:
			f_patch = PolygonPatch(s.spazio,fc='gray',ec='BLACK') 
			ax.add_patch(f_patch)
			ax.set_xlim(xmin,xmax)
			ax.set_ylim(ymin,ymax)
			ax.text(s.spazio.representative_point().x,s.spazio.representative_point().y,str("parz"),fontsize=8)
		#vado ad evidenziare i bordi di una stanza che toccano il bordo dell'immagine(questo per indicare che non posso proseguire da quella parte con la predizione)
		for cellette in s.cells:
			bordi = cellette.c.bordi
			ascisse = []
			ordinate = []
			for b in bordi:
				if b.cluster_spaziale == 'bordo1' or b.cluster_spaziale == 'bordo2' or b.cluster_spaziale == 'bordo3' or b.cluster_spaziale == 'bordo4':
					#se tocco le extended dei bordi
					x1 = b.x1
					x2 = b.x2
					y1 = b.y1
					y2 = b.y2
					ascisse.extend((x1,x2))
					ordinate.extend((y1,y2))
					ax.plot(ascisse,ordinate, color='r',linewidth=2)
					del ascisse[:]
					del ordinate[:]
	
	
	ascisse = []
	ordinate = []
	for edge in edges:
		if (edge.weight>=0.3):
			ascisse.append(edge.x1)
			ascisse.append(edge.x2)
			ordinate.append(edge.y1)
			ordinate.append(edge.y2)
			ax.plot(ascisse,ordinate, color='k', linewidth=1.0)
			del ascisse[:]
			del ordinate[:]

		
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
	return (fig, ax)

def disegna_contorno(vertici,xmin,ymin,xmax,ymax,savefig = True, format='pdf', filepath = '.', savename = '4_Contorno', title = False,x_span=0,y_span=0):
	'''
	disegna il contorno esterno della mappa metrica
	'''

	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)



	bbPath = mplPath.Path(vertici)
	patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
	ax.add_patch(patch)
	ax.set_xlim(xmin-1,xmax+1)
	ax.set_ylim(ymin-1,ymax+1)
	if title :
		ax.set_title('4.contorno esterno')
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

# def disegna_contorno(vertici,xmin,ymin,xmax,ymax):
# 	print vertici
# 	bbPath = mplPath.Path(vertici)
# 	fig = plt.figure()
# 	ax = fig.add_subplot(111)
# 	patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
# 	ax.add_patch(patch)
# 	ax.set_xlim(xmin-1,xmax+1)
# 	ax.set_ylim(ymin-1,ymax+1)
# 	plt.show()

def disegna_contorno_e_centro_frontiera(vertici,lista_centri,xmin,ymin,xmax,ymax,savefig = True, format='pdf', filepath = '.', savename = '4_Contorno', title = False,x_span=0,y_span=0):
	'''
	disegna il contorno esterno della mappa metrica
	'''

	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)



	bbPath = mplPath.Path(vertici)
	patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
	ax.add_patch(patch)
	
	x= []
	y =[]
	for centro in lista_centri: #i centri sono flippati
		x.append(centro[0])
		y.append(centro[1])
	ax.plot(x,y, 'ro')
	ax.set_xlim(xmin-1,xmax+1)
	ax.set_ylim(ymin-1,ymax+1)
	
	if title :
		ax.set_title('4.contorno esterno')
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_contorno_e_area_vista(vertici,cerchio,xmin,ymin,xmax,ymax,savefig = True, format='pdf', filepath = '.', savename = '4_Contorno', title = False,x_span=0,y_span=0):
	'''
	disegna il contorno con l'area che potrei vedere in seguito dalle metriche
	'''

	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)



	bbPath = mplPath.Path(vertici)
	patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
	ax.add_patch(patch)
	
	#disegno cerchio
	patch1 = PolygonPatch(cerchio, fc='gray', ec='BLACK', alpha=0.2, zorder=1)
	ax.add_patch(patch1)
	
	ax.set_xlim(xmin-1,xmax+1)
	ax.set_ylim(ymin-1,ymax+1)
	
	if title :
		ax.set_title('4.contorno esterno')
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_contorno_e_retta_frontiera(vertici,line,xmin,ymin,xmax,ymax,savefig = True, format='pdf', filepath = '.', savename = '4_Contorno', title = False,x_span=0,y_span=0):
	'''
	disegna il contorno e la retta della frontiera
	'''

	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)



	bbPath = mplPath.Path(vertici)
	patch = patches.PathPatch(bbPath, facecolor='orange', lw=2)
	ax.add_patch(patch)
	
	x, y = line.xy
	ax.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
	
	ax.set_xlim(xmin-1,xmax+1)
	ax.set_ylim(ymin-1,ymax+1)
	
	if title :
		ax.set_title('4.contorno esterno')
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()


def disegna_cluster_angolari(lista_muri, cluster_angolari, savefig = True,  format='pdf', filepath = '.',savename = '5b_Contorno', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna con lo stesso colore i muri con stesso cluster angolare
	''' 
	ascisse = []
	ordinate = []
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title: 
		ax.set_title('cluster angolari')
	#per ogni cluster angolare visualizzo in rosso i segmenti che vi appartengono, in nero quelli che non vi appartengono
	for c in set(cluster_angolari):
		for muro1 in lista_muri:
			if muro1.cluster_angolare == c:
				ascisse.extend((muro1.x1,muro1.x2))
				ordinate.extend((muro1.y1,muro1.y2))
				ax.plot(ascisse,ordinate, color='r', linewidth=2.0)
				del ascisse[:]
				del ordinate[:]
			else:
				ascisse.extend((muro1.x1,muro1.x2))
				ordinate.extend((muro1.y1,muro1.y2))
				ax.plot(ascisse,ordinate, color='g', linewidth=2.0)
				del ascisse[:]
				del ordinate[:]
		
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_cluster_angolari_corretto(lista_muri, cluster_angolari, savefig = True,  format='pdf', filepath = '.',savename = '5b_cluster_angolare', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna con lo stesso colore i muri con stesso cluster angolare
	''' 
	ascisse = []
	ordinate = []
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)
	numofcolors = len(set(cluster_angolari))
	cm = plt.get_cmap("nipy_spectral")
	cNorm = colors.Normalize(vmin=0, vmax=numofcolors)
	scalarMap = cmx.ScalarMappable(norm=cNorm, cmap = cm)
	if title: 
		ax.set_title('cluster angolari')
	for index,c in enumerate(np.random.permutation(list(set(cluster_angolari)))):
		for muro in lista_muri:
			if muro.cluster_angolare == c:
				ascisse.extend((muro.x1,muro.x2))
				ordinate.extend((muro.y1,muro.y2))
				ax.plot(ascisse,ordinate, color=colors.rgb2hex(scalarMap.to_rgba(index)), linewidth=2.0)
				del ascisse[:]
				del ordinate[:]
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegno_mura_segmenti_stanze(stanze, colori, xmin, ymin, xmax, ymax, cluster_spaziali, lista_muri,savefig = True, format='pdf', filepath = '.', savename = '14_tutto', title = False,x_span=0,y_span=0):
	'''
	mura, segemnti pesanti e stanze
	'''
	
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	ascisse = []
	ordinate = []
	numofcolors = len(set(cluster_spaziali))
	cm = plt.get_cmap("nipy_spectral")
	cNorm = colors.Normalize(vmin=0, vmax=numofcolors)
	scalarMap = cmx.ScalarMappable(norm=cNorm, cmap = cm)
	#plt.subplot(222)
	if title :
		ax.set_title('4.spatial clusters')
	for index,c in enumerate(np.random.permutation(list(set(cluster_spaziali)))):
		for muro in lista_muri:
			if muro.cluster_spaziale == c:
				ascisse.extend((muro.x1,muro.x2))
				ordinate.extend((muro.y1,muro.y2))
				ax.plot(ascisse,ordinate, color=colors.rgb2hex(scalarMap.to_rgba(index)), linewidth=2.0)
				del ascisse[:]
				del ordinate[:]
	'''
	ascisse = []
	ordinate = []
	for edge in edges:
		if (edge.weight>=0.3):#era 0.3
			ascisse.append(edge.x1)
			ascisse.append(edge.x2)
			ordinate.append(edge.y1)
			ordinate.append(edge.y2)
			ax.plot(ascisse,ordinate, color='k', linewidth=4.0)
			del ascisse[:]
			del ordinate[:]
	'''
	#stanze
	for index,s in enumerate(stanze):
		f_patch = PolygonPatch(s,fc=colori[index],ec='BLACK') 
		ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
	
	
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
		
def disegna_pareti(edges, savefig = True, format='pdf', filepath = '.', savename = '14_paretis', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	ascisse = []
	ordinate = []
	ascisse = []
	ordinate = []
	for edge in edges:
		if (edge.weight>=0.3):#era 0.3
			ascisse.append(edge.x1)
			ascisse.append(edge.x2)
			ordinate.append(edge.y1)
			ordinate.append(edge.y2)
			ax.plot(ascisse,ordinate, color='k', linewidth=4.0)
			del ascisse[:]
			del ordinate[:]
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()


def disegna_cluster_spaziali(cluster_spaziali, lista_muri,savefig = True, format='pdf', filepath = '.', savename = '5_MURA', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna con lo stesso colore i muri con stesso cluster spaziale
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	ascisse = []
	ordinate = []
	numofcolors = len(set(cluster_spaziali))
	cm = plt.get_cmap("nipy_spectral")
	cNorm = colors.Normalize(vmin=0, vmax=numofcolors)
	scalarMap = cmx.ScalarMappable(norm=cNorm, cmap = cm)
	#plt.subplot(222)
	if title :
		ax.set_title('4.spatial clusters')
	for index,c in enumerate(np.random.permutation(list(set(cluster_spaziali)))):
		for muro in lista_muri:
			if muro.cluster_spaziale == c:
				ascisse.extend((muro.x1,muro.x2))
				ordinate.extend((muro.y1,muro.y2))
				ax.plot(ascisse,ordinate, color=colors.rgb2hex(scalarMap.to_rgba(index)), linewidth=2.0)
				del ascisse[:]
				del ordinate[:]
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
	
	#metodo alternativo
	'''
	#per ogni cluster spaziale visualizzo in rosso i segmenti che vi appartengono, in nero quelli che non vi appartengono
	for c in set(cluster_spaziali):
		for muro1 in lista_muri:
			if muro1.cluster_spaziale == c:
				ascisse.extend((muro1.x1,muro1.x2))
				ordinate.extend((muro1.y1,muro1.y2))
				plt.plot(ascisse,ordinate, color='r', linewidth=4.0)
				del ascisse[:]
				del ordinate[:]
			else:
				ascisse.extend((muro1.x1,muro1.x2))
				ordinate.extend((muro1.y1,muro1.y2))
				plt.plot(ascisse,ordinate, color='#51af42', linewidth=2.0)
				del ascisse[:]
				del ordinate[:]
		plt.show()

	raw_input("Press enter to exit")
	'''


def disegna_extended_segments(extended_segments, lista_muri, savefig = True, format='pdf', filepath = '.', savename = '7_Extended', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna in nero i muri di lista_muri, in rosso gli extended_segments
	'''
	ascisse = []
	ordinate = []
	#plt.subplot(223)
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title :
		plt.ax.set_title('7.extended segments')
	for e in lista_muri:		
		ascisse.append(e.x1)
		ascisse.append(e.x2)
		ordinate.append(e.y1)
		ordinate.append(e.y2)
		ax.plot(ascisse,ordinate, color='k', linewidth=3.0)
		del ascisse[:]
		del ordinate[:]
	
	for e in extended_segments:		
		ascisse.append(e.x1)
		ascisse.append(e.x2)
		ordinate.append(e.y1)
		ordinate.append(e.y2)
		ax.plot(ascisse,ordinate, color='r', linewidth=1.5)
		del ascisse[:]
		del ordinate[:]

	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_extended_segments_e_contorno(vertici,xmin,ymin,xmax,ymax,extended_segments, savefig = True, format='pdf', filepath = '.', savename = '7_Extended_cotorno', title = False,x_span=0,y_span=0):
	'''
	disegna in nero i muri di lista_muri, in rosso gli extended_segments
	'''
	ascisse = []
	ordinate = []
	#plt.subplot(223)
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	if title :
		plt.ax.set_title('7.extended segments contorno')
	
	for e in extended_segments:		
		ascisse.append(e.x1)
		ascisse.append(e.x2)
		ordinate.append(e.y1)
		ordinate.append(e.y2)
		ax.plot(ascisse,ordinate, color='r', linewidth=1.5)
		del ascisse[:]
		del ordinate[:]
	
	bbPath = mplPath.Path(vertici)
	patch = patches.PathPatch(bbPath, facecolor='#DDDDDD', lw=2)
	ax.add_patch(patch)
	ax.set_xlim(xmin-1,xmax+1)
	ax.set_ylim(ymin-1,ymax+1)
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()		
		
def disegna_distance_transform(distanceMap, savefig = True, format='pdf', filepath = '.', savename = '10_distance_transform', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna la distance transforme
	'''

	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)
	
	if title :
		plt.title('10_distance_transform')
	
	#distanceMap = ndimage.distance_transform_edt(im_bw)
	plt.imshow(distanceMap)
	
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

#TODO: cancella questa funzione che non serve a nulla.
def disegna_distance_transform_e_stanze(distanceMap,stanze,colori, savefig = True, format='pdf', filepath = '.', savename = '10b_distance_and_stanze', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)
	
	if title :
		plt.title('10b_distance_and_stanze')
	
	plt.imshow(distanceMap)
	for index,s in enumerate(stanze):
		f_patch = PolygonPatch(s,fc=colori[index],ec='BLACK') 
		ax.add_patch(f_patch)
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_medial_axis(points,b3, savefig = True, format='png', filepath = '.', savename = '11_medial_axis', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna medial axis
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)
	
	if title :
		plt.title('11_medial_axis')
	
	ax.plot(points[:,0],points[:,1],'.')
	ax.imshow(b3,cmap='Greys')
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
		
def plot_nodi_e_stanze(colori,estremi, G, pos, spazi,stanze_collegate, savefig = True, format='pdf', filepath = '.', savename = '16_grafo_topologico', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna le stenze con i nodi corrispondenti
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)
	xmin = estremi[0]
	xmax = estremi[1]
	ymin = estremi[2]
	ymax = estremi[3]
	if title :
		plt.title('12_grafo_topologico')
	patches = []
	for index,s in enumerate(spazi):
		stanza = s.spazio
		#if len(s.exterior.coords)>12:
		f_patch = PolygonPatch(stanza,fc=colori[index],ec='BLACK')
		patches.append(f_patch)
		#for w in s.enlargedWalls:
		#	patches.append(PolygonPatch(w,fc='WHITE',ec='BLACK'))
	for f_patch in reversed(patches):
		ax.add_patch(f_patch)

	ax.set_xlim(xmin,xmax)
	ax.set_ylim(ymin,ymax)

	#plotto il grafo
	nx.draw_networkx_nodes(G,pos,node_color='w')
	nx.draw_networkx_edges(G,pos)
	#nx.draw_networkx_labels(G,pos)

	#plotto gli edges come linee da un representative point a un altro, perche' con solo drawedges non li plotta. Forse sono nascosti dai poligoni.
	for coppia in stanze_collegate:
		i1 = spazi[coppia[0]].spazio#stanze
		i2 = spazi[coppia[1]].spazio
		p1 = i1.representative_point()
		p2 = i2.representative_point()
		plt.plot([p1.x,p2.x],[p1.y,p2.y],color='k',ls = '--', lw=1.0, dashes=(2,2))	
	
		
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()

def disegna_cluster_mura(cluster_mura, lista_muri,savefig = True, format='pdf', filepath = '.', savename = '5d_cluster_muri', title = False,x_span=0,y_span=0,xmin=0,xmax=0,ymin=0,ymax=0):
	'''
	disegna con lo stesso colore i muri con stesso cluster spaziale
	'''
	fig, ax = setup_plot(x_span,y_span,xmin,xmax,ymin,ymax)
	savename = os.path.join(filepath, savename+'.'+format)

	ascisse = []
	ordinate = []
	numofcolors = len(set(cluster_mura))
	cm = plt.get_cmap("nipy_spectral")
	cNorm = colors.Normalize(vmin=0, vmax=numofcolors)
	scalarMap = cmx.ScalarMappable(norm=cNorm, cmap = cm)
	#plt.subplot(222)
	if title :
		ax.set_title('4.spatial clusters')
	for index,c in enumerate(np.random.permutation(list(set(cluster_mura)))):
		for muro in lista_muri:
			if muro.cluster_muro == c:
				ascisse.extend((muro.x1,muro.x2))
				ordinate.extend((muro.y1,muro.y2))
				ax.plot(ascisse,ordinate, color=colors.rgb2hex(scalarMap.to_rgba(index)), linewidth=2.0)
				del ascisse[:]
				del ordinate[:]
	if savefig :
		save_scaled(savename,x_span)
	else :
		plt.show()
