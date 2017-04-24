import matplotlib.pyplot as plt
import sys
import math
import collections
from mpl_toolkits.mplot3d import Axes3D
#from cgkit.cgtypes import *
import numpy as np

def rotate(origin, point, angle):
	'''
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    '''

	ox, oy = origin
	px, py = point

	qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
	qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
	return qx, qy

def plotSlam(slam):
	file2=open(slam,'r')

	x=[]
	y=[]

	for line in file2:
		words = line.split(" ")
		x.append(words[5])
		y.append(words[6])

	file2.close()
	plt.plot(x,y)

def plotGroundTruth():
	file=open(sys.argv[1],'r')

	xGT=[]
	yGT=[]

	for line in file:
		words = line.split(" ")
		xGT.append(words[1])
		yGT.append(words[2])

	file.close()

def plot():
	file=open(sys.argv[1],'r')
	#fileRot=open('office_d-5min-centered.log','w')
	#fig=plt.figure()
	#ax=fig.gca(projection='3d')

	xGT=[]
	yGT=[]
	#zGT=[]

	for line in file:
		words = line.split(" ")
		#rot=rotate((float(words[1]),float(words[2])),(0,0),0.785398163397)
		xGT.append(float(words[1]))
		yGT.append(float(words[2]))
		#zGT.append(float(words[0]))
		#fileRot.write(words[0]+' '+str((float(words[1])+25))+' '+str((float(words[2])+25))+' '+words[3])

	file.close()
	#fileRot.close()
	'''
	fileOdom=open(sys.argv[2],'r')

	xOdom=[]
	yOdom=[]

	for line in fileOdom:
		words = line.split(" ")
		xOdom.append(float(words[1]))
		yOdom.append(float(words[2]))

	fileOdom.close()
	'''
	file2=open(sys.argv[2],'r')
	#file2Scaled=open('modifiedmymap2.log','w')

	x=[]
	y=[]
	#z=[]
	#i=0

	for line in file2:
		words = line.split(" ")
		x.append(float(words[5]))
		y.append(float(words[6]))
		'''
		#z.append(float(words[8]))
		if 4000 <= i <= 5000:
			file2Scaled.write('FLASER 0 0.0 0.0 0.0 '+str(float(words[5])+10)+' '+str(float(words[6])+10)+' '+words[7]+' '+words[8])
		else:
			file2Scaled.write('FLASER 0 0.0 0.0 0.0 '+str(float(words[5]))+' '+str(float(words[6]))+' '+words[7]+' '+words[8])
		i+=1
		'''

	#ax.plot(x,y,z,label='gmapping')
	#ax.plot(xGT,yGT,zGT,label='ground truth')
	#ax.legend()

	file2.close()
	#file2Scaled.close()
	plt.plot(xGT,yGT,'g',x,y,'r')
	plt.show()
	#plt.savefig('trajectories.pdf')

def plotRelationsTR(relations):
	relationsFile=open(relations,'r')
	#orderedRelationsFile=open('acesOrdered.relations','w')
	times={}
	x_vect=[]
	y_vect=[]
	x=0
	y=0
	theta=0
	#ax=plt.axes()
	vec=np.array([[0],[0],[0],[1]])
	x_vect.append(x)
	y_vect.append(y)

	for line in relationsFile:
		words=line.split(' ')
		times[float(words[0])]=words

	sortedtimes=collections.OrderedDict(sorted(times.items()))
	for time in sortedtimes:
		#orderedRelationsFile.write(sortedtimes[time][0] + ' ' + sortedtimes[time][1] + ' ' + sortedtimes[time][2] + ' ' + sortedtimes[time][3] + ' ' + sortedtimes[time][4] + ' ' + sortedtimes[time][5] + ' ' + sortedtimes[time][6] + ' ' +sortedtimes[time][7]
		if float(sortedtimes[time][1])-float(sortedtimes[time][0]) < 50 and float(sortedtimes[time][1]) > float(sortedtimes[time][0]):

			current_x = float(sortedtimes[time][2])
			current_y = float(sortedtimes[time][3])

			


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


			M = m_translation_back_to_current * m_rotation * m_translation_to_origin * m_translation 

			'''
			print m_rotation
			print '\n'
			print m_translation
			print '\n'
			print m_rotation * m_translation
			print '\n'
			print m_translation * m_rotation
			print '\n'
			print m_rotation * m_translation * vec
			print '\n'
			print m_translation * m_rotation * vec
			print '\n'
			print m_translation_back_to_current
			print '\n'
			print m_translation_to_origin
			print '\n'
			print M 
			print '\n'
			'''
	
			vec = M * vec

			x=vec[0,0]
			y=vec[1,0]

			x_vect.append(x)
			y_vect.append(y)

			theta += float(sortedtimes[time][7])
			
			
			'''

			x += current_x
			y += current_y

			x += float(current_x*math.cos(theta)-current_y*math.sin(theta)) 
			y += float(current_x*math.sin(theta)+current_y*math.cos(theta)) 

			x_vect.append(x)
			y_vect.append(y)

			#update theta
			theta += float(sortedtimes[time][7])
			if theta > (math.pi):
				theta -= (2*math.pi)
			elif theta < (-math.pi):
				theta += (2*math.pi)
			'''

	relationsFile.close()

	plt.plot(x_vect,y_vect,'r')

def plotRelationsRT(relations):
	relationsFile=open(relations,'r')
	times={}
	x_vect=[]
	y_vect=[]
	x=0
	y=0
	theta=0
	vec=np.array([[0],[0],[0],[1]])
	x_vect.append(x)
	y_vect.append(y)

	for line in relationsFile:
		words=line.split(' ')
		times[float(words[0])]=words

	sortedtimes=collections.OrderedDict(sorted(times.items()))
	for time in sortedtimes:
		if float(sortedtimes[time][1])-float(sortedtimes[time][0]) < 50 and float(sortedtimes[time][1]) > float(sortedtimes[time][0]):

			current_x = float(sortedtimes[time][2])
			current_y = float(sortedtimes[time][3])
			theta += float(sortedtimes[time][7])	
			print theta


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


			M = m_translation_back_to_current * m_rotation * m_translation_to_origin * m_translation

			print M 
	
			vec = M * vec

			x=vec[0,0]
			y=vec[1,0]

			x_vect.append(x)
			y_vect.append(y)
			

	relationsFile.close()

	plt.plot(x_vect,y_vect,'g')

if __name__=='__main__':	
	plotRelationsRT(sys.argv[1])
	#plotRelationsTR(sys.argv[1])
	#plotSlam(sys.argv[2])
	plt.show()