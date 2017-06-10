import sys
import math
import numpy as np

def metricEvaluatorFreiburg(slam,relations):
	relationsFile=open(relations,'r')
	slamFile=open(slam,'r')
	displacementFile=open('metricEvaluator.log','w')
	slamDict={}
	totalerror=0
	count=0
	roundedAt=3


	for pos in slamFile:
		words=pos.split(' ')
		euler=[words[5],words[6],words[7]]
		if words[8] not in slamDict:
			slamDict[round(float(words[8]),roundedAt)]=euler 
		else:
			slamDict.update({ round(float(words[8]),roundedAt): euler })

	for line in relationsFile:
		words=line.split(' ')
		firststamp=round(float(words[0]),roundedAt)
		secondstamp=round(float(words[1]),roundedAt)
		if firststamp in slamDict and secondstamp in slamDict:
			firstpos=slamDict[firststamp]
			secondpos=slamDict[secondstamp]
			relation=[float(secondpos[0])-float(firstpos[0]), float(secondpos[1])-float(firstpos[1]), float(secondpos[2])-float(firstpos[2])]

			#inverse relationship
			xi=[1,2,3]
			xi[0]=-relation[0]*math.cos(relation[2])-relation[1]*math.sin(relation[2])
			xi[1]=relation[0]*math.sin(relation[2])-relation[1]*math.cos(relation[2])
			xi[2]=-relation[2]


			xj=[float(words[2]),float(words[3]),float(words[7])]

			#compose the relation xj-xi
			error=[0,0,0]
			error[0]=xj[0]+xi[0]*math.cos(xj[2])-xi[1]*math.sin(xj[2])
			error[1]=xj[1]+xi[0]*math.sin(xj[2])+xi[1]*math.cos(xj[2])
			error[2]=xj[2]+xi[2]

			totalerror+=np.dot(error,error)
			count+=1

			print np.dot(error,error)

	print 'Totalerror: '+str(totalerror)
	print totalerror/count

def metricEvaluator(slam,relations,error):
	relationsFile=open(relations,'r')
	slamFile=open(slam,'r')
	errorFile=open(error,'w')
	slamDict={}
	totalerror=0
	count=0


	for pos in slamFile:
		words=pos.split(' ')
		euler=[words[5],words[6],words[7]]
		if words[8] not in slamDict:
			slamDict[float(words[8])]=euler 
		else:
			slamDict.update({ float(words[8]): euler })

	for line in relationsFile:
		words=line.split(' ')
		firststamp=float(words[0])
		secondstamp=float(words[1])
		if firststamp in slamDict and secondstamp in slamDict:
			firstpos=slamDict[firststamp]
			secondpos=slamDict[secondstamp]
			relation=[float(secondpos[0])-float(firstpos[0]), float(secondpos[1])-float(firstpos[1]), float(secondpos[2])-float(firstpos[2])]

			#inverse relationship
			xi=[1,2,3]
			xi[0]=-relation[0]*math.cos(relation[2])-relation[1]*math.sin(relation[2])
			xi[1]=relation[0]*math.sin(relation[2])-relation[1]*math.cos(relation[2])
			xi[2]=-relation[2]


			xj=[float(words[2]),float(words[3]),float(words[7])]

			#compose the relation xj-xi
			error=[0,0,0]
			error[0]=xj[0]+xi[0]*math.cos(xj[2])-xi[1]*math.sin(xj[2])
			error[1]=xj[1]+xi[0]*math.sin(xj[2])+xi[1]*math.cos(xj[2])
			error[2]=xj[2]+xi[2]

			totalerror+=np.dot(error,error)
			count+=1

			errorFile.write(str(np.dot(error,error))+'\n')

	print 'Totalerror: '+str(totalerror)
	print totalerror/count
	errorFile.write('Error: '+str(totalerror/count))

if __name__=='__main__':
	#MY metricevaluator
	metricEvaluator(sys.argv[1],sys.argv[2],sys.argv[3])

	#MY metricevaluator x Freiburg
	#metricEvaluatorFreiburg(sys.argv[1],sys.argv[2])