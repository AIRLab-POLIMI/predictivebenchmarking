'''
in questo modulo ci sono tutte le predizioni Geometriche.
'''
from object import Extended_segment as ext
from object import Segmento as sg
from object import Superficie as fc #prima si chiamava cella 
from object import Spazio as sp
from object import Plan as plan
import itertools
from util import valutazione as val
import copy
import random
				
def estrai_celle_confinanti_alle_parziali(plan_o, spazio_parziale):
	'''
	estrae le celle out confinanti a quelle celle parziali interne ad una stanza
	'''
	
	cellette_out = plan_o.cellette_esterne
	celle_confinanti = []
	for c in spazio_parziale.cells:
		for co in cellette_out:
			if fc.adiacenti(c.c,co.c):
				if c.parziale == True: #se la cella interna e' anche parziale, aggiungi la cella out alla lista delle confinanti
					celle_confinanti.append(co)
	return celle_confinanti

def estrai_celle_esterne_confinanti_con_lista_celle(plan_o, C_unite):
	'''
	crea una lista di celle adiacenti alle celle che fanno parte della lista C_unite 
	'''
	celle_out = plan_o.cellette_esterne
	celle_confinanti = []
	for c in set(C_unite):
		for co in celle_out:
			if fc.adiacenti(c.c,co.c):
				celle_confinanti.append(co)
	return celle_confinanti
	
	
def estrai_celle_supportate_da_extended_segmement(celle_confinanti, stanza, extended_segments):
	'''
	delle celle che fanno parte della lista delle celle_confinanti, 
	estraggo solo quelle che hanno tutti i lati che non toccano l'interno supportati da un extended segment(cioe' che l'extended segment deve toccare almeno una stanza)
	'''
	
	#per tutte le celle out che confinano con il bordo
	candidate = []
	for cella_conf in celle_confinanti:
		
		#estraggo le extended segment della cella_confinante
		extended_cella_out = ext.estrai_extended_segment_da_cella(cella_conf.c, extended_segments)
		
		for celle_st in stanza.cells:
			if fc.adiacenti(celle_st.c,cella_conf.c):
				if(fc.edge_comune(celle_st.c,cella_conf.c)[0].weight < 0.2):#il bordo in comune non deve essere supportato da segmenti
					edge_comuni = fc.edge_comune(celle_st.c,cella_conf.c) #ottengo la lista degli edge comuni alle 2 celle
					#seleziono le extended segment corrispondenti
					comuni = []
					for bordo in edge_comuni:
						comuni.append(ext.estrai_extended_segment_da_bordo_cella(bordo, extended_segments))
					
					extended_cella_out = list(set(extended_cella_out)-set(comuni))#tolgo dalle extended della cella out quelle che ha in comune con la cella interna
				
					#ora controllo che tutte le extend_segment trovate abbiano un supporto significativo 
				
					tutte_ok = True
					for e in extended_cella_out:
						if e.peso < 0.05: #se non e' coperto da un po' di segmentini allora l'intera cella non va bene.
							tutte_ok = False
					
				
					if tutte_ok == True:
						#cella_conf.set_celletta_parziale(True) #questo sicuramente no perche' questa cella non e' parziale
						#cella_conf.set_celletta_out(False)
						candidate.append(cella_conf)
							
	return 	candidate	
	
def elimina_celle_con_parete_vista(celle_confinanti, s):
	'''
	dalla lista delle celle confinanti alla stanza s ci potrebbero essere delle celle che mi fanno sparire una parete gia' vista dal laser.
	Non volgio tener conto di quelle celle.
	'''
	#candidate = celle_confinanti[:]#copio le celle confinanti come se fossero tutte candidate
	da_eliminare = []
	for cella_conf in celle_confinanti:
		for cella_st in s.cells:
			if fc.adiacenti(cella_st.c,cella_conf.c):
				# se la cella ha una parete in comune gia' vista allora non va bene
				if(fc.edge_comune(cella_st.c,cella_conf.c)[0].weight > 0.05): #metto un minimo di gioco per il rumore (era 0.005)
					#significa che ci sono dei segmenti visti
					#quindi se aggiungessi questa celle alla stanza eliminerei una parete che effettivamente era stata gia' osservata
					#candidate.remove(cella_conf)#la elimino dalla lista delle celle candidate
					da_eliminare.append(cella_conf)
	
	candidate = list(set(celle_confinanti)-set(da_eliminare))
	
	return candidate, da_eliminare
	

def elimina_celle_che_eliminerebbero_parete(plan_o, celle_confinanti, s):
	'''
	nella lista delle celle confinanti ad una stanza parziale, ci potrebbero essere delle celle che se venissero aggiunte andrebbero
	ad eliminare una parete gia' vista nelle prossimita', queste celle molto probabilmente non devono essere aggiunte, allora le elimino dall'insieme
	delle celle confinanti.
	'''
	#estraggo le celle delle altre stanze
	celle_di_altre_stanze = []
	for s2 in plan_o.spazi:
		if s2 !=s:
			for c in s2.cells:
				celle_di_altre_stanze.append(c)	
	
	#estraggo celle circostanti 
	celle_circostanti = celle_di_altre_stanze + plan_o.cellette_esterne #creo una lista delle celle circostanti ad una stanza
	#extended visti di una stanza parziale.
	b= sp.estrai_solo_extended_visti(s, plan_o.extended_segments, celle_circostanti)#estraggo solo le extended sicuramente viste
	tot_segment_visti = list(set(b))
	
	celle_da_eliminare = []
	for cella_conf in celle_confinanti:
		for cella_st in s.cells:
			if fc.adiacenti(cella_st.c,cella_conf.c):
				edge = fc.edge_comune(cella_st.c,cella_conf.c)[0] #estraggo l'edge in comune 
				#se l'edge in comune ha stesso coefficiente spaziale di uno degli extended visti, allora quella cella non va bene
				for ext in tot_segment_visti:
					if ext.cluster_spaziale == edge.cluster_spaziale:
						celle_da_eliminare.append(cella_conf)
	
	return list(set(celle_confinanti)-set(celle_da_eliminare))

def	elimina_celle_che_eliminerebbero_parete2(plan_o, celle_confinanti, s, elementi_livello_precedente):
	'''
	questo metodo e' molto simile al precendente ma ha senso usarlo solo per livelli sucessivi al primo, perche' va a 
	controllare se la cella che vorrei aggiungere all'insieme potebbe portarmi ad eliminare una cella 
	'''
	#estraggo le celle delle altre stanze
	celle_di_altre_stanze = []
	for s2 in plan_o.spazi:
		if s2 !=s:
			for c in s2.cells:
				celle_di_altre_stanze.append(c)	
	
	#estraggo celle circostanti 
	celle_circostanti = celle_di_altre_stanze + plan_o.cellette_esterne #creo una lista delle celle circostanti ad una stanza
	#extended visti di una stanza parziale.
	b= sp.estrai_solo_extended_visti(s, plan_o.extended_segments, celle_circostanti)#estraggo solo le extended sicuramente viste
	tot_segment_visti = list(set(b))
						
	elementi_livello_successivo = list(set(celle_confinanti)-set(elementi_livello_precedente))	
	celle_da_eliminare = []
	for cella_conf_l1 in elementi_livello_precedente:
		for cella_conf_l2 in elementi_livello_successivo:				
			if fc.adiacenti(cella_conf_l1.c,cella_conf_l2.c):
				#non solo le celle vicine alla stanza devono soddisfare la condizione precede, ma anche le celle dello stesso insieme di elementi
				edge = fc.edge_comune(cella_conf_l1.c,cella_conf_l2.c)[0] #estraggo l'edge in comune 
				#se l'edge in comune ha stesso coefficiente spaziale di uno degli extended visti, allora quella cella non va bene
				for ext in tot_segment_visti:
					if ext.cluster_spaziale == edge.cluster_spaziale:
						celle_da_eliminare.append(cella_conf_l2)
	
	return list(set(celle_confinanti)-set(celle_da_eliminare))
		

def estrai_spazio_delle_celle(stanza, plan_o, level):	
	'''
	permette di creare l'insieme delle possibili celle in input, da aggiungere alla stanza, fino al livello specificato in level.
	'''	
	elementi = estrai_celle_confinanti_alle_parziali(plan_o, stanza)#primo livello
	#delle celle canidate al primo livello non devo unire quelle che farebbero sparire una parete.
	elementi, ele_con_parete = elimina_celle_con_parete_vista(elementi, stanza)#TODO: valutare se in questo caso funziona
	#delle candidate al primo livello devo eliminare quelle che farebbero sparire una parete nelle vicinanze
	elementi = elimina_celle_che_eliminerebbero_parete(plan_o, elementi, stanza)
	
	for i in xrange(level):
		elementi_livello_precedente = elementi[:]
		elementi = elementi + estrai_celle_esterne_confinanti_con_lista_celle(plan_o, elementi)
		#delle celle canidate ai livelli successivi devo togliere quelle che farebbero sparire una parete.
		elementi, ele_con_parete = elimina_celle_con_parete_vista(elementi, stanza)#TODO: valutare se in questo caso funziona
		#delle candidate al ai livelli successivi devo eliminare quelle che farebbero sparire una parete nelle vicinanze
		elementi = elimina_celle_che_eliminerebbero_parete2(plan_o, elementi, stanza, elementi_livello_precedente)
		del elementi_livello_precedente

	
	return set(elementi)
	
def elimina_spazi_sul_bordo_da_candidati(elementi, plan_o):
	'''
	toglie dalla lista di elementi, tutti quegli elementi che toccano il bordo dell'immagine.
	questo perche' non ha senso aggiungere una cella che tocca il bordo dell'immagine
	''' 
	celle_bordo = plan.estrai_celle_sul_bordo(plan_o)
	
	return list(set(elementi)-set(celle_bordo))
	
		
def possibili_permutazioni(set):
	'''
	creo le possibili permutazioni che ho dell'intero insieme di celle che potrei aggiungere
	'''
	permutazioni = []
	for i in xrange(1,len(set)+1):
		lst = list(itertools.permutations(set, i))
		perm_iter = []
		for tuple in lst:
			row = []
			for i in tuple:
				row.append(i)
			permutazioni.append(row)
		if len(perm_iter)>0:
			permutazioni.append(perm_iter)

	return permutazioni
	

def aggiunge_celle_permutazione(permutazione, plan_o, stanza):
	'''
	aggiunge tutte le celle di un permutazione a plan_o. Una permutazione e' valida se aggiungendo le celle in ordine non trovo errori
	 
	'''
	for cella in permutazione:
		sp.aggiungi_cella_a_spazio(stanza, cella, plan_o)
	
	
	
def elimina_celle_permutazione(permutazione, plan_o, stanza):
	'''
	elimina le celle che una permutazione aveva aggiunto
	'''
	for cella in permutazione:
		sp.elimina_cella_da_spazio(stanza, cella, plan_o)
		
