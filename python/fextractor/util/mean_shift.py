from __future__ import division
from object import Segmento as sg
import math
import warnings
warnings.warn('SISTEMARE LE RETTE DIAGONALI A RIGA 110')

def mean_shift(h,minOffset,walls):
	'''
	calcola i center_clusters tramite mean_shift. Vengono clusterizzate le inclinazioni in radianti dei muri
	'''
	#per ogni muro setto l'inclinazione
	for muro in walls:
		d = sg.inclinazione_radianti(muro.x1, muro.y1, muro.x2, muro.y2)
		if (d < -1.3):
			d += math.pi
		#if -0.15+math.pi < d > 0.15+math.pi :
		#	d -= math.pi

		muro.set_direction(d)

	#disegna(walls)

	#creo lista delle inclinazioni degli edges
	directions = []
	for muro in walls:
		directions.append(muro.direction)

	#inizialmente i cluster centers sono tutte le inclinazioni
	cluster_centers = directions[:]
	new_cluster_centers = calcola_new_cluster_centers(h,cluster_centers,directions)
	max_diff = massima_differenza(cluster_centers,new_cluster_centers)
	cluster_centers = new_cluster_centers[:]
	del new_cluster_centers[:]
	while(max_diff > minOffset):
		new_cluster_centers = calcola_new_cluster_centers(h,cluster_centers,directions)
		max_diff = massima_differenza(cluster_centers,new_cluster_centers)
		cluster_centers = new_cluster_centers[:]
		del new_cluster_centers[:]
	return cluster_centers


def calcola_new_cluster_centers(h,cluster_centers,directions):
	'''
	calcola i nuovi cluster_centers partendo da quelli del passo precedente
	'''
	new_cluster_centers = []	
	for alfa in cluster_centers:
		numeratore = 0
		#calcolo numeratore
		for teta in directions:
			kernel = 0
			condizione = (1-(math.cos(alfa-teta)))/h
			if(condizione <= 1):
				kernel = math.pow(1-condizione,2)
			tmp = kernel * teta
			numeratore += tmp
		denominatore = 0
		#calcolo il denominatore
		for teta in directions:
			kernel = 0
			condizione = (1-(math.cos(alfa-teta)))/h
			if(condizione <= 1):
				kernel = math.pow(1-condizione,2)
			denominatore += kernel
		#dopo aver calcolato numeratore e denominatore aggiungo il nuovo cluster_center alla lista new_cluster_centers
		new_cluster_centers.append(numeratore/denominatore)
	return new_cluster_centers


def massima_differenza(cluster_centers,new_cluster_centers):
	'''
	calcola massima differenza tra vecchi e nuovi cluster centers, in modo da determinare se puo' considerarsi terminato il clustering
	'''
	max_diff = 0
	for index,old in enumerate(cluster_centers):
		new = new_cluster_centers[index]
		if (abs(new-old) > max_diff):
			max_diff = abs(new-old)
	return max_diff


def indici_da_eliminare(num_min, lunghezza_min, cluster_centers, lista_muri, diagonali=True):
	# Se DIAGONALI = TRUE ELIMINA LE RETTE DIAGONALI
	'''
	trova gli indici di posizione dei cluster angolari causati da un numero di muri < num_min, e con ognuno di questi muri con
	lunghezza < lunghezza_min. Questi cluster angolari sono quindi causati da muri che possono essere considerati rumore, quindi elimino
	i cluster angolari e i rispetivi muri (indice cluster angolare in cluster_centers = indice muro in lista_muri)
	'''  
	indexes = []
	for c in set(cluster_centers):
		if (cluster_centers.count(c) <= num_min): #se il cluster angolare compare meno di tot volte nella lista cluster_centers 
			lunghezze = []
			candidati = []
			for index, c1 in enumerate(cluster_centers): 
				if c == c1: #per ogni cluster uguale al cluster in questione (con meno di tot occorrenze)
					candidati.append(index)
					#prendo il rispettivo muro (index cluster_centers = index lista_muri)
					m = lista_muri[index]
					lunghezze.append(sg.lunghezza(m.x1,m.y1,m.x2,m.y2)) 
					
			if tutti_corti(lunghezze,lunghezza_min): #se tutte le lunghezze sono <= lunghezza_min
				for i in candidati:
					indexes.append(i)
			
			del candidati [:]
			del lunghezze [:]
	if diagonali :
		diag = indici_diagonali(cluster_centers)
		indexes = indexes + diag
	return set(indexes)


def indici_diagonali(cluster_centers):
	'''
	trova gli indici di posizione dei cluster angolari diagonali
	'''  
	indexes = []
	for c in set(cluster_centers):
		if not (-0.15 < c < 0.15) and not (1.45 < c < 1.7) and not (-1.7 < c < -1.45):
			for index, c1 in enumerate(cluster_centers): 
				if c == c1: #per ogni cluster uguale al cluster in questione (con meno di tot occorrenze)
					indexes.append(index)
	return indexes


def tutti_corti(lunghezze,lunghezza_min):
	'''
	ritorna True se tutte le lunghezze sono < lunghezza_min
	'''
	for l in lunghezze:
		if l > lunghezza_min:
			return False
	return True


def unisci_cluster_simili(cluster_centers):
	'''
	Puo' accadere che alcuni cluster_angolari siano diversi per una quantita' infinitesima. Faccio una media e li setto = a questa media.
	'''
	for c1 in set(cluster_centers):
		for c2 in set(cluster_centers):
			if (c1 != c2) and (abs(c1-c2) <= 0.01):
				nuovo_cluster = (c1+c2)/2
				#print("unisco"+str(c1)+" e "+str(c2)+" in "+str(nuovo_cluster))
				for index,c3 in enumerate(cluster_centers):
					if(c3 == c1) or (c3==c2):
						cluster_centers[index] = nuovo_cluster
				return True
	return False


#codice per trovare parametri meanshift
'''				
vettore1 = np.arange(0.001, 1, 0.0001)
vettore2 = np.arange(0.00001, 0.00002, 0.00001)
for h in vettore1:
	for offset_minimo in vettore2:
		#inizialmente i cluster centers sono tutte le inclinazioni
		cluster_centers = directions[:]
		new_cluster_centers = []
		calcola_new_cluster_centers(h)
		#raw_input("Press enter to exit")
		max_diff = massima_differenza()
		cluster_centers = new_cluster_centers[:]
		del new_cluster_centers[:]
		while(max_diff > offset_minimo):
			calcola_new_cluster_centers(h)
			max_diff = massima_differenza()
			cluster_centers = new_cluster_centers[:]
			del new_cluster_centers[:]
		print(set(cluster_centers))
		print(len(set(cluster_centers)))
		print h
		print offset_minimo
		if(len(set(cluster_centers)) <= 20):
			print(set(cluster_centers))
			print(len(set(cluster_centers)))
			print h
			print offset_minimo
			#raw_input("Trovato")

raw_input("Press enter to exit")
'''
