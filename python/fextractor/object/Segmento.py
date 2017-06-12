from __future__ import division
import numpy as np
import math
from matplotlib import pyplot as plt
import matplotlib.cm as cmx

class Segmento(object):
	def __init__(self,x1,y1,x2,y2):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
		self.num_facce = 0
		self.cluster_spaziale = None
		self.cluster_muro = None
		self.cluster_angolare = None
	def set_cluster_index(self,i):
		self.cluster_index = i
	def set_weight(self,w):
		self.weight = w
	def set_direction(self,d):
		self.direction = d
	def set_cluster_angolare(self,c):
		self.cluster_angolare = c
	def set_cluster_spaziale(self,c):
		self.cluster_spaziale = c
	def set_branch(self,b):
		self.branch = b
	def set_cluster_muro(self, cluster):
		self.cluster_muro = cluster


def disegna_pesanti(edges, peso_min):
	ascisse = []
	ordinate = []
	for e in edges:
		ascisse.append(e.x1)
		ascisse.append(e.x2)
		ordinate.append(e.y1)
		ordinate.append(e.y2)
		if e.weight >= peso_min:
			plt.plot(ascisse,ordinate,color='k',linewidth=4)
		else:
			plt.plot(ascisse,ordinate,color='k',linewidth=1)
		del ascisse[:]
		del ordinate[:]
	plt.show()

def lunghezza(x1,y1,x2,y2):
	'''
	calcola e restituisce la distanza tra punto 1 e punto 2
	'''
	dist = np.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
	return dist


def point_segment_distance(px, py, x1, y1, x2, y2):
	'''
	calcola la distanza tra il punto px,py e il segmento individuato dagli estremi x1,y1 e x2,y2
	'''
	dx = x2 - x1
	dy = y2 - y1
	if dx == dy == 0:  # the segment's just a point
		return math.hypot(px - x1, py - y1)

	# Calculate the t that minimizes the distance.
	t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)

	# See if this represents one of the segment's
	# end points or a point in the middle.
	if t < 0:
		dx = px - x1
		dy = py - y1
	elif t > 1:
		dx = px - x2
		dy = py - y2
	else:
		near_x = x1 + t * dx
		near_y = y1 + t * dy
		dx = px - near_x
		dy = py - near_y

	return math.hypot(dx, dy)


def intersez_rette(m1,q1,m2,q2): 
	'''
	dati i coeff delle x e delle y delle 2 eq in forma (m1x+y=q1) e (m2x+y=q2) trova x e y di intersezione
	'''
	coeff = np.array([[m1,1], [m2,1]])
	term_noti = np.array([q1,q2])
	x = np.linalg.solve(coeff, term_noti)
	return x


def elimina_corti(n,lista):
	'''
	elimina i muri piu' corti di n
	'''
	indici_da_eliminare = []
	for index,s in enumerate(lista):		
		if lunghezza(s.x1,s.y1,s.x2,s.y2) <= n :
			indici_da_eliminare.append(index)
	for i in sorted(indici_da_eliminare, reverse=True):
		del lista[i]	


def segments_intersect(x11, y11, x12, y12, x21, y21, x22, y22):
	"""
	restituisce true se i segmenti si intersecano, false altrimenti
	whether two segments in the plane intersect:
	one segment is (x11, y11) to (x12, y12)
	the other is   (x21, y21) to (x22, y22)
	"""
	dx1 = x12 - x11
	dy1 = y12 - y11
	dx2 = x22 - x21
	dy2 = y22 - y21
	delta = dx2 * dy1 - dy2 * dx1
	if delta == 0: return False  # parallel segments
	s = (dx1 * (y21 - y11) + dy1 * (x11 - x21)) / delta
	t = (dx2 * (y11 - y21) + dy2 * (x21 - x11)) / (-delta)
	return (0 <= s <= 1) and (0 <= t <= 1)


def segments_distance(x11, y11, x12, y12, x21, y21, x22, y22):
	""" calcola distanza tra 2 segmenti, se si intersecano return 0, altrimenti la calcola e la restituisce
	    distance between two segments in the plane:
	    one segment is (x11, y11) to (x12, y12)
	    the other is   (x21, y21) to (x22, y22)
	"""
	if segments_intersect(x11, y11, x12, y12, x21, y21, x22, y22):
		return 0
	# try each of the 4 vertices w/the other segment
	# in pratica la distanza tra 2 segmenti e' il minimo tra la distanza tra 1 estremo e 2 segmento, 2 estremo e 2 segmento,
	# 3 estremo e 1 segmento, 4 estremo e 1 segmento
	distances = []
	distances.append(point_segment_distance(x11, y11, x21, y21, x22, y22))
	distances.append(point_segment_distance(x12, y12, x21, y21, x22, y22))
	distances.append(point_segment_distance(x21, y21, x11, y11, x12, y12))
	distances.append(point_segment_distance(x22, y22, x11, y11, x12, y12))
	return min(distances)



def inclinazione_radianti(x1,y1,x2,y2):
	'''
	calcola l'inclinazione in radianti del segmento con estremi x1,y1 e x2,y2
	'''
	if(x1!=x2): #evito la divisione per 0	
		m = (y2-y1)/(x2-x1)
		angolo = math.atan(m) #il coeff ang m e' la tg dell'angolo, in radianti
	else: #se le x sono uguali la linea e' verticale e quindi l'inclinazione e' 90 gradi
		angolo = math.radians(90.0)
	return angolo 


def assegna_cluster_angolare(lista_muri, cluster_centers):
	'''
	assegna cluster angolare ad ogni muro di lista_muri
	'''
	for index,muro in enumerate(lista_muri):
		cluster = cluster_centers[index]
		muro.set_cluster_angolare(cluster)
	return lista_muri


def spatialClustering(soglia, lista_muri):
	'''
	assegna cluster spaziale ad ogni muro di lista_muri. 2 muri hanno stesso cluster spaziale se hanno stesso cluster angolare
	e se hanno distanza laterale minore di soglia. Cluster spaziale = indice di posizione del primo muro in lista_muri che appartiene a quel cluster spaziale. E questo primo muro avra' quindi come cluster spaziale il proprio indice di posizione.
	'''
	for index,muro1 in enumerate(lista_muri):
		if (muro1.cluster_spaziale == None): #se non e' gia stato settato
			for muro2 in lista_muri[index+1:]: #controllo solo i successivi perche quelli prima sono di sicuro gia settati
				#se non e' stato ancora settato e se hanno stesso cluster angolare
				if(muro2.cluster_spaziale == None) and (muro1.cluster_angolare == muro2.cluster_angolare):
					if(lateral_separation(muro1,muro2) < soglia):
						muro2.set_cluster_spaziale(index)
			#dopo aver passato in rassegna tutti i successivi, setto quello che ho preso nel primo for.
			#NB: viene settato anche se non ho trovato nessun altro vicino. Sara' un cluster con un solo muro.
			muro1.set_cluster_spaziale(index)
	
		else: 
			#gia' stato settato, ma devo controllare lo stesso i successivi perche' possono essercene alcuni che dovrebbero
			#appartenere allo stesso cluster_spaziali ma avevano distanza laterale troppo grande. 
			for muro2 in lista_muri:
				#se non e' stato ancora settato e se hanno stesso cluster angolare
				if(muro2.cluster_spaziale == None) and (muro1.cluster_angolare == muro2.cluster_angolare):
					if(lateral_separation(muro1,muro2) < soglia):
						muro2.set_cluster_spaziale(muro1.cluster_spaziale)
						#questa volta non setto cluster = index perche' muro1 non e' il primo del cluster
				else:
					if(muro2.cluster_spaziale != None) and (muro2.cluster_spaziale != muro1.cluster_spaziale) and (muro1.cluster_angolare == muro2.cluster_angolare) and(lateral_separation(muro1,muro2) < soglia):
						for m in lista_muri:
							if m.cluster_spaziale == muro2.cluster_spaziale:
								m.set_cluster_spaziale(muro1.cluster_spaziale)

	return lista_muri


def lateral_separation(muro1,muro2):
	'''
	calcola lateral separation tra muro1 e muro2
	'''
	x1 = muro1.x1
	y1 = muro1.y1
	x2 = muro1.x2
	y2 = muro1.y2
	x3 = muro2.x1
	y3 = muro2.y1
	x4 = muro2.x2
	y4 = muro2.y2
	mid1_x = (x1+x2)/2
	mid1_y = (y1+y2)/2
	mid2_x = (x3+x4)/2
	mid2_y = (y3+y4)/2
	d = muro1.cluster_angolare # uguale a muro2.cluster_angolare
	m = math.tan(d)
	if(m!=0): #se il cluster_angolare non e' 0, quindi retta non orizzontale
		m_perp = -1/m
		q1 = mid1_y - (m_perp * mid1_x)
		q2 = mid2_y - (m * mid2_x)
		#devo calcolare la distanza tra le proiezioni di mid1 e mid2 sulla retta perp al loro cluster angolare. Questa retta la faccio
		#passare per mid1 cosi' devo proiettare solo mid2. Lo proietto trovando l'intersezione tra la retta perp passante per mid1 e la
		#retta con inclinazione = tan(direction) passante per mid2.
		mid2_proiettato = intersez_rette(-m_perp,q1,-m,q2)
		mid2_proiettato_x = mid2_proiettato[0]
		mid2_proiettato_y = mid2_proiettato[1]
		return lunghezza(mid1_x,mid1_y,mid2_proiettato_x,mid2_proiettato_y)
	else: #retta orizzontale
		#il mid2 proiettato avra' x = mid2_x e y = mid1_y
		return lunghezza(mid1_x,mid1_y,mid1_x,mid2_y)

def get_punti_proiettati(muro1,muro2):
	'''
	dati due muri, ottengo la retta perpendicolare passante per il centro del primo muro. 
	ottengo poi la retta passante per il centro del secondo muro avente come coefficiente angolare lo stesso del primo muro.
	ottenute le due rette ottengo il punto di intersezione e restituisco le coordinate del punto medio del secondo muro proiettato
	sulla retta ortogonale al primo muro.
	(cioe' la proiezione del punto medio del secondo muro sulla retta ortogonale e passante per il centro del primo muro).	
	'''
	x1 = muro1.x1
	y1 = muro1.y1
	x2 = muro1.x2
	y2 = muro1.y2
	x3 = muro2.x1
	y3 = muro2.y1
	x4 = muro2.x2
	y4 = muro2.y2
	mid1_x = (x1+x2)/2
	mid1_y = (y1+y2)/2
	mid2_x = (x3+x4)/2
	mid2_y = (y3+y4)/2
	d = muro1.cluster_angolare # uguale a muro2.cluster_angolare
	m = math.tan(d)
	if(m!=0): #se il cluster_angolare non e' 0, quindi retta non orizzontale
		m_perp = -1/m
		q1 = mid1_y - (m_perp * mid1_x)
		q2 = mid2_y - (m * mid2_x)
		#devo calcolare la distanza tra le proiezioni di mid1 e mid2 sulla retta perp al loro cluster angolare. Questa retta la faccio
		#passare per mid1 cosi' devo proiettare solo mid2. Lo proietto trovando l'intersezione tra la retta perp passante per mid1 e la
		#retta con inclinazione = tan(direction) passante per mid2.
		mid2_proiettato = intersez_rette(-m_perp,q1,-m,q2)
		mid2_proiettato_x = mid2_proiettato[0]
		mid2_proiettato_y = mid2_proiettato[1]
		
		#return mid1_x + mid1_y - mid2_proiettato_x - mid2_proiettato_y
		return (mid2_proiettato_x, mid2_proiettato_y)
	else: #retta orizzontale
		#il mid2 proiettato avra' x = mid2_x e y = mid1_y
		#return mid1_x+mid1_y-mid2_x-mid2_y
		#return -(mid1_x+mid1_y-mid2_x-mid2_y)
		return (mid2_x, mid1_y)

#TODO: lo uso, ma secondo me non va qui(tieni conto che nel tuo progetto un muro e' collegato a retta ed a parete, vedi UML. secondo il tuo progetto, questo metodo non e' un metodo di segmento, ma di muro)
def trova_estremi(lista_muri):
	'''
	trova xmin ymin xmax ymax dei muri di lista_muri. Costituiscono la bounding box.
	'''
	ascisse = []
	ordinate = []
	for muro in lista_muri: #prendo le minime e massime dei muri
		ascisse.append(float(muro.x1))
		ascisse.append(float(muro.x2))
		ordinate.append(float(muro.y1))
		ordinate.append(float(muro.y2))
	xmin = min(ascisse)
	xmax = max(ascisse)
	ymin = min(ordinate)
	ymax = max(ordinate)
	del ascisse[:]
	del ordinate[:]
	return np.array([xmin,xmax,ymin,ymax])


def crea_edges(extended_segments):
	'''
	creo gli edges tramite intersezioni tra extended_segments
	'''
	edges = []
	punti = []
	#per ogni segmento esteso vado a vedere quali punti ha come intersezione con altri estesi 
	for index,muro in enumerate(extended_segments): 
		x1 = muro.x1
		y1 = muro.y1
		x2 = muro.x2
		y2 = muro.y2
		for altro_muro in extended_segments:
			x3 = altro_muro.x1
			y3 = altro_muro.y1
			x4 = altro_muro.x2
			y4 = altro_muro.y2
			if(muro!=altro_muro)and(segments_intersect(x1,y1,x2,y2,x3,y3,x4,y4)): #se gli estesi sono diversi e se si intersecano
				punto = intersezione(x1,y1,x2,y2,x3,y3,x4,y4)
				punti.append(punto) #il punto di intersezione lo aggiungo alla lista punti
		#aggiungo anche gli estremi del muro esteso in questione
		#punti.append([x1,y1])
		#punti.append([x2,y2])
		punti.sort(key=lambda x: (x[0], x[1])) #li metto in ordine
		for i,punto in enumerate(punti):
			if(i<len(punti)-1): #creo gli edges. Len-1 per evitare out of bound.
				next = punti[i+1]
				if not ((punto[0]==next[0])and(punto[1]==next[1])): #evito i doppioni
					edge = Segmento(punto[0],punto[1],next[0],next[1])
					edge.set_cluster_angolare(muro.cluster_angolare)
					edge.set_cluster_spaziale(muro.cluster_spaziale) #ad ogni edge setto cluster = cluster del seg esteso
					edges.append(edge)
		del punti[:]
	return edges


def intersezione(x1,y1,x2,y2,x3,y3,x4,y4):
	'''
	dati gli estremi di 2 segmenti restituisce il punto di intersezione 
	'''
	if(x1!=x2)and(x3!=x4):
		m1 = (y2-y1)/(x2-x1)
		m2 = (y4-y3)/(x4-x3)
		q1 = y1 - (m1*x1)
		q2 = y3 - (m2*x3)
		punto = intersez_rette(-m1,q1,-m2,q2)
		return punto
	if(x1==x2):
		m2 = (y4-y3)/(x4-x3)
		q2 = y3 - (m2*x3)
		y = m2*x1 + q2
		punto = np.array([x1,y])
		return punto
	if(x3==x4):
		m1 = (y2-y1)/(x2-x1)
		q1 = y1 - (m1*x1)
		y = m1*x3 + q1
		punto = np.array([x3,y])
		return punto


def setPeso(edges, lista_muri):
	'''
	assegna peso ad ogni edge. Per ogni edge prendo i muri di lista_muri con stesso cluster_spaziale e li proietto sull'extended_segment 		con quel cluster_spaziale. Prima di tutti elimino le proiezioni incluse completamente in altre proiezioni, poi unisco le proiezioni 		che si sovrappongono parzialmente, infine calcolo la parte di edge coperta dalle proiezioni.
	'''
	tmp = []
	proiezioni = []

	for edge in edges:
	
		cluster_spaziale = edge.cluster_spaziale
	
		for muro in lista_muri:
			if(muro.cluster_spaziale == cluster_spaziale): #se muro ha stesso cluster dell'edge, devo aggiungerne la proiezione
			
				punto1 = proietta_punto(muro.x1,muro.y1,edge.x1,edge.y1,edge.x2,edge.y2)
				punto2 = proietta_punto(muro.x2,muro.y2,edge.x1,edge.y1,edge.x2,edge.y2)
				tmp.append(punto1) #aggiungo i punti alla lista tmp, che poi ordino in modo da avere start < end
				tmp.append(punto2)
				tmp.sort(key=lambda x: (x[0], x[1]))
				#li metto in ordine, in modo che il punto di inizio del segmento proiettato abbia x minore del punto di fine. 
				tmp2 = [tmp[0][0],tmp[0][1],tmp[1][0],tmp[1][1]]

				if not gia_dentro_seg(tmp2,proiezioni): #aggiungo la proiezione x1,y1,x2,y2 solo se non e' gia' dentro (evito doppi che mi creano problemi quando vado a eliminare le proiezioni incluse in altre)
					proiezioni.append(tmp2)
			
				del tmp[:]
		proiezioni[:] = [tup for tup in proiezioni if not compreso(tup,proiezioni)] #tolgo le proiezioni incluse in altre
		uniti = unisci_sovrapposti(proiezioni) #faccio merge di proiezioni che si intersecano
		while(uniti == 1):
			uniti = unisci_sovrapposti(proiezioni)

		#adesso devo calcolare cov per l'edge in questione
		cov = calcola_cov(edge,proiezioni)	
		weight = cov / lunghezza(edge.x1,edge.y1,edge.x2,edge.y2)
		edge.set_weight(weight)
		del proiezioni[:]
	
	return edges


def proietta_punto(x1,y1,x2,y2,x3,y3):
	'''
	dato il segmento con estremi x2,y2 e x3,y3 , proietto il punto p1 sul segmento
	'''	
	if (x2 == x3): #se segmento verticale
		punto = np.array([x2,y1])
		return punto
	if (y2 == y3): #se segmento orizzontale
		punto = np.array([x1,y2])
		return punto
	m = (y3-y2)/(x3-x2)
	q = y2 - m*x2
	m_perp = -(1/m)
	q_perp = y1 - m_perp*x1
	punto = intersez_rette(-m,q,-m_perp,q_perp) #trovo intersezione tra segmento e retta perp passante per p1
	return punto


def gia_dentro_seg(seg, proiezioni):
	'''
	restituisce true se il segmento e' gia' nelle proiezioni
	'''
	for seg2 in proiezioni:
		if(seg == seg2):
			return True


def compreso(seg1, lista):
	'''
	restituisce true se il segmento e' interamente compreso in un altro segmento della lista
	'''
	x1 = seg1[0]
	y1 = seg1[1]
	x2 = seg1[2]
	y2 = seg1[3]
	for seg2 in lista:
		if(seg1!=seg2):
			x3 = seg2[0]
			y3 = seg2[1]
			x4 = seg2[2]
			y4 = seg2[3]
			if(x1==x2==x3==x4) and (y1>=y3) and (y2<=y4):
				return True
			if(x1>x3) and (x2<=x4):
				return True
			if(x1>=x3) and (x2<x4):
				return True
	return False
			

def unisci_sovrapposti(proiezioni):
	'''
	restituisce 1 ogni volta che vengono trovate 2 proiezioni che si sovrappongono parzialmente, e viene creata e aggiunta l'unione delle 2 proiezioni, e queste 2 proiezioni vengono eliminate dalla lista delle proiezioni.
	'''
	for seg1 in proiezioni:
		x1 = seg1[0]
		y1 = seg1[1]
		x2 = seg1[2]
		y2 = seg1[3]
		for seg2 in proiezioni:
			if(seg1!=seg2):
				x3 = seg2[0]
				y3 = seg2[1]
				x4 = seg2[2]
				y4 = seg2[3]
				if(x1==x2==x3==x4)and(y1<y3)and(y3<=y2<y4):
					nuovo = [x1,y1,x2,y4]
					proiezioni.append(nuovo)
					proiezioni.remove(seg1)
					proiezioni.remove(seg2)
					return 1
				if(x1<x3)and(x3<=x2<x4):
					nuovo = [x1,y1,x4,y4]
					proiezioni.append(nuovo)
					proiezioni.remove(seg1)
					proiezioni.remove(seg2)
					return 1
	return 0


def calcola_cov(edge, proiezioni):
	'''
	restituisce la somma delle lunghezze delle proiezioni sull'edge, in pratica restituisce lo spazio di edge occupato dalle proiezioni
	'''
	x1 = edge.x1
	y1 = edge.y1
	x2 = edge.x2
	y2 = edge.y2
	cov = 0
	for seg in proiezioni:
		x3 = seg[0]
		y3 = seg[1]
		x4 = seg[2]
		y4 = seg[3]
		if(x1==x2==x3==x4):
			if (y3<=y1) and (y4>=y2):
				return (y2-y1)
			if (y3>=y1) and (y4<=y2):
				cov += (y4-y3)
			if (y1<y3<y2) and (y4>y2):
				cov += (y2-y3)
			if (y3<y1) and (y1<y4<y2):
				cov += (y4-y1)
		else:
			if(x3<=x1) and (x4>=x2):
				return lunghezza(x1,y1,x2,y2)
			if(x3>=x1) and (x4<=x2):
				cov += lunghezza(x3,y3,x4,y4)
			if(x1<x3<x2) and (x4>x2):
				cov += lunghezza(x3,y3,x2,y2)
			if(x3<x1) and (x1<x4<x2):
				cov += lunghezza(x1,y1,x4,y4)
	return cov


def edge_adiacenti(x, y, edge, edges):
	'''
	restituisce lista di edges diversi dall'edge, con m diversa, e che come estremo hanno x1 y1
	'''
	e = []
	for altro_edge in edges:
		x1 = altro_edge.x1
		y1 = altro_edge.y1
		x2 = altro_edge.x2
		y2 = altro_edge.y2 
		if (edge!=altro_edge) and ( ( (x1==x)and(y1==y) ) or ( (x2==x)and(y2==y) ) ) and not ( stessa_m(edge, altro_edge) ):
			e.append(altro_edge)	
	return e


def stessa_m(edge, altro_edge,epsilon = 0.05):
	'''
	restituisce true se i 2 edge hanno stessa inclinazione
	'''
	x1 = edge.x1
	y1 = edge.y1
	x2 = edge.x2
	y2 = edge.y2
	x3 = altro_edge.x1
	y3 = altro_edge.y1
	x4 = altro_edge.x2
	y4 = altro_edge.y2
	if(x1==x2) and (x3==x4):
		return True
	if ((x1==x2) and (x3!=x4)) or ((x1!=x2) and (x3==x4)):
		return False
	m1 = (y2-y1)/(x2-x1)
	m2 = (y4-y3)/(x4-x3)
	if abs(m1-m2) < epsilon:
		return True
	return False

def set_segment_label(walls, label):

	for index, segment in enumerate(walls):
		segment.set_cluster_spaziale(label[index])
		
	return walls

def set_segment_label2(angolar_ordered, label):

	#siccome facendo un clustering spaziale per ogni cluster angolare, ottengo label uguali per ogni cluster angolare, mi conviene
	#aggiungere un fattore uguale al numero di cluster usati durante il fit del metodo di clustering(in questo caso 50 ) 
	c = 0
	for ang, l in zip(angolar_ordered, label):
		for index, segment in enumerate(ang):
			#segment.set_cluster_spaziale(l[index] + c)
			if l[index] !=-1:
				segment.set_cluster_muro(l[index] + c)
			else:#in questo caso stiamo trattando con segmenti che sono stati classificati come outlier dal metodo DBSCAN
				segment.set_cluster_muro(l[index]) # metto all'interno di un cluster tutti gli outlier
		c = c + len(set(l))
		
		
	#ricostruisco la lista dei segmenti, tieni conto che non sono piu' ordinati 
	walls=[]
	for ang in angolar_ordered:
		for segment in ang:
			walls.append(segment)
	return walls
