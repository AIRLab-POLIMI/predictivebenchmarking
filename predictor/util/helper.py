from sklearn.cluster import DBSCAN
import numpy as np
import cv2
import math 
from util import disegna as dsg
import matplotlib.pyplot as plt

def cluster_img(image,m=20,e=5,savename='cluster',cluster_filter = 1) :

	count = np.zeros(256)
	cv2.imwrite("00_before.png",image)
	print image.shape

	# se e' grayscale la riconverto a colori
	if len(image.shape) == 2 :
		image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
		wi,he = image.shape
	else :
		wi,he,_=image.shape
	pixels = []

	for i in xrange(wi):
		for j in xrange(he):
			count[image[i,j]]+=1
			if image[i,j][0] == 0:
				pixels.append([i,j])

	db=DBSCAN(eps=e, min_samples=m).fit(pixels)
	labels=db.labels_
	print labels
	unique_labels=set(labels)
	colors = plt.cm.Spectral(np.linspace(0,1,len(unique_labels)))
	colormap =dict()
	for k,col in zip(unique_labels,colors):
		if k == -1 :
			col = [0,0,0,0]
		colormap[k]=col
	print "number of clusters ", len(unique_labels)
	# controllo quanti elementi ci sono in ogn cluster
	cluster_size = dict()
	cluster_dict = dict()
	for i in unique_labels :
		cluster_size[i] = 0
		# elenco dei pixel per ogni elemento
		cluster_dict[i] = []
	for muro, i in zip(pixels,range(len(pixels))):

		my_label = labels[i]
		cluster_size[my_label]+=1
		cluster_dict[my_label].append(muro)
		#plt.plot([muro[0]],[muro[1]], color=colormap[my_label])
		cc = colormap[my_label]
		color_r = int(255*cc[0])
		color_g = int(255*cc[1])
		color_b = int(255*cc[2])
		image[muro[0],muro[1]]= [color_r,color_g,color_b]
	print "CLUSTER SIZE"
	for i in cluster_size.keys():
		print i,":",cluster_size[i]
	# trovo i cluster piu popolosi
	cluster_values = cluster_size.values()
	cluster_values.sort()
	removed_clusters = cluster_values[:-cluster_filter]

	cv2.imwrite('00_'+str(savename)+'_'+str(m)+'.'+str(e)+ '.png',image)

	# restituisco tutti i pixel appartenenti ai cluster meno popolosi /spero che -1 sia tra loro 
	removed_pixel = []
	for i in unique_labels :
		if cluster_size[i] in removed_clusters :
			print "removed: ",i
			removed_pixel += cluster_dict[i]
	return removed_pixel
	'''
    count = np.zeros(256)
	pixels = []
	print thresh1.shape
	cv2.imwrite('000_thre.png',thresh1)
	for i in xrange(wi):
		for j in xrange(he):
			count[thresh1[i,j]]+=1
			if thresh1[i,j][0] == 0:
				pixels.append([i,j])
			else:
				img_c[i,j]=[0,0,0]
	e = 5
	m=20
	db=DBSCAN(eps=e, min_samples=m).fit(pixels)
	labels=db.labels_
	print labels
	unique_labels=set(labels)
	import matplotlib.pyplot as plt
	colors = plt.cm.Spectral(np.linspace(0,1,len(unique_labels)))
	colormap =dict()
	for k,col in zip(unique_labels,colors):
		if k == -1 :
			col = [0,0,0,0]
		colormap[k]=col
	print colormap[1]
	for muro, i in zip(pixels,range(len(pixels))):

		my_label = labels[i]
		#plt.plot([muro[0]],[muro[1]], color=colormap[my_label])
		cc = colormap[my_label]
		color_r = int(255*cc[0])
		color_g = int(255*cc[1])
		color_b = int(255*cc[2])
		img_c[muro[0],muro[1]]= [color_r,color_g,color_b]
	cv2.imwrite('00_boh_'+str(e)+'.'+str(m)+ '.png',img_c)
	
	exit()
	'''