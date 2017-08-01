'''
modulo che computa MCMC
'''
from util import valutazione as val
from object import Spazio as sp 
from util import predizionePlan_geometriche as pgeom
import os
import random
from util import disegna as dsg


def random_coin(p):
    unif = random.uniform(0,1)
  
    if unif>=p:
        return True
    else:
        return False

def computa_MCMC(stanza, plan_o, celle_di_altre_stanze, index_stanza,  xmin, ymin, xmax, ymax, path_obj):
	'''
	'''
	celle_out = plan_o.cellette_esterne
	celle_confinanti = pgeom.estrai_celle_confinanti_alle_parziali(plan_o, stanza) #insieme iniziale delle celle che potrei aggiungere
	#elimino quelle celle candidate che mi andrebbero ad eliminare una parete gia' vista
	celle_confinanti, celle_elimina_pareti = pgeom.elimina_celle_con_parete_vista(celle_confinanti, stanza)
	
	#---------------------------------PASSI----------------------------
	
	C_unite = []#insieme delle celle unite durante l'algoritmo	
	indice = 0
	n_iter =1
	count = 0#serve per calcolare la probabilita', piu' siamo avanti con le iterazioni meno probabilita' ho di aggiungere una cella.
	while(len(celle_confinanti)>0 and count<=2):
		print "stanza n ", index_stanza	
		
		for index_cella,cella in enumerate(set(celle_confinanti)):	
			#1) computo la funzione di costo iniziale del layout
			penal1_prima = val.penalita1(stanza)
			penal2_prima = val.penalita2(stanza, plan_o, celle_di_altre_stanze)
		
			penal4_prima = val.penalita4(stanza, plan_o, celle_di_altre_stanze)
			print "prima di aggiungere_pen1", penal1_prima
			print "prima di aggiungere_pen2", penal2_prima
			print "prima di aggiungere_pen4", penal4_prima
			
			cost_function_prima = val.cost_funzion(penal1_prima, penal2_prima, penal4_prima)
			b_e_prima = val.Boltzman_equation(cost_function_prima)
			print "costo_prima = ", cost_function_prima
			print "boltzman eq prima= ", b_e_prima
		
			#2)unisco la cella -----------------------------------------------------------
			sp.aggiungi_cella_a_spazio(stanza, cella, plan_o)
			#C_unite.append(cella)
			#crea cartella per visualizzare quello che stai facendo
			salva_risultati_parziali(plan_o, path_obj, index_stanza, index_cella + indice, xmin, ymin, xmax, ymax)
			#-----------------------------------------------------------------------------
		
			#3)ricomputo la funzione costo con la cella unita
			penal1_dopo= val.penalita1(stanza)
			penal2_dopo= val.penalita2(stanza, plan_o, celle_di_altre_stanze)
		
			penal4_dopo = val.penalita4(stanza, plan_o, celle_di_altre_stanze)
			print "dopo aver aggiunto_pen1", penal1_dopo
			print "dopo aver aggiunto_pen2", penal2_dopo
			print "dopo aver aggiunto_pen4", penal4_dopo
			cost_function_dopo = val.cost_funzion(penal1_dopo, penal2_dopo, penal4_dopo)
			b_e_dopo= val.Boltzman_equation(cost_function_dopo)
			print "costo_dopo = ", cost_function_dopo
			print "boltzman eq dopo= ", b_e_dopo
			
			n_iter +=1 #serve solo per salvare le immagini in sequenza
			
			#valuto con acceptance probability------------------------------------
			acc = min(1, b_e_prima/b_e_dopo)
			print "b_e_prima/b_e_dopo = ", b_e_prima/b_e_dopo
			print "acc ", acc
			if random_coin(acc):
				#accetto la mossa e vado avanti
				C_unite.append(cella)
			else:
				#non accetto la mossa
				sp.elimina_cella_da_spazio(stanza, cella, plan_o)
			
			
	
		if len(C_unite)>=0 :
			#le iterazioni successive vogliono come spazio delle soluzione tutte le celle confinanti a quelle appena aggiunte.
			celle_confinanti =[]
			celle_confinanti = pgeom.estrai_celle_esterne_confinanti_con_lista_celle(plan_o, C_unite)
			#elimino quelle celle candidate che mi andrebbero ad eliminare una parete gia' vista
			celle_confinanti, celle_elimina_pareti = pgeom.elimina_celle_con_parete_vista(celle_confinanti, stanza)
			#svuoto la lista
			C_unite = []
			
		indice = n_iter #serve solo per salvare le immagini in sequenza
		count += 1
		
		
def salva_risultati_parziali(plan_o, path_obj, index_stanza, index_cella, xmin, ymin, xmax, ymax):
	'''
	salva i risultati parziali
	'''
	SAVE_FOLDER = path_obj.filepath + '/dati_parziali_stanza_n'+str(index_stanza)
	if not os.path.exists(SAVE_FOLDER):
		os.mkdir(SAVE_FOLDER)
	dsg.disegna_spazi(plan_o.spazi, dsg.get_colors(plan_o.spazi), xmin, ymin, xmax, ymax,filepath = SAVE_FOLDER, savename = 'cella'+str(index_cella), format='png')
		

			