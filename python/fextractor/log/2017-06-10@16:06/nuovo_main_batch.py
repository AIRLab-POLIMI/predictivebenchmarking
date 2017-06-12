'''
main tesi
'''
from __future__ import division
import numpy as np
import util.layout as lay
import util.GrafoTopologico as gtop
import util.transitional_kernels as tk
import util.MappaSemantica as sema
from util import pickle_util as pk
import pickle
import time
from util import accuracy as ac


def start_main(minLateralSeparation, minVal, maxVal, rho, theta, thresholdHough, minLineLenght, maxLineGap, eps, minPts, h, minOffset, metricMap, outLayout_pickle_path, outTopologicalGraph_pickle_path,nome_gt,filepath,cv2thresh,flip_dataset=True, diagonali = True, m= 20, metodo_classificazione_celle = True):
	
	#----------------------------LAYOUT DELLE STANZE-----------------------------------
	#layout delle stanze
	#(stanze, clustersCelle, estremi, colori, spazi) = lay.get_layout(metricMap, minVal, maxVal, rho, theta, thresholdHough, minLineLenght, maxLineGap, eps, minPts, h, minOffset, minLateralSeparation,filepath,cv2thresh)
	(stanze, clustersCelle, estremi, colori, spazi) = lay.get_layout(metricMap, minVal, maxVal, rho, theta, thresholdHough, minLineLenght, maxLineGap, eps, minPts, h, minOffset, minLateralSeparation,filepath,cv2thresh, diagonali, m, metodo_classificazione_celle)

	print "Inizio a calcolare metriche"
	ac.calcola_accuracy(nome_gt,estremi,stanze,metricMap,filepath, flip_dataset)
	print "Fine calcolare metriche"
	
	#creo i file pickle per il layout delle stanze
	#print("creo pickle layout")
	#pk.crea_pickle((stanze, clustersCelle, estremi, colori, spazi), outLayout_pickle_path)
	#-----------------------------------------------------------------------------------
	
	#------------------------------GRAFO TOPOLOGICO-------------------------------------
	
	#in questo momento per non andare ad eseguire interamente il programma uso il pickle creato dentro il file layout_stanze, che contiene (stanze, clustersCelle, estremi, colori)
	'''pkl_file = open( outLayout_pickle_path, 'rb')
	data1 = pickle.load(pkl_file)
	stanze = data1[0]
	clustersCelle = data1[1]
	estremi = data1[2]
	print(estremi)
	colori = data1[3]
	spazi = data1[4]
	'''
	#costruisco il grafo 
	(G, pos, collegate, doorsVertices) = gtop.get_grafo(metricMap, stanze, estremi, colori)
	
	#creo i file pickle per il grafo topologico
	#print("creo pickle grafoTopologico")
	#pk.crea_pickle((stanze, clustersCelle, estremi, colori), outTopologicalGraph_pickle_path)
	
	#in questa fase il grafo non e' ancora stato classificato con le label da dare ai vai nodi.
	#-----------------------------------------------------------------------------------
	
	#leggo il pickle del grafo (da togliere). da qui leggo le strutture che mi servono.
	'''
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
	'''
	#in questa fase classifico i nodi del grafo e conseguentemente anche quelli della mappa.
	
	#gli input di questa fase non mi sono ancora molto chiari 
	#per ora non la faccio poi se mi serve la copio/rifaccio, penso proprio sia sbagliata.

	#stanze ground truth
	(stanze_gt, nomi_stanze_gt, RC, RCE, FCES, spaces, collegate_gt) = sema.get_stanze_gt(nome_gt, estremi)

	#corrispondenze tra gt e segmentate (backward e forward)
	(indici_corrispondenti_bwd, indici_gt_corrispondenti_fwd) = sema.get_corrispondenze(stanze,stanze_gt)

	#creo xml delle stanze segmentate
	id_stanze = sema.crea_xml(nomeXML,stanze,doorsVertices,collegate,indici_gt_corrispondenti_fwd,RCE,nomi_stanze_gt)

	#parso xml creato, va dalla cartella input alla cartella output/xmls, con feature aggiunte
	xml_output = sema.parsa(dataset_name, nomeXML)


	#classifico
	predizioniRCY = sema.classif(dataset_name,xml_output,'RC','Y',30)
	predizioniRCN = sema.classif(dataset_name,xml_output,'RC','N',30)
	predizioniFCESY = sema.classif(dataset_name,xml_output,'RCES','Y',30)
	predizioniFCESN = sema.classif(dataset_name,xml_output,'RCES','N',30)

	#creo mappa semantica segmentata e ground truth e le plotto assieme
	
	sema.creaMappaSemantica(predizioniRCY, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, RC, estremi, colori)
	plt.show()
	sema.creaMappaSemantica(predizioniRCN, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, RC, estremi, colori)
	plt.show()
	sema.creaMappaSemantica(predizioniFCESY, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, FCES, estremi, colori)
	plt.show()
	sema.creaMappaSemantica(predizioniFCESN, G, pos, stanze, id_stanze, estremi, colori, clustersCelle, collegate)
	sema.creaMappaSemanticaGt(stanze_gt, collegate_gt, FCES, estremi, colori)
	plt.show()
	'''
	#-----------------------------------------------------------------------------------
	
	
	print "to be continue..."
	#TODO
	

def main():
	start = time.time()
	#-------------------PARAMETRI-------------------------------------------------------
	
	#distanza massima in pixel per cui 2 segmenti con stesso cluster angolare sono considerati appartenenti anche allo stesso cluster spaziale 
	minLateralSeparation = 7
	cv2thresh = 150

	#parametri di Canny
	minVal = 90
	maxVal = 100
	
	#parametri di Hough
	rho = 1
	theta = np.pi/180
	thresholdHough = 20
	minLineLength = 7
	maxLineGap = 3
	
	#parametri di DBSCAN
	eps = 0.85#1.5#0.85
	minPts = 1
	
	#parametri di mean-shift
	h = 0.023
	minOffset = 0.00001
	
	#path output pickle
	outLayout_pickle_path = './data/OUTPUT/pickle/layout_stanze.pkl'
	outTopologicalGraph_pickle_path = './data/OUTPUT/pickle/grafo_topologico.pkl'
	
	
	
	#-----------------------------MAPPA METRICA--------------------------------

	#immagine della mappa metrica
	#metricMap = './data/INPUT/layout_images/fake2.png'
	#metricMap = './data/INPUT/IMGs/SURVEY/NLB.png'
	#metricMap = './data/INPUT/IMGs/SURVEY/office_d.png'

	metricMap = './data/INPUT/IMGs/SURVEY/Freiburg79_scan.png'
	#metricMap = './data/INPUT/IMGs/SURVEYGT/lab_ipa.png'
	
	#metricMap = './data/INPUT/IMGs/SURVEY/office_i.png'
	#metricMap = './data/INPUT/IMGs/SURVEY/Freiburg52_scan.png'
	
	#metricMap = './data/INPUT/IMGs/SCHOOL/henderson_high_school_updated.png'
	#metricMap = './data/INPUT/IMGs/SCHOOL/scuola_sconosciuta_3_updated.png'
	#metricMap = './data/INPUT/IMGs/SCHOOL/cunningham2f_updated.png'
	#metricMap = './data/INPUT/IMGs/SURVEY/lab_a_scan.png'


	#----------------------------NOMI FILE DI INPUT----------------------------
	#xml ground truth corrispondente
	#nome_gt = './data/INPUT/XMLs/SURVEY/NLB.xml'
	#nome_gt = './data/INPUT/XMLs/SURVEY/office_d.xml'
	#nome_gt = './data/INPUT/XMLs/SURVEYGT/lab_ipa.xml'
	#nome_gt = './data/INPUT/XMLs/SURVEY/Freiburg52_scan.xml'
	#nome_gt = './data/INPUT/XMLs/SCHOOL/scuola_sconosciuta_3_updated.xml'
	#nome_gt = './data/INPUT/XMLs/SCHOOL/cunningham2f_updated.xml'
	#nome_gt = './data/INPUT/XMLs/SURVEY/lab_a_scan.xml'


	
	nome_gt = './data/INPUT/XMLs/SURVEY/Freiburg79_scan.xml'

	
	#nome_gt = './data/INPUT/XMLs/SURVEY/office_i.xml'
	#nome_gt = './data/INPUT/XMLs/SCHOOL/henderson_high_school_updated.xml'
	#nome_gt = './data/INPUT/XMLs/SURVEY/Freiburg52_scan.xml'

	# CARTELLA DOVE SALVO
	filepath = './'

	#xml creato da me, relativo alle stanze segmentate
	nomeXML = "./Input/miei/b.xml"
	#dataset usato per le label semantiche
	dataset_name = 'school'

	
	#-------------------ESECUZIONE------------------------------------------------------
	#flip_dataset = False #questo lo metti a true se la mappa che stai guardando e' di SURVEY
	#metodo_di_classificazione_celle = True significa usare il metodo di matteo, metodo_di_classificazione_celle = False significa usare quello di Valerio. 
	start_main(minLateralSeparation, minVal, maxVal, rho, theta, thresholdHough, minLineLength, maxLineGap, eps, minPts, h, minOffset, metricMap, outLayout_pickle_path, outTopologicalGraph_pickle_path,nome_gt,filepath,cv2thresh, flip_dataset=True, diagonali = True, m = 20, metodo_classificazione_celle = True)
	#-------------------TEMPO IMPIEGATO-------------------------------------------------
	fine = time.time()
	elapsed = fine-start
	print "la computazione ha impiegato %f secondi" % elapsed

if __name__ == '__main__':
    main()	