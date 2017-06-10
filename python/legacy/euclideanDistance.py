import sys
import math

def euclideanDistance(gt,slam):

	gtFile=open(gt,'r')
	slamFile=open(slam,'r')
	euclideanDist=open('euclideanDistance.log','w')
	slamDict={}

	for pos in slamFile:
		words=pos.split(' ')

		eulerslam=[float(words[5]),float(words[6]),float(words[7])]

		if words[8] not in slamDict:
			slamDict[float(words[8])]=eulerslam
		else:
			slamDict.update({ float(words[8]): eulerslam })	

	for line in gtFile:
		words = line.split(' ')

		euler=[float(words[1]),float(words[2]),float(words[3])]
		timestamp=float(words[0])

		if timestamp in slamDict:
			dist=math.sqrt(math.pow((euler[0]-slamDict[timestamp][0]),2)+math.pow((euler[1]-slamDict[timestamp][1]),2))
			euclideanDist.write(str(timestamp)+' '+str(dist)+'\n')

if __name__=='__main__':
	euclideanDistance(sys.argv[1],sys.argv[2])