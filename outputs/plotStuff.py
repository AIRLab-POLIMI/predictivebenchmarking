import matplotlib.pyplot as plt
import sys
import math
import collections
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

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

def plotOdom(odom):
	file=open(odom,'r')

	xOdom=[]
	yOdom=[]

	for line in file:
		words = line.split(" ")
		if words[0] == "ODOM":
			xOdom.append(words[1])
			yOdom.append(words[2])

	file.close()
	plt.plot(xOdom,yOdom,'y')

def plotSlam(slam):
	file2=open(slam,'r')

	x=[]
	y=[]

	for line in file2:
		words = line.split(" ")
		x.append(words[5])
		y.append(words[6])

	file2.close()
	plt.plot(x,y,'r')

def plotGroundTruth(groundtruth):
	file=open(groundtruth,'r')

	xGT=[]
	yGT=[]

	for line in file:
		words = line.split(" ")
		xGT.append(words[1])
		yGT.append(words[2])

	file.close()
	plt.plot(xGT,yGT,'g')

def plotSlam3d(slam):
	file=open(slam,'r')
	fig=plt.figure()
	ax=fig.gca(projection='3d')

	xSlam=[]
	ySlam=[]
	zSlam=[]

	xrS=[]
	yrS=[]
	zrS=[453.9,689.2]

	for line in file:
		words = line.split(" ")
		xSlam.append(float(words[5]))
		ySlam.append(float(words[6]))
		zSlam.append(float(words[8]))
		if float(words[8]) in zrS:
			xrS.append(float(words[5]))
			yrS.append(float(words[6]))

	file.close()
	ax.plot(xSlam,ySlam,zSlam,label='slam')
	ax.plot(xrS,yrS,zrS,label='relationSlam')
	ax.legend()

def plotRelation3d(gt,slam,t1,t2):
	file=open(gt,'r')
	fig=plt.figure()
	ax=fig.gca(projection='3d')

	xGT=[]
	yGT=[]
	zGT=[]

	xr=[]
	yr=[]
	zr=[t1,t2]

	for line in file:
		words = line.split(" ")
		xGT.append(float(words[1]))
		yGT.append(float(words[2]))
		zGT.append(float(words[0]))
		if float(words[0]) in zr:
			xr.append(float(words[1]))
			yr.append(float(words[2]))

	file.close()
	print xr
	print yr 
	print zr
	ax.plot(xGT,yGT,zGT,label='ground truth')
	ax.plot(xr,yr,zr,label='relation')
	ax.legend()
	file=open(slam,'r')

	xSlam=[]
	ySlam=[]
	zSlam=[]

	xrS=[]
	yrS=[]
	zrS=[t1,t2]

	for line in file:
		words = line.split(" ")
		xSlam.append(float(words[5]))
		ySlam.append(float(words[6]))
		zSlam.append(float(words[8]))
		if float(words[8]) in zrS:
			if float(words[5]) not in xrS:
				xrS.append(float(words[5]))
			if float(words[6]) not in yrS:
				yrS.append(float(words[6]))

	file.close()
	ax.plot(xSlam,ySlam,zSlam,label='slam')
	ax.plot(xrS,yrS,zrS,label='relationSlam')
	ax.legend()

def plot():
	file=open(sys.argv[1],'r')
	#fileRot=open('office_d-5min-centered.log','w')
	fig=plt.figure()
	ax=fig.gca(projection='3d')

	xGT=[]
	yGT=[]
	zGT=[]

	for line in file:
		words = line.split(" ")
		#rot=rotate((float(words[1]),float(words[2])),(0,0),0.785398163397)
		xGT.append(float(words[1]))
		yGT.append(float(words[2]))
		zGT.append(float(words[0]))
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
		
		#z.append(float(words[8]))
		if 4000 <= i <= 5000:
			file2Scaled.write('FLASER 0 0.0 0.0 0.0 '+str(float(words[5])+10)+' '+str(float(words[6])+10)+' '+words[7]+' '+words[8])
		else:
			file2Scaled.write('FLASER 0 0.0 0.0 0.0 '+str(float(words[5]))+' '+str(float(words[6]))+' '+words[7]+' '+words[8])
		i+=1
		'''

	#ax.plot(x,y,z,label='gmapping')
	ax.plot(xGT,yGT,zGT,label='ground truth')
	ax.legend()

	file2.close()
	#file2Scaled.close()
	#plt.plot(xGT,yGT,'g',x,y,'r')
	#plt.show()
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
		if float(sortedtimes[time][1])-float(sortedtimes[time][0]) < 10 and float(sortedtimes[time][1]) > float(sortedtimes[time][0]):

			current_x = float(sortedtimes[time][2])
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

			#vec =  m_translation * m_rotation * vec
			M = m_translation_back_to_current * m_rotation * m_translation_to_origin * m_translation
			vec = M * vec

			x=vec[0,0]
			y=vec[1,0]

			x_vect.append(x)
			y_vect.append(y)
			

	relationsFile.close()

	plt.plot(x_vect,y_vect,'b')

def plotOdomRawSeeds(odom):
	x=[]
	y=[]
	with open(odom) as odomfile:
		reader=csv.DictReader(odomfile)
		for row in reader:
			x.append(row['x'])
			y.append(row['y'])
	
	plt.plot(x,y,'r')

def plotGTRawSeeds(gt):
	x=[]
	y=[]
	with open(gt) as gtfile:
		reader=csv.DictReader(gtfile)
		for row in reader:
			x.append(row['x'])
			y.append(row['y'])
	
	plt.plot(x,y,'g')

def calcTime(relations):
	file=open(relations,'r')
	c=0
	totdif=0
	mano=0
	for line in file:
		words = line.split(" ")
		if float(words[1])-float(words[0]) < 1:
			totdif+=float(words[1])-float(words[0])
			c+=1
		else:
			mano+=1
	print c
	print mano
	print totdif/c
	file.close()

def calcError(unsorted):
	file=open(unsorted,'r')
	error=0
	num=0
	for line in file:
		words = line.split(" ")
		if float(words[0]) > 10:
			print float(words[0])
			error+=float(words[0])
			num+=1
	print error
	print num
	print error/num
	file.close()

def histoErrorNum(relations,errors):
	relationsFile=open(relations,'r')
	errorFile=open(errors,'r')
	deltaTimes={}

	errors={}

	errorRange=[0,0.1,0.6,1,2,5,10,20,30]

	i=0
	for line in relationsFile:
		words=line.split(' ')
		if i not in deltaTimes:
			deltaTimes[i]=[float(words[1])-float(words[0])]
		i+=1

	i=0
	for line in errorFile:
		words=line.split(' ')
		deltaTimes[i].append(float(words[0]))
		i+=1

	for d in deltaTimes:
		for e in range(1,len(errorRange)):

			if e not in errors:
				errors[e]=[0,0,0,0]

			if deltaTimes[d][1] < errorRange[e] and deltaTimes[d][1] > errorRange[e-1]:
				if deltaTimes[d][0] > 1:
					errors[e][1] += 1
				else:
					errors[e][3] += 1


	orderedNum=[]
	randomNum=[]

	for e in errors:
		orderedNum.append(errors[e][3])
		randomNum.append(errors[e][1])

	N=7
	errorRange=[0.1,0.6,1,2,5,10,20,30]
	ind = errorRange
	width = 0.35
	p1 = plt.bar(ind, orderedNum, width, color=(0.2588,0.4433,1.0))
	p2 = plt.bar(ind, randomNum, width, color=(1.0,0.5,0.62),bottom=orderedNum)
	plt.ylabel('Num of relations with that error')
	plt.xlabel('Error of Relation')
	plt.legend((p1[0], p2[0]), ('Ordered', 'Random'))

def histoErrorSum(relations,errors):
	relationsFile=open(relations,'r')
	errorFile=open(errors,'r')
	deltaTimes={}

	errors={}

	errorRange=[0,0.1,0.3,0.6,1,2,5,10,20,30]

	i=0
	for line in relationsFile:
		words=line.split(' ')
		if i not in deltaTimes:
			deltaTimes[i]=[float(words[1])-float(words[0])]
		i+=1

	i=0
	for line in errorFile:
		words=line.split(' ')
		deltaTimes[i].append(float(words[0]))
		i+=1

	for d in deltaTimes:
		for e in range(1,len(errorRange)):

			if e not in errors:
				errors[e]=[0,0,0,0]

			if deltaTimes[d][1] < errorRange[e] and deltaTimes[d][1] > errorRange[e-1]:
				if deltaTimes[d][0] > 1:
					errors[e][0] += deltaTimes[d][1]
				else:
					errors[e][2] += deltaTimes[d][1]



	orderedError=[]
	randomError=[]

	for e in errors:
		orderedError.append(errors[e][2])
		randomError.append(errors[e][0])

	N=7
	errorRange=[0.1,0.3,0.6,1,2,5,10,20,30]
	ind = errorRange
	width = 0.35
	p1 = plt.bar(ind, orderedError, width, color=(0.2588,0.4433,1.0))
	p2 = plt.bar(ind, randomError, width, color=(1.0,0.5,0.62),bottom=orderedError)
	plt.ylabel('Error Sum')
	plt.xlabel('Error of Relation')
	plt.title('Error by relation')
	plt.legend((p1[0], p2[0]), ('Ordered', 'Random'))

def histoErrorAvg(relations,errors):
	relationsFile=open(relations,'r')
	errorFile=open(errors,'r')
	deltaTimes={}

	errors={}

	errorRange=[0,0.1,0.3,0.6,1,2,5,10,20,30]

	i=0
	for line in relationsFile:
		words=line.split(' ')
		if i not in deltaTimes:
			deltaTimes[i]=[float(words[1])-float(words[0])]
		i+=1

	i=0
	for line in errorFile:
		words=line.split(' ')
		deltaTimes[i].append(float(words[0]))
		i+=1

	for d in deltaTimes:
		for e in range(1,len(errorRange)):

			if e not in errors:
				errors[e]=[0,0,0,0]

			if deltaTimes[d][1] < errorRange[e] and deltaTimes[d][1] > errorRange[e-1]:
				if deltaTimes[d][0] > 1:
					errors[e][0] += deltaTimes[d][1]
				else:
					errors[e][2] += deltaTimes[d][1]


	orderedAvg=[]
	randomAvg=[]

	for e in errors:
		orderedAvg.append(errors[e][2]/i)
		randomAvg.append(errors[e][0]/i)

	N=7
	errorRange=[0.1,0.3,0.6,1,2,5,10,20,30]
	ind = errorRange
	width = 0.35
	p1 = plt.bar(ind, orderedAvg, width, color=(0.2588,0.4433,1.0))
	p2 = plt.bar(ind, randomAvg, width, color=(1.0,0.5,0.62),bottom=orderedAvg)
	plt.ylabel('Error Avg')
	plt.xlabel('Error of Relation')
	plt.title('Error by relation')
	plt.legend((p1[0], p2[0]), ('Ordered', 'Random'))

def histoErrorAvgRot(relations,errors):
	relationsFile=open(relations,'r')
	errorFile=open(errors,'r')
	deltaTimes={}

	errors={}

	errorRange=[0,0.1,0.2,0.3,0.4,0.6,1,1.5,2,3]

	i=0
	for line in relationsFile:
		words=line.split(' ')
		if i not in deltaTimes:
			deltaTimes[i]=[float(words[1])-float(words[0])]
		i+=1

	i=0
	for line in errorFile:
		words=line.split(' ')
		deltaTimes[i].append(float(words[0]))
		i+=1

	for d in deltaTimes:
		for e in range(1,len(errorRange)):

			if e not in errors:
				errors[e]=[0,0,0,0]

			if deltaTimes[d][1] < errorRange[e] and deltaTimes[d][1] > errorRange[e-1]:
				if deltaTimes[d][0] > 1:
					errors[e][0] += deltaTimes[d][1]
				else:
					errors[e][2] += deltaTimes[d][1]


	orderedAvg=[]
	randomAvg=[]

	for e in errors:
		orderedAvg.append(errors[e][2]/i)
		randomAvg.append(errors[e][0]/i)

	N=7
	errorRange=[0.1,0.2,0.3,0.4,0.6,1,1.5,2,3]
	ind = errorRange
	width = 0.1
	p1 = plt.bar(ind, orderedAvg, width, color=(0.2588,0.4433,1.0))
	p2 = plt.bar(ind, randomAvg, width, color=(1.0,0.5,0.62),bottom=orderedAvg)
	plt.ylabel('Error Avg')
	plt.xlabel('Error of Relation')
	plt.title('Error by relation')
	plt.legend((p1[0], p2[0]), ('Ordered', 'Random'))

def plotGaussianError(path, numFiles):
	errors = {}
	numFiles = int(numFiles)
	minError = 100000000000000
	maxError = 0
	for i in range(1,numFiles+1):
		errorFile = open(path+"Terror"+str(i)+".error","r")
		content = errorFile.readlines()
		words = content[1].split(", ")
		mean = round(float(words[0]),2) # retrieve the rounded mean mean
		if mean > maxError:
			maxError = mean
		if mean < minError:
			minError = mean
		errors[mean] = errors.get(mean, 0) + 1
		errorFile.close()
	print minError
	print maxError
	errorRange = [round(x,2) for x in np.arange(minError,maxError+0.01,0.01,dtype=np.float64)]
	print errorRange
	values = []
	for e in errorRange:
		values.append(errors.get(e,0))
	ind = errorRange
	width = 0.01
	p1 = plt.bar(ind, values, width, color=(0.2588,0.4433,1.0))
	plt.ylabel('N. of occurrences')
	plt.xlabel('Error mean')
	plt.title('Error mean distribution')

		

if __name__=='__main__':	
	#plotRelation3d(sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]))
	#plotSlam3d(sys.argv[2])
	#plotRelationsRT(sys.argv[1])
	#plotRelationsTR(sys.argv[1])
	#plotGroundTruth(sys.argv[1])
	#plotSlam(sys.argv[2])
	#plotOdom(sys.argv[3])
	#plotGTRawSeeds(sys.argv[1])
	#plotOdomRawSeeds(sys.argv[2])
	if sys.argv[1] == 'Sum':
		histoErrorSum(sys.argv[2],sys.argv[3])
	elif sys.argv[1] == 'Num':
		histoErrorNum(sys.argv[2],sys.argv[3])
	elif sys.argv[1] == 'Avg':
		histoErrorAvg(sys.argv[2],sys.argv[3])
	elif sys.argv[1] =='AvgR':
		histoErrorAvgRot(sys.argv[2],sys.argv[3])
	elif sys.argv[1] == 'SLAMGT':
		plotSlam(sys.argv[2])
		plotGroundTruth(sys.argv[3])
	elif sys.argv[1] == 'Gauss':
		plotGaussianError(sys.argv[2],sys.argv[3])
	plt.show()
	#calcTime(sys.argv[1])
	#calcError(sys.argv[1])
