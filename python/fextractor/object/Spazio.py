'''
spazio si intende un ambiente composto da piu' superfici alla quale e' possibile associare un significato diverso a seconda della forma e della dimensione che possiede.
Uno spazio infatti puo' essere distinto tra corridoio o stanza
'''
from shapely.ops import cascaded_union
from object import Extended_segment as ext
from object import Superficie as fc #prima si chiamava cella 


class Spazio(object):
	def __init__(self, cells, stanza, celle_corrispondenti, id):
		self.cells = crea_cellette(cells, celle_corrispondenti)#questi prima erano dei semplici poligoni, ora sono delle vere e proprie celle
		self.spazio = stanza
		self.id = id
		#self.out = True #di default e' esterno 
		self.out = False#di default e' interno 
		self.parziale = False
		self.area_predetta =0 #l'area predetta di uno spazio di default e' 0
		#self.area_originale = stanza.area #questa rappresenta l'area della stanza originale
	def set_out(self,o):
		self.out = o
	def set_parziale(self,p):
		self.parziale = p
	def set_tipo(self,t):
		self.tipo = t
	def set_id(self, id):
		self.id = id
	def add_cell(self, cell):
		self.cell.append(cell)
	def set_spazio(self,spazio):
		self.spazio = spazio
	def set_area_predetta(self, area):
		self.area_predetta = area
	def set_cluster_frontiera(self, cluster_fr):
		self.cluster_frontiera = cluster_fr
	def set_tocco_bordo(self, tb):
		self.tocco_bordo = tb
	def set_area_originale(self, area_originale):
		self.area_originale = area_originale

class Celletta(object):
	def __init__(self, polygon_cella, cella_normale):
		self.cella = polygon_cella #oggetto di tipo poligono
		self.c = cella_normale #oggetto di tipo Superficie(mi serve per il peso degli edge)
		#self.out = True #default
		self.parziale = False #default
	def set_celletta_out(self, o):
		self.out = o
	def set_celletta_parziale(self, p):
		self.parziale = p
	def set_vedo_frontiera(self, bool): #mi serve specialmente per immagazzinare l'informazione che una cella ha visto anche solo una piccola parte di una frontiera
		self.vedo_frontiera = bool
	def set_cluster_frontiera(self, cluster):
		self.cluster_frontiera = cluster
		
def crea_cellette(cells, celle_corrispondenti):	
	cellette = []
	for cella, c in zip(cells,celle_corrispondenti):
		c = Celletta(cella, c)
		cellette.append(c)
	return cellette
		
def get_spazi_reali(spazi, stanze_reali):
	'''
	setto come 'in' tutti gli spazi che sono collegati ad altri spazi.
	'''
	for s in spazi:
		for st in stanze_reali:
			if s.spazio.equals(st):
				s.set_out(False)
	return spazi
def get_spazi_reali_v2(spazi, stanze_reali):
	'''
	setto come 'in' tutti gli spazi che sono collegati ad altri spazi.
	'''
	for s in spazi:
		trovato = False
		for st in stanze_reali:
			if s.spazio.equals(st):	
				trovato = True
		if trovato == False:
			s.set_out(True)
	
	

def trova_spazi_parziali(spazi):
	'''
	se all'interno della lista delle celle che compongono uno spazio c'e' anche una sola cella 
	parziale allora anche lo spazio lo e'
	'''	
	for s in spazi:
		c =[]
		trovato=False
		cluster = None
		for cella in s.cells:
			if cella.parziale == True:
				c.append(cella.cluster_frontiera)
				trovato = True
				cluster = cella.cluster_frontiera
		if trovato == True:
			s.set_parziale(True)
		'''
		#-----added
		max = 0
		for elem in c:
			if c.count(elem) > max:
				max = c.count(elem)
				cluster = elem			
		#---------------------	
		'''
		s.set_cluster_frontiera(cluster) #assegno None se non e' una stanza parziale, mentre il cluster della frontiera se lo e'
			
	return spazi

def set_cellette_parziali(spazi, parz_poligoni):
	'''
	siccome e' praticamente impossibile ricavare le celle parziali per come ha costruito il layout, mi trovo costretto a ricontrollare che una cella sia parziale in questo modo.
	se una cella che ora e' un oggetto e nn solo un poligono, interseca il contorno allora e' fuori.
	'''
	
	for s in spazi:
		for cella in s.cells:
			for pp in parz_poligoni:
				if cella.cella.equals(pp):
					cella.set_celletta_parziale(True)#setto la celletta a out = True se e' nella lista delle celle out il default e' False.
	
	
	# for index, s in enumerate(spazi):
# 		for cella in s.cells:
# 			if index%2 == 0: #TODO: trovare una funzine che mi permetti di capire se la cella e' out. se l'intersezione e' considerevole allora setto la cella come parziale. 
# 				cella.set_celletta_parziale(True)
# 			else:
# 				cella.set_celletta_parziale(False)


def get_cellette_poligoni(spazio):
	'''
	restituisce le cellette di uno spazio
	'''
	cellette_poligoni = []
	for celletta in spazio.cells:
		cellette_poligoni.append(celletta.cella)
	
	return cellette_poligoni

def get_cellette_vecchie(spazio):
	'''
	restituisce l'oggetto cella con il vecchio metodo
	'''
	cellette_vecchie = []
	for celletta in spazio.cells:
		cellette_vecchie.append(celletta.c)
	
	return cellette_vecchie

def unisci_spazi(s1,s2):
	'''
	creo uno spazio che e' l'unione di due spazi
	'''
	#estraggo le celle come oggetto poligono del primo spazio 
	celle_poligoni1= get_cellette_poligoni(s1)
	celle_vecchie1 = get_cellette_vecchie(s1)
	
	#estraggo le celle vecchie del secondo spazio
	celle_poligoni2= get_cellette_poligoni(s2)
	celle_vecchie2 = get_cellette_vecchie(s2)

	#uso l'id del primo spazio
	id = s1.id
	#creo la lista di celle poligono e delle vecchie celle
	celle_poligono = celle_poligoni1 + celle_poligoni2
	celle_vecchie = celle_vecchie1 + celle_vecchie2
	#unisco la stanza
	
	stanza = s1.spazio.union(s2.spazio)#questo crea MultiPolygon.Sbagliato
	#stanza = cascaded_union([s1.spazio, s2.spazio])
	
	nuovo_spazio = Spazio(celle_poligono, stanza, celle_vecchie, id)
	#setto il nuovo spazio come interno, dato che e' la composizione di due spazi interni
	nuovo_spazio.set_out(False)
	
	if s1.parziale == True or s2.parziale==True: #se una delle due stanze e' parziale anche l'unione lo e'
		nuovo_spazio.set_parziale(True)
	else:
		nuovo_spazio.set_parziale(False)
		
	return nuovo_spazio
	
	
	
	
def aggiungi_cella_a_spazio(spazio, cella, plan_o):
	
	#la cella non e' piu out 
	cella.set_celletta_out(False)
	#unisco la cella al poligono
	s = spazio.spazio.union(cella.cella)
	spazio.set_spazio(s)
	spazio.cells.append(cella)
	#tolgo dalla lista delle celle out del layout la cella che ho appena aggiunto.
	plan_o.cellette_esterne.remove(cella)

# def aggiungi_set_di_celle(spazio, set_celle, plan_o):
# 	'''
# 	aggiunge un set di celle ad uno spazio.
# 	'''
# 	set_celle = list(set(set_celle))
# 	polygons = []
# 	for cella in set_celle:
# 		#la cella non e' piu out 
# 		cella.set_celletta_out(False)
# 		polygons.append(cella.cella)
# 	#unisco la cella al poligono
# 	s = spazio.spazio.cascaded_union(polygons)
# 	spazio.set_spazio(s)
# 	for c in set_celle:
# 		spazio.cells.append(c)
# 		plan_o.cellette_esterne.remove(c)
	
	
#TODO: da verificare funzioni(sembra funzionare)
def elimina_cella_da_spazio(spazio, cella, plan_o):
	'''
	la cella non fa piu' parte della stanza parziale ma ritorna a far parte delle celle out.
	'''
	#la cella diventa out
	cella.set_celletta_out(True)
	#inserisco la cella tra le celle esterne del layout
	plan_o.cellette_esterne.append(cella)
	
	#tolgo la cella dal poligono originale
	s= spazio.spazio #poligono della stanza con anche la cella
	c= cella.cella #poligono della cella
	new_poly = s.difference(c)#TODO: da verificare funzioni veramente
	spazio.set_spazio(new_poly)
	#tolgo la cella dalla lista delle celle che compongono la stanza
	spazio.cells.remove(cella)


# def elimina_set_celle(spazio, set_celle, plan_o):
# 	'''
# 	elimina un inseime di celle da una spazio
# 	'''
# 	set_celle = list(set(set_celle))
# 	polygons = []
# 	for cella in set_celle:
# 		#la cella diventa out
# 		cella.set_celletta_out(True)
# 		polygons.append(cella.cella)
# 		#inserisco la cella tra le celle esterne del layout
# 		plan_o.cellette_esterne.append(cella)
# 		#tolgo la cella dal poligono originale
# 		s= spazio.spazio #poligono della stanza con anche la cella
# 		c= cella.cella #poligono della cella
# 		new_poly = s.difference(c)#TODO: da verificare funzioni veramente
# 		spazio.set_spazio(new_poly)
# 		#tolgo la cella dalla lista delle celle che compongono la stanza
# 		spazio.cells.remove(cella)

		
	
def estrai_extended_da_spazio(spazio, extended_segments, cellette_out):
	'''
	permette di estrarre le extended segment esterni di uno spazio
	'''
	#se c'e' una cella che condivide un edge con l'esterno allora l'extended di qull'edge e' esterno
	
	extended=[]
	edge_comuni=[]
	for celletta in spazio.cells:
		for celletta_out in cellette_out:
			if fc.adiacenti(celletta.c,celletta_out.c):
				comuni = fc.edge_comune(celletta.c,celletta_out.c)
				for e in comuni:
					edge_comuni.append(e)
		#controllo che non tocchi il bordo, se si aggiungo anche quelle celle 
		bordi_cella = celletta.c.bordi
		for e in bordi_cella:
			if e.cluster_spaziale == "bordo1" or e.cluster_spaziale == "bordo2" or e.cluster_spaziale == "bordo3" or e.cluster_spaziale == "bordo4":
				edge_comuni.append(e)

		
		
	edge_comuni = list(set(edge_comuni))
	for edge in edge_comuni:
		extended.append(ext.estrai_extended_segment_da_bordo_cella(edge, extended_segments))
	
	return list(set(extended))
	

def estrai_solo_extended_visti(spazio_parz, extended_segments, cellette_out):
	'''
	permette di estrarre tutti gli extended segments di una stanza parziale che sono stati sicuramente visti in precedenza.
	un extended segment risulta sicuramente visto se all'interno della stanza parziale esiste almeno una cella completa 
	che condivide pareti con l'esterno.
	
	non necessariamente l'esterno si puo' ad esempio controllare anche confrondando la cella con celle di altre stanze.
	'''
	
	celle = spazio_parz.cells
	cellette = []  # ci sono solo le celle della stanza parziale complete
	
	for ce in celle:
		if ce.parziale == False:
			cellette.append(ce)
	
	extended=[]
	edge_comuni=[]
	for celletta in cellette:
		for celletta_out in cellette_out:
			if fc.adiacenti(celletta.c,celletta_out.c):
				comuni = fc.edge_comune(celletta.c,celletta_out.c)
				for e in comuni:
					edge_comuni.append(e)
	
	edge_comuni = list(set(edge_comuni))
	for edge in edge_comuni:
		extended.append(ext.estrai_extended_segment_da_bordo_cella(edge, extended_segments))
	
	return list(set(extended))
	

	