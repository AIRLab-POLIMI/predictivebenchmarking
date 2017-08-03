'''
un transitional kernel permette di modificare il mondo presente, e' utile per la costruzione della catena di Markov.
'''
from util import disegna as dsg


from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import Polygon

def split_stanza_verticale(id_stanza, stanze, colori, estremi):
	'''
	input: id della stanza da splittare
	output: lista delle stanze completa.
	divide la stanza in 2 e parti segueno una linea verticale messa al centro 
	'''
	stanza = stanze[id_stanza]
	colore = colori[id_stanza]
	
	new_index = len(stanze)
	vertici_stanza = stanze[id_stanza].bounds #e' la bounding box
	coord = stanza.exterior.coords #sono tutte le coordinate del poligono
	
	dsg.disegna_stanze(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3])#disegno prima. Da cancellare
	
	#divido a meta', qualunque sia la forma, non e' una buona strategia, ma magari e' utile.
	(xmin, ymin, xmax, ymax) = (vertici_stanza[0],vertici_stanza[1],vertici_stanza[2],vertici_stanza[3])
	new_x = ((xmax - xmin)/2 )+xmin #calcolo la nuova coordinata x
	
	#bounding box destra
	box_dx = Polygon([(xmin, ymin),(xmin, ymax),(new_x, ymax), (new_x, ymin)]) #punti messi in senso orario
	stanza1 = box_dx.intersection(stanza)
	#bounding box sinistra
	box_sx = Polygon([(new_x, ymin),(new_x, ymax), (xmax, ymax),(xmax, ymin)])
	stanza2 = box_sx.intersection(stanza)
		
	
	#del stanze[id_stanza]
	stanze[id_stanza] = stanza1
	stanze.append(stanza2)
	colori.append("#5F1978") #trovare un modo piu' intellignete di questo per assegnare un colore alla nuova stanza
	
	#disegno la stanza divisa, TODO: si puo' cancellare
	disegna_stanza(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3], id_stanza)
	disegna_stanza(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3], new_index)
	
	dsg.disegna_stanze(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3])#disegno prima. Da cancellare
	
	return stanze, colori

def split_stanza_orizzontale(id_stanza, stanze, colori, estremi):
	'''
	input: id della stanza da splittare
	output: lista delle stanze completa.
	divide la stanza in 2 e parti segueno una linea orizzontale messa al centro 
	'''
	stanza = stanze[id_stanza]
	colore = colori[id_stanza]
	
	new_index = len(stanze)
	vertici_stanza = stanze[id_stanza].bounds #e' la bounding box
	dsg.disegna_stanze(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3])#disegno prima
	
	#divido a meta', qualunque sia la forma, non e' una buona strategia, ma magari e' utile.
	(xmin, ymin, xmax, ymax) = (vertici_stanza[0],vertici_stanza[1],vertici_stanza[2],vertici_stanza[3])
	new_y = ((ymax-ymin)/2)+ymin #calcolo la nuova coordinata y
	
	#bounding box alto 
	box_alto = Polygon([(xmin,new_y),(xmin,ymax),(xmax,ymax),(xmax,new_y)])
	stanza1 = box_alto.intersection(stanza)
	#bounding box basso
	box_basso = Polygon([(xmin, ymin),(xmin, new_y),(xmax,new_y),(xmax, ymin)])
	stanza2 = box_basso.intersection(stanza)
	
	#del stanze[id_stanza]
	stanze[id_stanza] = stanza1
	stanze.append(stanza2)
	colori.append("#5F1978") #trovare un modo piu' intellignete di questo per assegnare un colore alla nuova stanza

	#disegno la stanza divisa, TODO: si puo' cancellare
	disegna_stanza(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3],  id_stanza)
	disegna_stanza(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3], new_index)
	
	dsg.disegna_stanze(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3])#disegno prima. Da cancellare
	return stanze, colori

#qui sto usando il concetto di Sazio creato come oggetto.
def slit_all_cell_in_room(spazi, id_spazio, colori, estremi):
	'''
	splitta nuovamente una stanza nelle celle originarie
	'''
	spazio = spazi[id_spazio]
	celle_di_spazio = spazio.cells
	new_index = len(spazi) #da dove parto ad inserire le celle successive alla prima di una stanza
	
	#del spazi[id_spazio]
	
	spazi[id_spazio] = celle_di_spazio[0]#nella vecchia posizione ci metto la prima cella della lista
	spazi = spazi + celle_di_spazio[1:]
	
	#aggiungo colori gia' usati da altre parti
	for c in range(0,len(celle_di_spazio)-2):
		colori.append(colori[c])
	
	#disegno per vedere se e' giusto, da cancellare	
	disegna_stanza(spazi, colori, estremi[0],estremi[2],estremi[1],estremi[3], id_spazio)
	disegna_stanza(spazi, colori, estremi[0],estremi[2],estremi[1],estremi[3], new_index)
	disegna_stanza(spazi, colori, estremi[0],estremi[2],estremi[1],estremi[3], new_index+1)
	disegna_stanza(spazi, colori, estremi[0],estremi[2],estremi[1],estremi[3], new_index+2)
	disegna_stanza(spazi, colori, estremi[0],estremi[2],estremi[1],estremi[3], new_index+3)
	disegna_stanza(spazi, colori, estremi[0],estremi[2],estremi[1],estremi[3], new_index+4)
	
	return spazi, colori

#siccome ho inserito all'interno di Spazio anche l'id ora non ho nemmeno piu' bisogno di passare come argomento l'inetera lista degli spazi e l'id dello spazio	
def split_some_cells(spazio):
	'''
	permette di splittare in spazi differenti solo alcune celle all'interno di una stanza. 
	pensare meglio a come farlo, quali sono le celle che voglio splittare?
	'''
	

#Reverce transitional kernels senza il concetto di Spazio
def split_stanza_reverce(id_stanza1, id_stanza2, stanze, colori, estremi):
	'''
	unisce due stanze
	'''	
	stanza1 = stanze[id_stanza1]
	stanza2 = stanze[id_stanza2]
	
	nuovo_spazio = stanza1.union(stanza2)
	del colori[len(colori)-1]	#elimino dalla lista dei colori un colore
	#inserisco la nuova stanza in posizione di una delle due stanze che ho voluto unire(id_Stanza1)	
	stanze[id_stanza1] = nuovo_spazio
	del stanze[id_stanza2]
	dsg.disegna_stanze(stanze, colori, estremi[0],estremi[2],estremi[1],estremi[3])#disegno prima. Da cancellare
	return stanze, colori


#metodo utile solo a capire se ho corretamente diviso le stanze
def disegna_stanza(stanze, colori, xmin, ymin, xmax, ymax, idStanza):
	'''
	disegna una stanza.
	'''
	fig = plt.figure()
	plt.title('11.stanza 0 ')
	ax = fig.add_subplot(111)
	
	for index,s in enumerate(stanze):
		if index == idStanza:
			f_patch = PolygonPatch(s,fc=colori[index],ec='BLACK')
			ax.add_patch(f_patch)
		ax.set_xlim(xmin,xmax)
		ax.set_ylim(ymin,ymax)
	plt.show()
	return (fig, ax)