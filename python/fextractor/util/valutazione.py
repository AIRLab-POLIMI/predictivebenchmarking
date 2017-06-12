'''
in questo modulo ci sono tutti le funzioni di score e penalita' per calcolare la funzione di costo.
'''
from object import Plan as plan
from object import Spazio as sp

import math

def score1(stanza, cella, plan_o):
	'''
	primo score, stanza-> stanza parziale considerata,cella --> cella aggiunta plan_o --> layout fino ad ora ottenuto.
	'''
	a= 0
	
def score2(stanza, plan_o, celle_di_altre_stanze):
	'''
	attribuisce un valore positivo, pari alla somma dei persi degli extended segment del bordo di una stanza. Favorisce stanze supportate da 
	extended segment molto importanti.
	'''
	#estraggo extended da stanza
	celle_circostanti = celle_di_altre_stanze + plan_o.cellette_esterne #creo una lista delle celle circostanti ad una stanza		
	a = sp.estrai_extended_da_spazio(stanza, plan_o.extended_segments, celle_circostanti)
	tot_segment = list(set(a))
	
	somma = 0
	for ext in tot_segment:
		somma = somma + ext.peso
		
	return somma
		

	
def penalita1(stanza):
	'''
	penalizza ambieneti concavi
	'''
	
	#area della stanza 
	spazio= stanza.spazio
	area_spazio = spazio.area
	#area del convex hull
	convexHull = spazio.convex_hull
	area_convex_hull = convexHull.area
	#calcolo della penalita'
	penal1 = (area_convex_hull - area_spazio) / area_spazio

	#TODO: valutare se conviene andare a normalizzare penal1 con un valore tra 0,1
	#penal1= 1- 1/penal1 #computo la percentuale di concavita'
	
	return penal1 
	
	
def penalita2(stanza, plan_o, celle_di_altre_stanze):
	'''
	controlla che la stanza non stia toccando il bordo
	se la stanza tocca il bordo, la prenalita' deve essere altissima, perche' non voglio aggiungere quste celle.
	'''
	#estraggo extended da stanza
	celle_circostanti = celle_di_altre_stanze + plan_o.cellette_esterne #creo una lista delle celle circostanti ad una stanza		
	a = sp.estrai_extended_da_spazio(stanza, plan_o.extended_segments, celle_circostanti)
	tot_segment = list(set(a))
	#estraggo extended dal bordo dell'immagine
	bordi_immagine = plan.estrai_extended_segments_del_bordo(plan_o.extended_segments)
	
	trovato = False
	for bordo in bordi_immagine:
		for e in tot_segment:
			if e == bordo:
				trovato = True
	
		
	if trovato ==True:
		#ho trovato un bordo della stanza che tocca il bordo dell'immagine
		return 1
	else:
		return 0
	
def penalita4(stanza, plan_o, celle_di_altre_stanze):
	'''
	piu' e' alto il numero di extended introdotto piu' questa penalita' sara' alta, e la calcolo sul numero di extended che formano la stanza
	'''
	celle_circostanti = celle_di_altre_stanze + plan_o.cellette_esterne #creo una lista delle celle circostanti ad una stanza		
	a = sp.estrai_extended_da_spazio(stanza, plan_o.extended_segments, celle_circostanti)
	tot_segment = list(set(a))
	
	return 1* len(set(tot_segment))


def cost_funzion(penal1, penal2, penal4):
	'''
	computa la funzione di costo
	TODO: aggiungere gli altri score e penalita'
	'''	
	k3 = 10 #controlla la convessita'
	k4 = 50 #molto importante non voglio celle che toccano il bordo dell'immagine
	k6 = 1 #controlla il numero di extended introdotte
	cost_function = (k3*penal1) + (k4*penal2) + (k6*penal4)
	
	return cost_function

def Boltzman_equation(cost_function):
	'''
	computa la Boltzman_equation a partire dalla funzione di costo
	'''
	
	beta = 1
	
	return math.exp(-beta*cost_function)

#-----------------------------------------------------------------------------------------
#di seguito uso un'altra funzione di costo che sto usando per l'azione_geometrica_complessa

def score_function(score2,penal1, penal4):
	'''
	calcola lo score function di uno specifico layout 
	'''
	k1 = 10 #controllo per il peso degli extended	
	k3 = 10 #controlla la convessita'
	k6 = 5 #controlla il numero di extended introdotte
	score_function = (k1*score2)-((k3*penal1) + (k6*penal4))
	
	return score_function
	
	
	