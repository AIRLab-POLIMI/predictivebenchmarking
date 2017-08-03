'''
main tesi
'''
from __future__ import division
import numpy as np
import util.layout as lay
import util.GrafoTopologico as gtop
import util.transitional_kernels as tk

from util import pickle_util as pk
import parameters as par
import pickle
import datetime as dt
import os
import shutil
import glob


def start_main(minLateralSeparation, minVal, maxVal, rho, theta, thresholdHough, minLineLenght, maxLineGap, eps, minPts, h, minOffset, metricMap, outLayout_pickle_path, outTopologicalGraph_pickle_path, SAVE_FOLDER, LOGFILE):
	
	#----------------------------LAYOUT DELLE STANZE-----------------------------------
	#layout delle stanze
	(stanze, clustersCelle, estremi, colori, spazi) = lay.get_layout(metricMap, minVal, maxVal, rho, theta, thresholdHough, minLineLenght, maxLineGap, eps, minPts, h, minOffset, minLateralSeparation)

	
	#creo i file pickle per il layout delle stanze
	print("creo pickle layout")
	pk.crea_pickle((stanze, clustersCelle, estremi, colori, spazi), outLayout_pickle_path)
	#salvo i pickle nella cartella di log
	split_path = metricMap.split('/')
	pickle_name = split_path[len(split_path)-1]
	pickle_name = pickle_name.split('.png')[0] #splitto il path dell'immagine e prendo il nome dell'immagine senza l'estensione
	#salvo le operazioni fatte sul file di log
	print >>LOGFILE, "layout creto per la mappa: ", pickle_name
	print >>LOGFILE, "pickle layout creto per la mappa: ", pickle_name
	shutil.copy(outLayout_pickle_path, SAVE_FOLDER+'/layout_stanze_'+pickle_name+'.pkl')
	
	#-----------------------------------------------------------------------------------
	'''
	#------------------------------GRAFO TOPOLOGICO-------------------------------------
	
	#in questo momento per non andare ad eseguire interamente il programma uso il pickle creato dentro il file layout_stanze, che contiene (stanze, clustersCelle, estremi, colori)
	pkl_file = open( outLayout_pickle_path, 'rb')
	data1 = pickle.load(pkl_file)
	stanze = data1[0]
	clustersCelle = data1[1]
	estremi = data1[2]
	print(estremi)
	colori = data1[3]
	spazi = data1[4]
	
	#costruisco il grafo 
	(G, pos, collegate, doorsVertices) = gtop.get_grafo(metricMap, stanze, estremi, colori)
	
	#creo i file pickle per il grafo topologico
	print("creo pickle grafoTopologico")
	pk.crea_pickle((stanze, clustersCelle, estremi, colori), outTopologicalGraph_pickle_path)
	
	#in questa fase il grafo non e' ancora stato classificato con le label da dare ai vai nodi.
	#-----------------------------------------------------------------------------------
	
	#leggo il pickle del grafo (da togliere). da qui leggo le strutture che mi servono.
	pkl_file2 = open( outTopologicalGraph_pickle_path, 'rb')
	data2 = pickle.load(pkl_file2)
	G = data2[0]
	pos = data2[1]
	collegate = data2[2]
	doorsVertices = data2[3]
	'''
	#-------------------------prova transitional kernels--------------------------------
	
	
	#splitto una stanza e restituisto la nuova lista delle stanze
	#stanze, colori = tk.split_stanza_verticale(2, stanze, colori,estremi) 
	#stanze, colori = tk.split_stanza_orizzontale(3, stanze, colori,estremi)
	#stanze, colori = tk.slit_all_cell_in_room(spazi, 1, colori, estremi) #questo metodo e' stato fatto usando il concetto di Spazio, dunque fai attenzione perche' non restituisce la cosa giusta.
	#stanze, colori = tk.split_stanza_reverce(2, len(stanze)-1, stanze, colori, estremi) #questo unisce 2 stanze precedentemente splittate, non faccio per ora nessun controllo sul fatto che queste 2 stanze abbiano almeno un muro in comune, se sono lontani succede un casino

	
	#-----------------------------------------------------------------------------------

	
	#-------------------------MAPPA SEMANTICA-------------------------------------------
	#in questa fase classifico i nodi del grafo e conseguentemente anche quelli della mappa.
	
	#gli input di questa fase non mi sono ancora molto chiari 
	#per ora non la faccio poi se mi serve la copio/rifaccio, penso proprio sia sbagliata.
	
	#-----------------------------------------------------------------------------------
	
	
	print "to be continue..."
	#TODO
	

def main():
		
	#-----------------------------MAPPA METRICA--------------------------------
	DATASET_Immagini = 'layout_immages'
	DATASET_XML_GT = 'XML_GT'
	DATASET_XML_generati ='XML_generati' 
	
	PKL_FOLDER = os.path.join( par.input_dataset_folder, DATASET_Immagini)#in questo momento sto usando le immagini nella cartella old  
	our_time = str(dt.datetime.now())[:-10].replace(' ','@')
	SAVE_FOLDER = os.path.join('./log', our_time)
	if not os.path.exists(SAVE_FOLDER):
		os.mkdir(SAVE_FOLDER)
	SAVE_LOGFILE = SAVE_FOLDER+'/log.txt'
	    
	with open(SAVE_LOGFILE,'w+') as LOGFILE:
		print "AZIONE", par.AZIONE
		print >>LOGFILE, "AZIONE", par.AZIONE
		shutil.copy('./main.py',SAVE_FOLDER+'/nuovo_main_batch.py') #ricreo il main, da modificare dato che voglio creare il file dei parametri
		
		if par.AZIONE == 'batch':
			for metricMap in glob.iglob(os.path.join(PKL_FOLDER, "*.png")):
				start_main(par.minLateralSeparation, par.minVal, par.maxVal, par.rho, par.theta, par.thresholdHough, par.minLineLenght, par.maxLineGap, par.eps, par.minPts, par.h, par.minOffset, metricMap, par.outLayout_pickle_path, par.outTopologicalGraph_pickle_path, SAVE_FOLDER, LOGFILE)
			LOGFILE.flush()
		elif par.AZIONE == 'mappa_singola':
			#immagine della mappa metrica presa singolarmente
			metricMap = './data/INPUT/old/layout_immages/b_doors.png'
			start_main(par.minLateralSeparation, par.minVal, par.maxVal, par.rho, par.theta, par.thresholdHough, par.minLineLenght, par.maxLineGap, par.eps, par.minPts, par.h, par.minOffset, metricMap, par.outLayout_pickle_path, par.outTopologicalGraph_pickle_path, SAVE_FOLDER, LOGFILE)
			LOGFILE.flush()
			
		print "SAVING ...."
		print "ARCHIVING"
		     
		shutil.make_archive(SAVE_FOLDER,'tar',SAVE_FOLDER)
		shutil.rmtree(SAVE_FOLDER)


if __name__ == '__main__':
    main()	