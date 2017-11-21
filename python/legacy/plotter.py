import matplotlib.pyplot as plt
import sys
import math
import collections
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

global_x = 60
global_y = 0

def plotSlam(slam):
	global global_x
	global global_y
	file2=open(slam,'r')

	x=[]
	y=[]

	for line in file2:
		words = line.split(" ")
		x.append(float(words[5]))
		y.append(float(words[6]))

	file2.close()
	plt.plot(x,y,'r')
	# find first non-zero coordinate pair and use that as a reference


def plotGroundTruth(groundtruth):
	global global_x
	global global_y
	file=open(groundtruth,'r')

	xGT=[]
	yGT=[]

	found = False
	for line in file:
		words = line.split(" ")
		xGT.append(words[1])
		yGT.append(words[2])
		'''
		if (float(words[1])>0) and not found:
			global_x = float(words[1])
			global_y = float(words[2])
			found = True
			print "found"
			print global_x
			print global_y
		'''

	file.close()
	plt.plot(xGT,yGT,'g')

def plotRelationsRT(relations):
	relationsFile=open(relations,'r')
	times={}
	x_vect=[]
	y_vect=[]
	dx=0
	dy=0
	dtheta=0
	#print global_x
	#print global_y
	x = global_x
	y = global_y
	theta = 0
	vec=np.array([[global_x],[global_y],[0.0],[1.0]])
	x_vect.append(x)
	y_vect.append(y)
	i = 0
	for line in relationsFile:
		words=line.split(' ')
		times[float(words[0])]=words
    # strong assumption: once ordered, they are contiguous 
	sortedtimes=collections.OrderedDict(sorted(times.items()))
	for time in sortedtimes:
		if float(sortedtimes[time][1])-float(sortedtimes[time][0]) < 50 and float(sortedtimes[time][1]) > float(sortedtimes[time][0]):

			'''current_x = float(sortedtimes[time][2])
			current_y = float(sortedtimes[time][3])
			theta += float(sortedtimes[time][7])	


			m_translation=np.matrix(((1,0,0,current_x),
									(0,1,0,current_y),
									(0,0,1,0),
									(0,0,0,1)))

			m_translation_to_origin=np.matrix(((1,0,0,-x),
												(0,1,0,-y),
												(0,0,1,0),
												(0,0,0,1)))

			m_translation_back_to_current=np.matrix(((1,0,0,x),
													(0,1,0,y),
													(0,0,1,0),
													(0,0,0,1)))

			m_rotation=np.matrix(((math.cos(theta),-math.sin(theta),0,0),
									(math.sin(theta),math.cos(theta),0,0),
									(0,0,1,0),
									(0,0,0,1)))


			M = m_translation_back_to_current * m_rotation * m_translation_to_origin * m_translation'''
			dx = float(sortedtimes[time][2])
			dy = float(sortedtimes[time][3])
			dtheta = float(sortedtimes[time][7])
			theta+=dtheta
			dxp = math.cos(theta)*dx-math.sin(theta)*dy
			dyp = math.sin(theta)*dx+math.cos(theta)*dy

			
			M = np.matrix(((1,0,0,dxp),
                           (0,1,0,dyp),
                           (0,0,1,0),
                           (0,0,0,1)))
	
			vec = M * vec

			#x=vec[0,0]
			#y=vec[1,0]
			#print vec
			x_vect.append(np.asarray(vec[0]).flatten()[0])
			y_vect.append(np.asarray(vec[1]).flatten()[0])
			
		i+=1
		#if (i>30): break

	relationsFile.close()
	#print x_vect
	plt.plot(x_vect,y_vect,'b')

if __name__=='__main__':	
	#plotGroundTruth(sys.argv[1])
	#plotSlam(sys.argv[2])
	plotRelationsRT(sys.argv[1])
	plt.show()
