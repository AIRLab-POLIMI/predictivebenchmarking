from util import medial as mdl
from object import Superficie as fc

import networkx as nx
import matplotlib.pyplot as plt
import cv2
from util import disegna as dsg

from descartes import PolygonPatch


def get_grafo(metricMap, stanze, estremi, colori, parametri_obj):
	'''
	INPUT: la mappa metrica, la lista di stanze, i cluster delle celle, estremi e colori.
	Trova le connessioni tra le stanze con medial axis.
	OUTPUT il grafo topologico, il dizionario di posizioni dei nodi, le coppie di stanze collegate e le coordinate dei collegamenti. 
	'''
	
	#----------------------------------MEDIAL AXIS---------------------------------------
	if cv2.__version__[0] == '3' :
		flag = cv2.IMREAD_GRAYSCALE
	elif cv2.__version__[0] == '2' :
		flag = cv2.CV_LOAD_IMAGE_GRAYSCALE
	else :
		raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*') 

	im_gray = cv2.imread(metricMap, flag)

	(thresh, im_bw) = cv2.threshold(im_gray, 240, 255, cv2.THRESH_BINARY_INV)
	#cannyEdges = cv2.Canny(im_gray, parametri_obj.minVal, parametri_obj.maxVal, apertureSize=parametri_obj.apertureSize)
	#im_bw =cannyEdges
	medialAxis, distanceMap, points, b3, distance= mdl.medial_points(im_bw)
	print "lunghezza di medialAxis:",len(medialAxis)
	stanze_collegate = []
	stanze_collegate, porte_colleganti = mdl.trovaCollegamenti(stanze,stanze_collegate,medialAxis)
	print len(stanze_collegate)
	print len(porte_colleganti)
	
	#per ogni punto dello skeleton, vado a vedere se e' in prossimita' dei bordi di qualche stanza. Se le stanze vicine al punto hanno label diverse, vuol dire che in quel punto c'e' una porta, o comunque un passaggio diretto.
	#print stanze_collegate, porte_colleganti
	#----------------------------------GRAFO---------------------------------------------
	#G, pos = crea_grafo(stanze, stanze_collegate, estremi, colori)
	#------------------------------------------------------------------------------------
	return stanze_collegate, porte_colleganti, distanceMap, points, b3
	
def  crea_grafo(stanze, stanze_collegate, estremi, colori):

	# xmin = estremi[0]
# 	xmax = estremi[1]
# 	ymin = estremi[2]
# 	ymax = estremi[3]

	#creo grafo, ogni nodo corrisponde a una label
	G=nx.Graph()
	for i,s in enumerate(stanze):
		G.add_node(i)
		
	#gli edge li prendo da stanze_collegate
	G.add_edges_from(stanze_collegate)
	#creo un dizionario che contiene le posizioni dei nodi. Le posizioni sono i representative point delle stanze corrispondenti. Creo la prima chiave del dizionario, poi aggiungo le restanti con un ciclo for.
	pos = {0: (stanze[0].representative_point().x,stanze[0].representative_point().y)}
	for i,s in enumerate(stanze[1:]):
		pos[i+1] = (s.representative_point().x,s.representative_point().y)
	#aggiungo l'attributo posizione ad ogni nodo
	for n, p in pos.iteritems():
		G.node[n]['pos'] = p
		
	print "il grafo ha tot edges", len(G.edges())
	
		
	#---- decimo plot --> con questo plot disegno i nodi relative alle stanze.
# 	#plotto le stanze
# 	fig = plt.figure()
# 	plt.title('10.grafo topologico')
# 	ax = fig.add_subplot(111)
# 	for index,s in enumerate(stanze):
# 		f_patch = PolygonPatch(s,fc=colori[index],ec='BLACK')
# 		ax.add_patch(f_patch)
# 		ax.set_xlim(xmin,xmax)
# 		ax.set_ylim(ymin,ymax)
# 
# 	#plotto il grafo
# 	nx.draw_networkx_nodes(G,pos,node_color='w')
# 	nx.draw_networkx_edges(G,pos)
# 	nx.draw_networkx_labels(G,pos)
# 
# 	#plotto gli edges come linee da un representative point a un altro, perche' con solo drawedges non li plotta. Forse sono nascosti dai poligoni.
# 	for coppia in stanze_collegate:
# 		i1 = stanze[coppia[0]]
# 		i2 = stanze[coppia[1]]
# 		p1 = i1.representative_point()
# 		p2 = i2.representative_point()
# 		plt.plot([p1.x,p2.x],[p1.y,p2.y],color='k',ls = 'dotted', lw=0.5)
# 
# 	plt.show() #visualizzo il grafo topologico.	

	#plotto le stanze con nodi
	#dsg.plot_nodi_e_stanze(colori,estremi, G, pos, stanze, stanze_collegate, filepath = filepath)
	
	return G, pos

def get_stanze_non_collegate(stanze, stanze_collegate):

	indice_stanze_non_collegate = []	
	s_collegate_list = []
	stanze_non_collegate =[]
	for collegamento in stanze_collegate:
		for s in collegamento:
			if s not in s_collegate_list:
				s_collegate_list.append(s)
				
	for indice_stanza in xrange(0, len(stanze)):
		if indice_stanza not in s_collegate_list:
			indice_stanze_non_collegate.append(indice_stanza)
	
	print "gli indici sono: ", indice_stanze_non_collegate
	print len(indice_stanze_non_collegate)
	
	for indice in indice_stanze_non_collegate:
		stanze_non_collegate.append(stanze[indice])
	
	return stanze_non_collegate
	