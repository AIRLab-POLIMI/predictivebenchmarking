import sys

def calcDisplacement(slam,relations):

	relationsFile=open(relations,'r')
	slamFile=open(slam,'r')
	displacementFile=open('displacement.log','w')
	slamDict={}


	for pos in slamFile:
		words=pos.split(' ')
		euler=[words[5],words[6],words[7]]
		if words[8] not in slamDict:
			slamDict[round(float(words[8]),1)]=euler 
		else:
			slamDict.update({ round(float(words[8]),1): euler })

	for line in relationsFile:
		words=line.split(' ')
		firststamp=round(float(words[0]),1)
		secondstamp=round(float(words[1]),1)
		if firststamp in slamDict and secondstamp in slamDict:
			firstpos=slamDict[firststamp]
			secondpos=slamDict[secondstamp]
			relation=[float(secondpos[0])-float(firstpos[0]), float(secondpos[1])-float(firstpos[1]), float(secondpos[2])-float(firstpos[2])]
			displacementFile.write(str(relation[0])+" "+str(relation[1])+" "+str(relation[2])+"\n")

if __name__=='__main__':
	calcDisplacement(sys.argv[1], sys.argv[2])