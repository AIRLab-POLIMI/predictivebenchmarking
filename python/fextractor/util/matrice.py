from __future__ import division
from object import Superficie as fc
import numpy as np
import math


def crea_matrice_l(facce, sigma, val):
	'''
	crea la matrice L cosi' come definita nel paper di Mura
	'''
	riga = []
	#creo la matrice con solo la prima riga
	faccia = facce[0]
	for altra_faccia in facce:
		adj = fc.adiacenti(faccia,altra_faccia)
		if(faccia == altra_faccia):
			#print("stessa faccia")
			val = 1
		else:
			#print("non sono la stessa faccia")
			if (adj):
				#print("adiacenti")
				e = fc.edge_comune(faccia,altra_faccia)
				w = e[0].weight
				val = math.exp(-w/sigma)
			else:
				#print("non adiacenti")
				val = 0
		riga.append(val)

	matrice_l = np.matrix([riga])
	del riga[:]


	for faccia in facce[1:]:
		for altra_faccia in facce:
			adj = fc.adiacenti(faccia,altra_faccia)
			if(faccia == altra_faccia):
				#print("stessa faccia")
				val = 1
			else:
				#print("non sono la stessa faccia")
				if (adj):
					#print("adiacenti")
					e = fc.edge_comune(faccia,altra_faccia)
					w = e[0].weight
					val = math.exp(-w/sigma)
				else:
					#print("non adiacenti")
					val = 0
			riga.append(val)
		matrice_l = np.vstack([matrice_l,riga])
		del riga[:]
	
	return matrice_l


def crea_matrice_d(matrice_l):
	'''
	crea la matrice D cosi' come definita nel paper di Mura
	'''
	vett = []
	for row in matrice_l:
		vett.append(row.sum())
	matrice_d = np.asmatrix(np.diag(vett))
	return matrice_d


def simmetrizza(M) :
	'''
	rende simmetrica la matrice M in modo da darla in input a dbscan
	'''
	if type(M) == np.matrix:
		M = np.array(M)
	[r,c] = M.shape
	M2 = np.copy(M)
	for i in xrange(r) :
		for j in xrange(i,c) :
			M2[i,j] = (M[i,j] + M[j,i]) /2
			M2[j,i] = M2[i,j]
	return M2


def print_matrix(M) :
	'''
	stampa in modo appropriato la matrice passata come parametro
	'''
	if type(M) == np.matrix:
		M = np.array(M)
	[r,c] = M.shape
	for i in xrange(r) :
		line = str()
		for j in M[i]:
			line += "%.3f"%j + ', '
			#line+= str("{0:2f}".format(M[i,j]))+' ,'
		line = line[:-2]
		print line
