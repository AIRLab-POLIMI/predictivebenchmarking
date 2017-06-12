'''
Una superficie e' un poligono atomico che non puo' essere scomposto nelle sue parti.
L'unione di piu' superfici forma uno spazio.
'''
from __future__ import division
import Segmento as sg
from matplotlib import pyplot as plt

#oggetto di tipo Faccia, ha come attributo una lista di edges che formano un poligono chiuso. La dimensione della lista e' >3.
class Cella(object):
	def __init__(self,edges):
		self.bordi = edges
	def set_out(self,o):
		self.out = o
	def set_parziale(self,p):
		self.parziale = p


def crea_celle(edges):
	'''
	crea le facce come catene chiuse di edges adiacenti
	''' 
	facce = []
	creata = False

	creata = crea_facce3(facce, edges)
	while creata:
		creata = crea_facce3(facce, edges)
	
	creata = crea_facce4(facce, edges)
	while creata:
		creata = crea_facce4(facce, edges)
	
	creata = crea_facce5(facce, edges)
	while creata:
		creata = crea_facce5(facce, edges)
	
	creata = crea_facce6(facce, edges)
	while(creata):
		creata = crea_facce6(facce, edges)
	
	return facce


def crea_facce3(facce, edges):
	'''
	se trova una faccia di 3 lati non ancora presente in facce, la crea e la aggiunge a facce, e restituisce True. Altrimenti False.
	'''
	boards = []
	edge_rimasti = []
	#lista di tutti gli edge associati a meno di 2 facce, quindi che ancora possono creare una faccia
	for edge in edges:
		if (edge.num_facce < 2):
			edge_rimasti.append(edge)
	for edge in edge_rimasti:
		x1 = edge.x1
		y1 = edge.y1
		x2 = edge.x2
		y2 = edge.y2
		#print("edge = ")
		#print(x1,y1,x2,y2)
		#ogni volta metto in comune_x e comune_y le coord del punto per cui voglio trovare gli adiacenti 
		comune_x_edge = x1
		comune_y_edge = y1
		adiacenti = sg.edge_adiacenti(comune_x_edge, comune_y_edge, edge, edge_rimasti)
		#edge che hanno come estremo il punto x1,y1 e m diversa da quella dell'edge
		for a in adiacenti:
			x3 = a.x1
			y3 = a.y1
			x4 = a.x2
			y4 = a.y2
			#se c'e' gia faccia con quei 2 lati non vado avanti, cerco un altro adiacente
			if(esiste_faccia(edge, a, facce)): 
				break
			#print("a = ")
			#print(x3,y3,x4,y4)
			#vedo gli edge che hanno come estremo quello diverso da quello controllato prima
			if (x3==comune_x_edge) and (y3==comune_y_edge):
				comune_x_a = x4
				comune_y_a = y4
				adiacenti2 = sg.edge_adiacenti(comune_x_a, comune_y_a, a, edge_rimasti)
			else:
				comune_x_a = x3
				comune_y_a = y3
				adiacenti2 = sg.edge_adiacenti(comune_x_a, comune_y_a, a, edge_rimasti)
			for b in adiacenti2:
				x5 = b.x1
				y5 = b.y1
				x6 = b.x2
				y6 = b.y2
				#print("b = ")
				#print(x5,y5,x6,y6)
				if (x5==comune_x_a) and (y5==comune_y_a):
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x6==x2) and (y6==y2):
						#print("trovata faccia con bordi: ")
						#print(x1,y1,x2,y2)
						#print(x3,y3,x4,y4)
						#print(x5,y5,x6,y6)
						boards.extend((edge,a,b))
						faccia = Cella(boards) 
						if not (gia_dentro(faccia, facce)):
							#print("faccia aggiunta alle facce")
							edge.num_facce += 1
							a.num_facce += 1
							b.num_facce += 1
							facce.append(faccia)
							return True
						else:
							#print("faccia gia presente")
							del boards [:]
				else:
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x5==x2) and (y5==y2):
						#print("trovata faccia con bordi: ")
						#print(x1,y1,x2,y2)
						#print(x3,y3,x4,y4)
						#print(x5,y5,x6,y6)
						boards.extend((edge, a, b))
						faccia = Cella(boards)
						if not (gia_dentro(faccia, facce)):
							#print("faccia aggiunta alle facce")
							edge.num_facce += 1
							a.num_facce += 1
							b.num_facce += 1
							facce.append(faccia)
							return True
						else:
							#print("faccia gia presente")
							del boards [:]
		
	return False


def crea_facce4(facce, edges):
	'''
	se trova una faccia di 4 lati non ancora presente in facce, la crea e la aggiunge a facce, e ritorna True. Altrimenti False.
	'''
	boards = []
	edge_rimasti = []
	#lista di tutti gli edge associati a meno di 2 facce, quindi che ancora possono creare una faccia
	for edge in edges:
		if (edge.num_facce < 2):
			edge_rimasti.append(edge)
	for edge in edge_rimasti:
		x1 = edge.x1
		y1 = edge.y1
		x2 = edge.x2
		y2 = edge.y2
		#print("edge = ")
		#print(x1,y1,x2,y2)
		#ogni volta metto in comune_x e comune_y le coord del punto per cui voglio trovare gli adiacenti 
		comune_x_edge = x1
		comune_y_edge = y1
		adiacenti = sg.edge_adiacenti(comune_x_edge,comune_y_edge,edge,edge_rimasti)
		#edge che hanno come estremo il punto x1,y1 e m diversa da quella dell'edge
		for a in adiacenti:
			x3 = a.x1
			y3 = a.y1
			x4 = a.x2
			y4 = a.y2
			#print("a = ")
			#print(x3,y3,x4,y4)
			#vedo gli edge che hanno come estremo quello diverso da quello controllato prima
			if(esiste_faccia(edge,a,facce)): 
				break
			if (x3==comune_x_edge) and (y3==comune_y_edge):
				comune_x_a = x4
				comune_y_a = y4
				adiacenti2 = sg.edge_adiacenti(comune_x_a,comune_y_a,a,edge_rimasti)
			else:
				comune_x_a = x3
				comune_y_a = y3
				adiacenti2 = sg.edge_adiacenti(comune_x_a,comune_y_a,a,edge_rimasti)
			for b in adiacenti2:
				x5 = b.x1
				y5 = b.y1
				x6 = b.x2
				y6 = b.y2
				#print("b = ")
				#print(x5,y5,x6,y6)
				if (x5==comune_x_a) and (y5==comune_y_a):
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x6==x2) and (y6==y2):
						adiacenti3 = []
						#nel for successivo nemmeno ci entro e quindi scelgo un altro b del for precedente
					else: #se non si e chiusa una faccia di 3 lati
						comune_x_b = x6
						comune_y_b = y6
						adiacenti3 = sg.edge_adiacenti(comune_x_b,comune_y_b,b,edge_rimasti)
				else:
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x5==x2) and (y5==y2):
						adiacenti3 = []
							
					else: #se non si e chiusa una faccia di 3 lati
						comune_x_b = x5
						comune_y_b = y5
						adiacenti3 = sg.edge_adiacenti(comune_x_b,comune_y_b,b,edge_rimasti)
				for c in adiacenti3:
					x7 = c.x1
					y7 = c.y1
					x8 = c.x2
					y8 = c.y2
					#print("c = ")
					#print(x7,y7,x8,y8)
					if (x7==comune_x_b) and (y7==comune_y_b):
					#potrebbe essere una faccia di 4 lati, vedo se sono tornato alle coordinate del primo edge
						if (x8==x2) and (y8==y2) and not(sg.stessa_m(edge,c)):
							#print("trovata faccia con bordi: ")
							#print(x1,y1,x2,y2)
							#print(x3,y3,x4,y4)
							#print(x5,y5,x6,y6)
							#print(x7,y7,x8,y8)
							boards.extend((edge,a,b,c))
							faccia = Cella(boards)
							if not (gia_dentro(faccia,facce)):
								#print("faccia aggiunta alle facce")
								edge.num_facce += 1
								a.num_facce += 1
								b.num_facce += 1
								c.num_facce += 1
								facce.append(faccia)
								return True
							else:
								#print("faccia gia presente")
								del boards [:]
					else:
					#potrebbe essere una faccia di 4 lati, vedo se sono tornato alle coordinate del primo edge
						if (x7==x2) and (y7==y2) and not(sg.stessa_m(edge,c)):
							#print("trovata faccia con bordi: ")
							#print(x1,y1,x2,y2)
							#print(x3,y3,x4,y4)
							#print(x5,y5,x6,y6)
							#print(x7,y7,x8,y8)
							boards.extend((edge,a,b,c))
							faccia = Cella(boards)
							if not (gia_dentro(faccia,facce)):
								#print("faccia aggiunta alle facce")
								edge.num_facce += 1
								a.num_facce += 1
								b.num_facce += 1
								c.num_facce += 1
								facce.append(faccia)
								return True
							else:	
								#print("faccia gia presente")
								del boards [:]
	return False


def crea_facce5(facce, edges):
	'''
	se trova una faccia di 5 lati non ancora presente in facce, la crea e la aggiunge a facce, e ritorna True. Altrimenti False.
	'''
	controllo = []
	boards = []
	edge_rimasti = []
	#lista di tutti gli edge associati a meno di 2 facce, quindi che ancora possono creare una faccia
	for edge in edges:
		if (edge.num_facce < 2):
			edge_rimasti.append(edge)
	for edge in edge_rimasti:
		x1 = edge.x1
		y1 = edge.y1
		x2 = edge.x2
		y2 = edge.y2
		#print("edge = ")
		#print(x1,y1,x2,y2)
		#ogni volta metto in comune_x e comune_y le coord del punto per cui voglio trovare gli adiacenti 
		comune_x_edge = x1
		comune_y_edge = y1
		adiacenti = sg.edge_adiacenti(comune_x_edge,comune_y_edge,edge,edge_rimasti)
		#edge che hanno come estremo il punto x1,y1 e m diversa da quella dell'edge
		for a in adiacenti:
			x3 = a.x1
			y3 = a.y1
			x4 = a.x2
			y4 = a.y2
			#print("a = ")
			#print(x3,y3,x4,y4)
			#vedo gli edge che hanno come estremo quello diverso da quello controllato prima
			if(esiste_faccia(edge,a,facce)): 
				break
			if (x3==comune_x_edge) and (y3==comune_y_edge):
				comune_x_a = x4
				comune_y_a = y4
				adiacenti2 = sg.edge_adiacenti(comune_x_a,comune_y_a,a,edge_rimasti)
			else:
				comune_x_a = x3
				comune_y_a = y3
				adiacenti2 = sg.edge_adiacenti(comune_x_a,comune_y_a,a,edge_rimasti)
			for b in adiacenti2:
				x5 = b.x1
				y5 = b.y1
				x6 = b.x2
				y6 = b.y2
				#print("b = ")
				#print(x5,y5,x6,y6)
				if (x5==comune_x_a) and (y5==comune_y_a):
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x6==x2) and (y6==y2):
						adiacenti3 = []
						#nel for successivo nemmeno ci entro e quindi scelgo un altro b del for precedente
					else: #se non si e chiusa una faccia di 3 lati
						comune_x_b = x6
						comune_y_b = y6
						adiacenti3 = sg.edge_adiacenti(comune_x_b,comune_y_b,b,edge_rimasti)
				else:
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x5==x2) and (y5==y2):
						adiacenti3 = []
							
					else: #se non si e chiusa una faccia di 3 lati
						comune_x_b = x5
						comune_y_b = y5
						adiacenti3 = sg.edge_adiacenti(comune_x_b,comune_y_b,b,edge_rimasti)
				for c in adiacenti3:
					x7 = c.x1
					y7 = c.y1
					x8 = c.x2
					y8 = c.y2
					#print("c = ")
					#print(x7,y7,x8,y8)
					if (x7==comune_x_b) and (y7==comune_y_b):
					#potrebbe essere una faccia di 4 lati, vedo se sono tornato alle coordinate del primo edge
						if (x8==x2) and (y8==y2) and not(sg.stessa_m(edge,c)):
							adiacenti4 = []
						else: #se non si e chiusa una faccia di 4 lati
							comune_x_c = x8
							comune_y_c = y8
							adiacenti4 = sg.edge_adiacenti(comune_x_c,comune_y_c,c,edge_rimasti)
					else:
					#potrebbe essere una faccia di 4 lati, vedo se sono tornato alle coordinate del primo edge
						if (x7==x2) and (y7==y2) and not(sg.stessa_m(edge,c)):
							adiacenti4 = []		
						else: #se non si e chiusa una faccia di 4 lati
							comune_x_c = x7
							comune_y_c = y7
							adiacenti4 = sg.edge_adiacenti(comune_x_c,comune_y_c,c,edge_rimasti)
					for d in adiacenti4:
						x9 = d.x1
						y9 = d.y1
						x10 = d.x2
						y10 = d.y2
						#print("d = ")
						#print(x9,y9,x10,y10)
						if (x9==comune_x_c) and (y9==comune_y_c):
						#potrebbe essere una faccia di 5 lati, vedo se sono tornato alle coordinate del primo edge
							if (x10==x2) and (y10==y2) and (d!=edge) and not(sg.stessa_m(edge,d)):
								#print("trovata faccia con bordi: ")
								#print(x1,y1,x2,y2)
								#print(x3,y3,x4,y4)
								#print(x5,y5,x6,y6)
								#print(x7,y7,x8,y8)
								#print(x9,y9,x10,y10)
								boards.extend((edge,a,b,c,d))
								faccia = Cella(boards)
								if not (gia_dentro(faccia,facce)):
									#print("faccia aggiunta alle facce")
									edge.num_facce += 1
									a.num_facce += 1
									b.num_facce += 1
									c.num_facce += 1
									d.num_facce += 1
									facce.append(faccia)
									return True
								else:
									del boards [:]
						else:
						#potrebbe essere una faccia di 5 lati, vedo se sono tornato alle coordinate del primo edge
							if (x9==x2) and (y9==y2) and (d!=edge) and not(sg.stessa_m(edge,d)):
								#print("trovata faccia con bordi: ")
								#print(x1,y1,x2,y2)
								#print(x3,y3,x4,y4)
								#print(x5,y5,x6,y6)
								#print(x7,y7,x8,y8)
								#print(x9,y9,x10,y10)
								boards.extend((edge,a,b,c,d))
								faccia = Cella(boards)
								if not (gia_dentro(faccia,facce)):
									#print("faccia aggiunta alle facce")
									edge.num_facce += 1
									a.num_facce += 1
									b.num_facce += 1
									c.num_facce += 1
									d.num_facce += 1
									facce.append(faccia)
									return True
								else:
									del boards [:]		 
	return False


def crea_facce6(facce, edges):
	'''
	se trova una faccia di 6 lati non ancora presente in facce, la crea e la aggiunge a facce, e ritorna True. Altrimenti False.
	'''
	controllo = []
	boards = []
	edge_rimasti = []
	#lista di tutti gli edge associati a meno di 2 facce, quindi che ancora possono creare una faccia
	for edge in edges:
		if (edge.num_facce < 2):
			edge_rimasti.append(edge)
	for edge in edge_rimasti:
		x1 = edge.x1
		y1 = edge.y1
		x2 = edge.x2
		y2 = edge.y2
		#print("edge = ")
		#print(x1,y1,x2,y2)
		#ogni volta metto in comune_x e comune_y le coord del punto per cui voglio trovare gli adiacenti 
		comune_x_edge = x1
		comune_y_edge = y1
		adiacenti = sg.edge_adiacenti(comune_x_edge,comune_y_edge,edge,edge_rimasti)
		#edge che hanno come estremo il punto x1,y1 e m diversa da quella dell'edge
		for a in adiacenti:
			x3 = a.x1
			y3 = a.y1
			x4 = a.x2
			y4 = a.y2
			#print("a = ")
			#print(x3,y3,x4,y4)
			#vedo gli edge che hanno come estremo quello diverso da quello controllato prima
			if(esiste_faccia(edge,a,facce)): 
				break
			if (x3==comune_x_edge) and (y3==comune_y_edge):
				comune_x_a = x4
				comune_y_a = y4
				adiacenti2 = sg.edge_adiacenti(comune_x_a,comune_y_a,a,edge_rimasti)
			else:
				comune_x_a = x3
				comune_y_a = y3
				adiacenti2 = sg.edge_adiacenti(comune_x_a,comune_y_a,a,edge_rimasti)
			for b in adiacenti2:
				x5 = b.x1
				y5 = b.y1
				x6 = b.x2
				y6 = b.y2
				#print("b = ")
				#print(x5,y5,x6,y6)
				if (x5==comune_x_a) and (y5==comune_y_a):
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x6==x2) and (y6==y2):
						adiacenti3 = []
						#nel for successivo nemmeno ci entro e quindi scelgo un altro b del for precedente
					else: #se non si e chiusa una faccia di 3 lati
						comune_x_b = x6
						comune_y_b = y6
						adiacenti3 = sg.edge_adiacenti(comune_x_b,comune_y_b,b,edge_rimasti)
				else:
				#potrebbe essere una faccia di 3 lati, vedo se sono tornato alle coordinate del primo edge
					if (x5==x2) and (y5==y2):
						adiacenti3 = []
							
					else: #se non si e chiusa una faccia di 3 lati
						comune_x_b = x5
						comune_y_b = y5
						adiacenti3 = sg.edge_adiacenti(comune_x_b,comune_y_b,b,edge_rimasti)
				for c in adiacenti3:
					x7 = c.x1
					y7 = c.y1
					x8 = c.x2
					y8 = c.y2
					#print("c = ")
					#print(x7,y7,x8,y8)
					if (x7==comune_x_b) and (y7==comune_y_b):
					#potrebbe essere una faccia di 4 lati, vedo se sono tornato alle coordinate del primo edge
						if (x8==x2) and (y8==y2) and not(sg.stessa_m(edge,c)):
							adiacenti4 = []
						else: #se non si e chiusa una faccia di 4 lati
							comune_x_c = x8
							comune_y_c = y8
							adiacenti4 = sg.edge_adiacenti(comune_x_c,comune_y_c,c,edge_rimasti)
					else:
					#potrebbe essere una faccia di 4 lati, vedo se sono tornato alle coordinate del primo edge
						if (x7==x2) and (y7==y2) and not(sg.stessa_m(edge,c)):
							adiacenti4 = []		
						else: #se non si e chiusa una faccia di 4 lati
							comune_x_c = x7
							comune_y_c = y7
							adiacenti4 = sg.edge_adiacenti(comune_x_c,comune_y_c,c,edge_rimasti)
					for d in adiacenti4:
						x9 = d.x1
						y9 = d.y1
						x10 = d.x2
						y10 = d.y2
						#print("d = ")
						#print(x9,y9,x10,y10)
						if (x9==comune_x_c) and (y9==comune_y_c):
						#potrebbe essere una faccia di 5 lati, vedo se sono tornato alle coordinate del primo edge
							if (x10==x2) and (y10==y2) and (d!=edge) and not(sg.stessa_m(edge,d)):
								adiacenti5 = []
							else:
								comune_x_d = x10
								comune_y_d = y10
								adiacenti5 = sg.edge_adiacenti(comune_x_d,comune_y_d,d,edge_rimasti)
						else:
						#potrebbe essere una faccia di 5 lati, vedo se sono tornato alle coordinate del primo edge
							if (x9==x2) and (y9==y2) and (d!=edge) and not(sg.stessa_m(edge,d)):
								 adiacenti5 = []
							else:
								comune_x_d = x9
								comune_y_d = y9
								adiacenti5 = sg.edge_adiacenti(comune_x_d,comune_y_d,d,edge_rimasti)
						for e in adiacenti5:
							x11 = e.x1
							y11 = e.y1
							x12 = e.x2
							y12 = e.y2
							#print("d = ")
							#print(x9,y9,x10,y10)
							if (x11==comune_x_d) and (y11==comune_y_d):
							#potrebbe essere una faccia di 5 lati, vedo se sono tornato alle coordinate del primo edge
								if (x12==x2) and (y12==y2) and (e!=edge) and not(sg.stessa_m(edge,e)):
									#print("trovata faccia con bordi: ")
									#print(x1,y1,x2,y2)
									#print(x3,y3,x4,y4)
									#print(x5,y5,x6,y6)
									#print(x7,y7,x8,y8)
									#print(x9,y9,x10,y10)
									boards.extend((edge,a,b,c,d,e))
									faccia = Cella(boards)
									if not (gia_dentro(faccia,facce)):
										#print("faccia aggiunta alle facce")
										edge.num_facce += 1
										a.num_facce += 1
										b.num_facce += 1
										c.num_facce += 1
										d.num_facce += 1
										e.num_facce += 1
										facce.append(faccia)
										return True
									else:
										del boards [:]
							else:
							#potrebbe essere una faccia di 5 lati, vedo se sono tornato alle coordinate del primo edge
								if (x11==x2) and (y11==y2) and (e!=edge) and not(sg.stessa_m(edge, e)):
									#print("trovata faccia con bordi: ")
									#print(x1,y1,x2,y2)
									#print(x3,y3,x4,y4)
									#print(x5,y5,x6,y6)
									#print(x7,y7,x8,y8)
									#print(x9,y9,x10,y10)
									boards.extend((edge,a,b,c,d,e))
									faccia = Cella(boards)
									if not (gia_dentro(faccia, facce)):
										#print("faccia aggiunta alle facce")
										edge.num_facce += 1
										a.num_facce += 1
										b.num_facce += 1
										c.num_facce += 1
										d.num_facce += 1
										e.num_facce += 1
										facce.append(faccia)
										return True
									else:
										del boards [:]	
	return False


def esiste_faccia(edge, a, facce):
	'''
	ritorna True se esiste gia' una faccia con bordi edge e a
	'''	
	for faccia in facce:
		if (edge in faccia.bordi) and (a in faccia.bordi):
			return True
	return False


def gia_dentro(faccia,facce):
	'''
	ritorna true se la faccia e' gia' nella lista facce oppure se ce n'e' gia' una con almeno 2 edge in comune
 	'''
	bordi = faccia.bordi
	for altra_faccia in facce:
		altri_bordi = altra_faccia.bordi
		if (all(dentro(bordo, altri_bordi) for bordo in bordi)) and (all(dentro(altro_bordo, bordi) for altro_bordo in altri_bordi)):
			return True
		if(len(edge_comune(faccia, altra_faccia))>=2):
			return True
	return False


def dentro(bordo, bordi):
	'''
	ritorna True se bordo e' incluso in bordi
	'''
	if bordo in bordi:
		return True
	else:
		return False


def edge_comune(faccia, altra_faccia):
	'''
	ritorna lista di edges in comune tra le due facce
	'''
	bordi1 = []
	bordi2 = []
	for bordo in faccia.bordi:
		bordi1.append(bordo)
	for bordo in altra_faccia.bordi:
		bordi2.append(bordo)	
	return(list(set(bordi1).intersection(bordi2)))


def adiacenti(faccia, altra_faccia):
	'''
	ritorna true se le due facce sono adiacenti
	'''
	bordi1 = []
	bordi2 = []
	#print("edges della faccia : ")
	for bordo in faccia.bordi:
		bordi1.append(bordo)
		#print (bordo.x1,bordo.y1,bordo.x2,bordo.y2)
	#print("edges della faccia : ")
	for bordo in altra_faccia.bordi:
		bordi2.append(bordo)
		#print (bordo.x1,bordo.y1,bordo.x2,bordo.y2)
	in_comune = list(set(bordi1).intersection(bordi2))
	if(len(in_comune) == 0):
		#print("nessuno in comune, non sono adiacenti")
		return False
	#print("in comune: ")
	return True


def disegna_facce(facce):
	'''
	disegna le facce
	'''
	ascisse = []
	ordinate = []
	for faccia in facce:
		for edge in faccia.bordi:
			ascisse.append(edge.x1)
			ascisse.append(edge.x2)
			ordinate.append(edge.y1)
			ordinate.append(edge.y2)
			plt.plot(ascisse,ordinate, color='k', linewidth=2.0)
			del ascisse[:]
			del ordinate[:]
	plt.show()

