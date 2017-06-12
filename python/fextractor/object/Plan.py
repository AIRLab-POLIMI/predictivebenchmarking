from object import Superficie as fc #prima si chiamava cella 
from object import Spazio as sp
from object import Segmento as sg
from util import layout as lay
from util import disegna as dsg
import copy
import cv2
import collections
from shapely.geometry import Point


class Plan(object):
	def __init__(self, spazi, contorno, cellette_esterne):
		self.spazi = spazi
		self.contorno = contorno
		self.cellette_esterne = cellette_esterne
	def set_extended_segments(self, extended_segments):
		self.extended_segments = extended_segments


#questo e' il primo metodo per unire le stanze oversegentate (sbaglia in parecchi casi)	
def unisci_stanze_oversegmentate(plan_o):
	'''
	se esistono due spazi diversi che sono collegati tramite un edge di una cella che ha un peso basso allora unisco quegli spazi
	'''	
	
	spazi = plan_o.spazi
	
	
	#per ogni spazio guardo se esiste un altro spazio che ha una cella che ha a sua volta un edge in comune con il primo spazio
	stanze_da_unire =[]
	 
	c =0
	for s1 in spazi:
		for s2 in spazi:
			for c1 in s1.cells:
				for c2 in s2.cells:
					if fc.adiacenti(c1.c,c2.c):
						if fc.edge_comune(c1.c, c2.c)[0].weight < 0.25 and s1!= s2 and s1.out == False and s2.out == False: # se hanno un peso basso
							#dovrei unire i due spazi							
							coppia = [s1,s2]
							if (coppia not in stanze_da_unire) and ([coppia[1], coppia[0]] not in stanze_da_unire):#mi interessa anche il senso contrario. Li voglio unire solo una volta
								stanze_da_unire.append(coppia)
								c+=1
	
	for ele in stanze_da_unire:
		print ele
	print "\n"
	
	#ora che ho le coppie di spazi devo unire tutte le coppie che hanno almeno un elemento in comune poiche' fanno parte della stessa stanza.
	l = stanze_da_unire
	out = []
	while len(l)>0:
		first, rest = l[0], l[1:]
		first = set(first)

		lf = -1
		while len(first)>lf:
			lf = len(first)

			rest2 = []
			for r in rest:
				if len(first.intersection(set(r)))>0:
					first |= set(r)
				else:
					rest2.append(r)     
			rest = rest2

		out.append(first)
		l = rest

	#lista di elementi comuni (appartenenti alla stessa stanza)
	elementi_comuni=[]
	for s in out:
		elementi_comuni.append(list(s))
	
	
	'''
	elementi_comuni=[]
	for index1,coppia1 in enumerate(stanze_da_unire):
		da_unire = [coppia1[0],coppia1[1]]
		for index2,coppia2 in enumerate(stanze_da_unire):
			if index2>index1:
				if coppia1 != coppia2:#aggiungo in cascata tutti quelli che dovrebbero essere uniti
					if coppia1[1] == coppia2[0]:
						da_unire.append(coppia2[1])					
					if len(elementi_comuni) >0:
						for e in elementi_comuni:
							if (coppia1[0] in e) and (coppia1[1] in e):
								da_unire = e
								#ricorda che potrebbe non essere necessariamente coppia2[1], devi selezionare quello diverso
								if coppia2[0] in e: 
									da_unire.append(coppia2[1])
								else:
									da_unire.append(coppia2[0])
								elementi_comuni.remove(e)# in teoria dovrebbe andare bene dato che ce ne dovrebbe essere solo uno di elemento da eliminare
					#da aggiungere anche gli altri controlli 
		elementi_comuni.append(da_unire)
	
	for ele in elementi_comuni:
		print ele
	'''
	for e in elementi_comuni:
		prima_coppia = [e[0],e[1]]
		count = 2
		spazio_risultante = sp.unisci_spazi(prima_coppia[0],prima_coppia[1])
		#elimino i vecchi spazi(che ormai ho unito )
		print "gli spazi sono: ", len(plan_o.spazi)
		elimina_spazio(prima_coppia[0], plan_o)
		elimina_spazio(prima_coppia[1], plan_o)
		print "gli spazi sono: ", len(plan_o.spazi)
		#aggiungo alla lista degli spazi di un Plan la stanza che ho appena creato
		aggiungi_spazio(spazio_risultante, plan_o) 
		print "gli spazi sono, ora che ho aggiunto: ", len(plan_o.spazi)
		while count<len(e) :
			seconda_coppia = [spazio_risultante, e[count]]
			count+=1
			spazio_risultante = sp.unisci_spazi(spazio_risultante,seconda_coppia[1]) 
			#elimino i vecchi spazi(che ormai ho unito )
			print "gli spazi sono: ", len(plan_o.spazi)
			elimina_spazio(seconda_coppia[0], plan_o)
			elimina_spazio(seconda_coppia[1], plan_o)
			print "gli spazi sono: ", len(plan_o.spazi)
			#aggiungo alla lista degli spazi di un Plan la stanza che ho appena creato
			aggiungi_spazio(spazio_risultante, plan_o) 
			print "gli spazi sono, ora che ho aggiunto: ", len(plan_o.spazi)
		
	
	print "il numero di cellette adiacenti con basso peso sono",c
	
	
	
def elimina_spazio(spazio, plan_o):
	'''
	permette di eliminare uno spazio dalla lista degli spazi di plan_o
	'''
	for s in plan_o.spazi:
		if s==spazio:
			plan_o.spazi.remove(spazio)
	

def aggiungi_spazio(spazio, plan_o):
	'''
	aggiungo alla lista degli spazi di un Plan un nuovo spazio
	'''
	plan_o.spazi.append(spazio)

#secondo metodo per aggregare stanze oversegmentate	
#rinominare la funzione unisciOversegmentazione()
def postprocessing(plan_o, parametri_obj):
	'''
	unisco stanze che dovrebbero essere unite, lo faccio epr coppia di spazi.
	1) trovo gli edge adiacenti tra spazi.
	2) e calcolo l'affinita' pesato su tutti gli edge in comune  
	'''
	
	spazi = plan_o.spazi
	
	
	#per ogni spazio guardo se esiste un altro spazio che ha una cella che ha a sua volta un edge in comune con il primo spazio
	stanze_da_unire =[]
	 
	c =0
	s2_temp = spazi[0]
	edge_in_comune = []
	for s1 in spazi:
		for s2 in spazi:
			edge_in_comune = []
			s2_temp = s2
			for c1 in s1.cells:
				for c2 in s2.cells:
					if fc.adiacenti(c1.c,c2.c):
						edge_com = fc.edge_comune(c1.c, c2.c)
						for ele in edge_com:
							edge_in_comune.append(ele)#colleziono tutti gli edge in comune 
		
			if len(edge_in_comune)>0 and Q_split(edge_in_comune) < parametri_obj.soglia_q_split and s1!= s2_temp and s1.out == False and s2_temp.out == False: # se hanno un peso basso					
			#if fc.edge_comune(c1.c, c2.c)[0].weight < 0.25 and s1!= s2 and s1.out == False and s2.out == False: # se hanno un peso basso
				#dovrei unire i due spazi							
				coppia = [s1,s2_temp]
				if (coppia not in stanze_da_unire) and ([coppia[1], coppia[0]] not in stanze_da_unire):#mi interessa anche il senso contrario. Li voglio unire solo una volta
					stanze_da_unire.append(coppia)
					c+=1
	
	for ele in stanze_da_unire:
		print ele
	print "\n"
	
	#ora che ho le coppie di spazi devo unire tutte le coppie che hanno almeno un elemento in comune poiche' fanno parte della stessa stanza.
	l = stanze_da_unire
	out = []
	while len(l)>0:
		first, rest = l[0], l[1:]
		first = set(first)

		lf = -1
		while len(first)>lf:
			lf = len(first)

			rest2 = []
			for r in rest:
				if len(first.intersection(set(r)))>0:
					first |= set(r)
				else:
					rest2.append(r)     
			rest = rest2

		out.append(first)
		l = rest

	#lista di elementi comuni (appartenenti alla stessa stanza)
	elementi_comuni=[]
	for s in out:
		elementi_comuni.append(list(s))
	
	
	#li stanpo solo per vedere se sono corretti
	for ele in elementi_comuni:
		print ele
	
	
	
	for e in elementi_comuni:
		prima_coppia = [e[0],e[1]]
		count = 2
		spazio_risultante = sp.unisci_spazi(prima_coppia[0],prima_coppia[1])
		#elimino i vecchi spazi(che ormai ho unito )
		print "gli spazi sono: ", len(plan_o.spazi)
		elimina_spazio(prima_coppia[0], plan_o)
		elimina_spazio(prima_coppia[1], plan_o)
		print "gli spazi sono: ", len(plan_o.spazi)
		#aggiungo alla lista degli spazi di un Plan la stanza che ho appena creato
		aggiungi_spazio(spazio_risultante, plan_o) 
		print "gli spazi sono, ora che ho aggiunto: ", len(plan_o.spazi)
		while count<len(e) :
			seconda_coppia = [spazio_risultante, e[count]]
			count+=1
			spazio_risultante = sp.unisci_spazi(spazio_risultante,seconda_coppia[1]) 
			#elimino i vecchi spazi(che ormai ho unito )
			print "gli spazi sono: ", len(plan_o.spazi)
			elimina_spazio(seconda_coppia[0], plan_o)
			elimina_spazio(seconda_coppia[1], plan_o)
			print "gli spazi sono: ", len(plan_o.spazi)
			#aggiungo alla lista degli spazi di un Plan la stanza che ho appena creato
			aggiungi_spazio(spazio_risultante, plan_o) 
			print "gli spazi sono, ora che ho aggiunto: ", len(plan_o.spazi)
		
	
	print "il numero di cellette adiacenti con basso peso sono",c
	
	
def Q_split(edge_in_comune):
	'''
	calcola il Q_split come definito nel paper di mura. rappresenta la qualita' dello splitting
	'''
	
	num = 0
	den = 0
	for e in edge_in_comune:
		num = num + (e.weight* sg.lunghezza(e.x1,e.y1,e.x2,e.y2))
		den = den + sg.lunghezza(e.x1,e.y1,e.x2,e.y2)
	
	q_split = num / den
	
	return q_split



#questo metodo trova solo gli spazi al confine con il convexHull
def spazi_al_confine(spazi, cellette_esterne):
	'''
	trova tutti gli spazi del confine e ne restituisce la lista
	'''
	spazi_confine_interno = []
	for s in spazi:
		for c in cellette_esterne:
			if s.spazio.touches(c.cella):
				spazi_confine_interno.append(s)
	
	spazi_confine_interno = list(set(spazi_confine_interno)) #elimino duplicati 
	
	return spazi_confine_interno
	

def trova_spazi_parziali_due(plan_o):
	'''
	secondo metodo per trovare le stanze parziali. faccio un confronto pesato 
	'''
	
	spazi_in = plan_o.spazi #oggetto di tipo spazio
	cellette_esterne = plan_o.cellette_esterne #oggetto di tipo poligono
	
	spazi_al_confine_interni = spazi_al_confine(spazi_in, cellette_esterne)
	
	#ora cerco per ogni spazio del confine la lista di edges che ha in comune con l'esterno
	
	for s in spazi_al_confine_interni:
		edge_in_comune = [] #edge di una stanza in comune con l'esterno
		for c1 in s.cells:	
			for c2 in cellette_esterne:
				if fc.adiacenti(c1.c,c2.c):
					edge_com = fc.edge_comune(c1.c, c2.c)
					for ele in edge_com:
						edge_in_comune.append(ele)#colleziono tutti gli edge in comune 
		if 	Q_split(edge_in_comune) < 0.6: #0.6 e' un parametro di cui si deve fare il tuning
			#significa che e' una stanza parziale
			for spazio in plan_o.spazi:
				if s == spazio:
					spazio.set_parziale(True)
					
def trova_spazi_parziali_da_frontiere(plan_o, lista_pixel_frontiere, immagine_cluster, labels):
	'''
	terzo metodo per riconoscere le stanze parziali, basato sul riconoscimento delle frontiere. Questo metodo controlla che all'interno dei pixel di una cella ci siano almeno il 30% di pixel dello stesso cluster per fare in modo che quella cella sia una cella parziale
	'''
	
	spazi = plan_o.spazi #oggetto di tipo spazio
	img_flipt= cv2.flip(immagine_cluster,0) #capire se va usato sempre
	#img_flipt = immagine_cluster.copy()
	counter=collections.Counter(labels)

	for spazio in spazi:
		for celletta in spazio.cells:
			
			bordo = celletta.cella.bounds #restituisce una tupla del tipo (minx, miny, maxx, maxy)
			
			immagine_cella = img_flipt[bordo[1]:bordo[3], bordo[0]:bordo[2]]	
			
			altezza = len(immagine_cella)
			larghezza = len(immagine_cella[0])
			total_count_pixel = 0
			pixel_diversi = 0
			
			cluster = None
			prima_volta = True
			c = []
			for i in xrange(0, altezza):
				for j in xrange( 0, larghezza):
					r = immagine_cella[i][j][0]
					g = immagine_cella[i][j][1]
					b = immagine_cella[i][j][2]
					total_count_pixel += 1
					if r!=g or r!=b or g!=b:#se ci sono componenti rgb diverse allora non sono in scala di grigio e quel pixel fa parte della frontiera
						pixel_diversi += 1
						#c.append(pixel.cluster)#added
						if prima_volta == True: #suppongo che una cella non abbia parti sconosciute su lati diversi (cioe' che il cluster della frontiera sia solo uno)
							for pixel in lista_pixel_frontiere:
								if pixel.rgb[0]==r and pixel.rgb[1]==g and pixel.rgb[2]==b:
									cluster = pixel.cluster
									#print "cluster", cluster
									prima_volta = False
			'''
			#--------aggiungo parte dove faccio media del cluster dominante #nel caso questa cosa va aggiunta anche dalle altre parti
			#TODO: questa funzione dovrebbe essere modificata come trova_spazi_gt_da_frontiere_versione_2 di metriche frontiere
			max = 0
			for elem in c:
				if c.count(elem) > max:
					max = c.count(elem)
					cluster = elem			
			#---------------------	
			'''		
						
			n_elementi_cluster = counter[cluster]
			#print "il numero di n_elementi_cluster", n_elementi_cluster
			#if pixel_diversi >= 0.3 * n_elementi_cluster and n_elementi_cluster > 0: #la copertura deve essere il 30% di quel cluster
			if pixel_diversi >= 15: #elimino un po' di rumore
				celletta.set_vedo_frontiera(True)
				celletta.set_celletta_out(False)
				celletta.set_celletta_parziale(True)	
				celletta.set_cluster_frontiera(cluster)
			else:
				celletta.set_vedo_frontiera(False)
				celletta.set_celletta_out(False)
				celletta.set_celletta_parziale(False)
				celletta.set_cluster_frontiera(None) #se la cella non ha una frontiera associata allora non esiste il cluster frontiera


#TODO: verificare che funzioni bene
def trova_spazi_parziali_da_frontiere_v2(plan_o, lista_pixel_frontiere, immagine_cluster, labels):

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
	
	for spazio in plan_o.spazi:
		for celletta in spazio.cells:

			num_pixel = 0
			cluster = None
			prima_volta = True
			c = []
			for pixel in lista_pixel_frontiere:
				posizione = Point(pixel.x,pixel.y)
				if posizione.distance(celletta.cella) == 0:
					#significa che quel pixel e' all'interno
					#print "ci entro????????? mai "
					num_pixel+=1
					c.append(pixel.cluster)#added
					#if prima_volta == True:
						#cluster = pixel.cluster
						#prima_volta = False
			#print "-------------------<<<<<<<<<<<<", num_pixel	
			
			#--------aggiungo parte dove faccio media del cluster dominante #nel caso questa cosa va aggiunta anche dalle altre parti
			max = 0
			for elem in c:
				if c.count(elem) > max:
					max = c.count(elem)
					cluster = elem			
			#---------------------		

			n_elementi_cluster = counter[cluster]
			#print "il numero di n_elementi_cluster", n_elementi_cluster
			#if pixel_diversi >= 0.3 * n_elementi_cluster and n_elementi_cluster > 0: #la copertura deve essere il 30% di quel cluster
			if num_pixel >= 15: #elimino un po' di rumore
				celletta.set_vedo_frontiera(True)
				celletta.set_celletta_out(False)
				celletta.set_celletta_parziale(True)	
				celletta.set_cluster_frontiera(cluster)
			else:
				celletta.set_vedo_frontiera(False)
				celletta.set_celletta_out(False)
				celletta.set_celletta_parziale(False)
				celletta.set_cluster_frontiera(None) #se la cella non ha una frontiera associata allora non esiste il cluster frontiera

	del lista_pixel_frontiere
	#rifaccio tornare la lista come prima
	lista_pixel_frontiere = []
	for p in lista_pixel:
		lista_pixel_frontiere.append(p) 




def assegna_a_spazio_cluster_frontiera(spazio, lista_pixel_frontiere, immagine_cluster, labels):
	'''
	assegno ad un solo spazio il suo cluster frontiera, quando uso questa funzione 
	'''
	img_flipt= cv2.flip(immagine_cluster,0) #capire se va usato sempre
	#img_flipt = immagine_cluster.copy()
	counter=collections.Counter(labels)
	
	for celletta in spazio.cells:
		bordo = celletta.cella.bounds #restituisce una tupla del tipo (minx, miny, maxx, maxy)
		
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
								#print "cluster", cluster
								prima_volta = False
					
					
		n_elementi_cluster = counter[cluster]
		#print "il numero di n_elementi_cluster", n_elementi_cluster
		#if pixel_diversi >= 0.3 * n_elementi_cluster and n_elementi_cluster > 0: #la copertura deve essere il 30% di quel cluster
		if pixel_diversi >= 15: #elimino un po' di rumore
			celletta.set_vedo_frontiera(True)
			celletta.set_celletta_out(False)
			celletta.set_celletta_parziale(True)	
			celletta.set_cluster_frontiera(cluster)
		else:
			celletta.set_vedo_frontiera(False)
			celletta.set_celletta_out(False)
			celletta.set_celletta_parziale(False)
			celletta.set_cluster_frontiera(None) #se la cella non ha una frontiera associata allora non esiste il cluster frontiera
	
	spazio.set_cluster_frontiera(cluster)#assegno allo spazio il cluster della frontiera che possiede all'interno.

				
def trova_celle_toccate_dal_laser_beam(lista_celle, immagine_cluster):
	'''
	dato in input una lista di celle e le frontiere, fornisce le celle della lista toccate dal beam del laser
	'''	
	
	img_flipt= cv2.flip(immagine_cluster,0) #capire se va usato sempre
	#img_flipt = immagine_cluster.copy()

	for celletta in lista_celle:
	
		bordo = celletta.cella.bounds #restituisce una tupla del tipo (minx, miny, maxx, maxy)
	
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
				
				
		#print "il numero di n_elementi_cluster", n_elementi_cluster
		if pixel_diversi >10 : #se nell'immagine ci sono almeno 20 pixel della frontiera altrimenti e' solo rumore
			celletta.set_vedo_frontiera(True)
			#celletta.set_celletta_out(False)
			celletta.set_celletta_parziale(True)	
		else:
			celletta.set_vedo_frontiera(False)
			#celletta.set_celletta_out(False) #sono gia' settati
			#celletta.set_celletta_parziale(False)
	
	return lista_celle
	
def estrai_extended_segments_del_bordo(extended_segments):
	'''
	estraggo le extended segments del bordo dell'immagine
	'''			
	
	bordi = []
	for e in extended_segments:
		if e.cluster_spaziale == "bordo1" or e.cluster_spaziale == "bordo2" or e.cluster_spaziale == "bordo3" or e.cluster_spaziale == "bordo4":
			bordi.append(e)
	
	return bordi

def estrai_celle_sul_bordo(plan_o):
	'''
	estrae le celle che toccano il bordo dell'immagine,
	'''
	
	adiacenti_al_bordo=[]

	for cella in plan_o.cellette_esterne:
		edges = cella.c.bordi
		trovato = False
		for b in edges:
			if b.cluster_spaziale == "bordo1" or b.cluster_spaziale == "bordo2" or b.cluster_spaziale == "bordo3" or b.cluster_spaziale == "bordo4":
				#tocca il bordo
				trovato = True
		if trovato == True:
			adiacenti_al_bordo.append(cella) 
		
	return list(set(adiacenti_al_bordo))
		
		
def estrai_celle_di_altre_stanze(stanza,plan_o):
	'''
	permette di estrarre tutte le celle di altre stanze diverse dalla "stanza" passata come paramentro alla funzione 
	'''		
	celle_di_altre_stanze = []
	for s2 in plan_o.spazi:
		if s2 !=stanza:
			for c in s2.cells:
				celle_di_altre_stanze.append(c)
				
	return celle_di_altre_stanze
	
	
	
def separaUndersegmentazione(plan_o, critical_points, parametri_obj, path_obj, xmin, ymin, xmax, ymax):
	'''
	permette di separare le stanze undersegmentate.
	in primis una stanza e' stata undersegmentata se esistono almeno 2 celle che la compongono che si toccano ed il peso di quella cella e' superiore a 0.3.
	'''
	
	print "il numero di critical points e '", len(critical_points)
	stanze = plan_o.spazi
	conta=0
	
	#in sostanza vado a chiudere le porte
	for stanza in stanze:
		#queste due liste mi servono per ricordarmi il vecchio valore dell'edge per poi risettarlo
		vecchio_valore_edge=[] #lista dei velori numerici dei singoli edge 
		edge_modificato=[]#oggetto di tipo edge
		
		cellette_stanza = stanza.cells
		trovato =False #controllo per vedere se la stanza e' stata undersegmentata
		for c1 in cellette_stanza:
			for c2 in cellette_stanza:
				if fc.adiacenti(c1.c,c2.c) and c1!=c2:
					if(fc.edge_comune(c1.c,c2.c)[0].weight >= 0.3):#il bordo in comune non deve essere supportato da segmenti(se questo avviene in una stanza significa che e' stata eliminata una parete che in teoria era stata gia' vista)
						trovato = True
										
		if trovato == True:
			#in questo punto va lo splitting della stanza
			#1) trovo l'edge su cui si trova il critical point
			#2) setto un peso alto su quell'edge e ricompunto DBSCAN
			
			
			porte_colleganti = []
			celle_collegate = []
			for index, p in enumerate(critical_points):
				coppia = []
				for celletta in cellette_stanza:
					if (celletta.cella.boundary).distance(Point(p[0],p[1])) < 0.2: # se il contorno della cella dista meno di 0,2 dal critical points(nel caso non basti aumentare questo parametro )
						porte_colleganti.append(Point(p[0],p[1]))
						if celletta not in coppia:
							coppia.append(celletta)
				if len(coppia)==2:
					if fc.adiacenti(coppia[0].c,coppia[1].c) and coppia[0]!=coppia[1]:
						print "ho trovato le 2 celle che si toccano per questo pixel ", index
						edge_comune = fc.edge_comune(coppia[0].c,coppia[1].c)[0]
						#assegno un peso alto a quell'edge (e come se ci fosse la porta chiusa)
						for edge1 in coppia[0].c.bordi:
							if edge1==edge_comune:
								print "la lunghezza del segmento e' :", sg.lunghezza(edge1.x1,edge1.y1, edge1.x2, edge1.y2)
								edge_modificato.append(edge1)#mi salvo il vecchio valore dell'edge
								vecchio_valore_edge.append(edge1.weight)							
								edge1.set_weight(1)
						for edge2 in coppia[1].c.bordi:
							if edge2==edge_comune:
								edge2.set_weight(1)
				
			
			#ora che ho chiuso le porte posso ricomputare DBSCAN
	
			#TODO: controllare questa parte da qui in giu', che non vengono settate bene le cose(frontiere etc)
			
			
			#in questo punto adesso per ogni stanza che ne ha bisogno ricomputo DBSCAN come all'inizio
			#metti qui tutto il DBSCAN
			#------------------CREO LE MATRICI L, D, D^-1, ED M = D^-1 * L------------------------
			#ci si riferisce alla stanza corrente presa in consierazione
			celle = []
			celle_poligoni = []
			for celletta in stanza.cells:
				celle.append(celletta.c)
				celle_poligoni.append(celletta.cella)
			(matrice_l, matrice_d, matrice_d_inv, X) = lay.crea_matrici(celle, sigma = parametri_obj.sigma)
			#-------------------------------------------------------------------------------------
			#----------------DBSCAN PER TROVARE CELLE NELLA STESSA STANZA-------------------------
			clustersCelle = lay.DB_scan(parametri_obj.eps, parametri_obj.minPts, X, celle_poligoni)
			print "la lunghezza di clustersCelle e' ", len(clustersCelle)
			colori = dsg.get_colors(clustersCelle)
			stanze, spazi_nuovi = lay.crea_spazio(clustersCelle, celle, celle_poligoni, colori, xmin, ymin, xmax, ymax, filepath = path_obj.filepath) 
			
			
			#elimino la vecchia stanza da plan_o ed inserisco quelle nuove
			print "il numero di stanze appena create e' ", len(spazi_nuovi)
			#TODO: controllare che le stanze appena create siano correntte(intendo le celle parziali etc)
			elimina_spazio(stanza, plan_o)
			for spaz in spazi_nuovi:
				aggiungi_spazio(spaz,plan_o)
			
			
			#-----finito DBScan rimetto a posto i valori degli edge(riapro le porte)-----------------
			
			for index, e in enumerate(edge_modificato):
				for celletta in cellette_stanza:
					edge_celletta = celletta.c.bordi
					for eb in edge_celletta:
						if e == eb:
							e.set_weight(vecchio_valore_edge[index])
			
			
	
	