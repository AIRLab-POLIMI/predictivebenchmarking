# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt

def bw(immagine):
	for x in range(immagine.shape[0]):
		for y in range(immagine.shape[1]):
			if immagine[x][y] < 128:
				immagine[x][y] = 1 #nero
			else:
				immagine[x][y] = 0 #bianco
	return immagine

def get_points(immagine):
	points = []
	for x in range(immagine.shape[0]):
		for y in range(immagine.shape[1]):
			if immagine[x][y] == 1:
				points.append( (np.array([y,x])).astype(float) )
	return points


def elimino_colori(soglia, immagine):
	b,g,r = cv2.split(immagine)
	w, h, channels = immagine.shape
	for i in range(w):
		for j in range(h):
			if(r[i, j] < 160 and g[i, j] < 160 and b[i, j] < 160):
				if(vicini(int(r[i,j]),int(g[i,j]),int(b[i,j]),soglia)):
					r[i,j]=0
					g[i,j]=0
					b[i,j]=0
	img = cv2.merge((b,g,r))
	plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
	plt.show()
	
	#trasformo in scala di grigi
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#tutto cio' che non e' propriamente nero lo metto bianco (elimino quindi tutti i colori, frecce verdi ecc)
	ret,thresh = cv2.threshold(gray,10,255,cv2.THRESH_BINARY_INV)
	return thresh


def vicini(r,g,b,soglia):
	'''
	restituisce True se i valori r,g,b sono tutti e 3 vicini entro una certa soglia, False altrimenti.
	'''
	if (abs(r-g)<soglia) and (abs(r-b)<soglia) and (abs(g-b)<soglia) :
		return True
	return False


def trova_contorno(t,m,edges_canny,file_name):

	'''
	hough su canny, plotto le hough lines su un'immagine bianca, applico la funzione cv2.findContours con retrieval_mode = external per trovare i contorni esterni. Se i contorni esterni sono più di 1, devo riapplicare la hough aumentando la threshold, in modo da rendere unico il contorno esterno.
	'''
	hough_contorni = cv2.HoughLinesP(edges_canny,1,np.pi/180,threshold=t,minLineLength=1,maxLineGap=m)
	if cv2.__version__[0] == '3' :
		hough_contorni = [i[0]for i in hough_contorni]
	elif cv2.__version__[0] == '2' :
		hough_contorni = hough_contorni[0]
	else :
		raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*')

	#creo immagine bianca su cui plottare le hough lines
	img4 = cv2.imread(file_name,0)
	ret,bianca = cv2.threshold(img4,255,255,cv2.THRESH_BINARY_INV)
	bianca2 = bianca.copy()
	#plotto le hough lines sull'immagine bianca
	for x1,y1,x2,y2 in hough_contorni:
		cv2.line(bianca2,(x1,y1),(x2,y2),(0,0,0),2)

	ret,bianca2 = cv2.threshold(bianca2,253,255,cv2.THRESH_BINARY_INV)
	if cv2.__version__[0] == '3' :
		img_copy, contours, hierarchy = cv2.findContours(image = bianca2.copy(), mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)
	elif cv2.__version__[0] == '2' :
		#trovo il contorno esterno
		contours, hierarchy = cv2.findContours(bianca2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	else :
		raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*')

	while(len(contours)!=1): #se il contorno esterno trovato non è unico
		t+=1 #aumento la threshold

		# COntrollo che le Hough funzionino bene compatibilmente alla versione di OpenCV
		hough_contorni = cv2.HoughLinesP(edges_canny,1,np.pi/180,threshold=t,minLineLength=1,maxLineGap=m)
		if cv2.__version__[0] == '3' :
			hough_contorni = [i[0]for i in hough_contorni]
		elif cv2.__version__[0] == '2' :
			hough_contorni = hough_contorni[0]
		else :
			raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*')

		bianca2 = bianca.copy()
		for x1,y1,x2,y2 in hough_contorni:
			cv2.line(bianca2,(x1,y1),(x2,y2),(0,0,0),2)
		ret,bianca2 = cv2.threshold(bianca2,253,255,cv2.THRESH_BINARY_INV)

		#Controllo che findcontours funzioni bene con openCvDiverse
		if cv2.__version__[0] == '3' :
			img_copy, contours, hierarchy = cv2.findContours(image = bianca2.copy(), mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)
		elif cv2.__version__[0] == '2' :
			#trovo il contorno esterno
			contours, hierarchy = cv2.findContours(bianca2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		else :
			raise EnvironmentError('Opencv Version Error. You should have OpenCv 2.* or 3.*')
	return (hough_contorni,contours)
