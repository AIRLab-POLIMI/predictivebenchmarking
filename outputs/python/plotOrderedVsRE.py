import sys
from os import listdir, makedirs
from os.path import isfile, join, exists
import matplotlib.pyplot as plt

def plotGraphic(folder):
	yTOrdered=[]
	yTRE=[]
	yROrdered=[]
	yRRE=[]

	fig=plt.figure()
	ax=fig.gca()

	x=[]
	c=0

	for f in listdir(folder):

		x.append(c)
		c+=1

		for error in listdir(join(folder,f)):

			#RE error
			if error[-2:] == "RE":
				for file in listdir(join(folder,f,error)):

					if file[:2]=="T.":
						e=open(join(folder,f,error,file),"r")
						for line in e:
							words = line.split(", ")
							if words[0] != "Mean":
								yTRE.append(words[0])
						e.close()

					elif file[:2]=="R.":
						e=open(join(folder,f,error,file),"r")
						for line in e:
							words = line.split(", ")
							if words[0] != "Mean":
								yRRE.append(words[0])
						e.close()

			#Ordered error
			else:
				for file in listdir(join(folder,f,error)):

					if file[:2]=="T.":
						e=open(join(folder,f,error,file),"r")
						for line in e:
							words = line.split(", ")
							if words[0] != "Mean":
								yTOrdered.append(words[0])
						e.close()
								
					elif file[:2]=="R.":
						e=open(join(folder,f,error,file),"r")
						for line in e:
							words = line.split(", ")
							if words[0] != "Mean":
								yROrdered.append(words[0])
						e.close()

	#plt.plot(x,yROrdered,'r',x,yTOrdered,'g',x,yRRE,'b',x,yTRE,'y')

#	ax.plot(x,yROrdered,label='Rot Ordered')
	ax.plot(x,yTOrdered,label='Trans Ordered')
#	ax.plot(x,yRRE,label='Rot RE')
	ax.plot(x,yTRE,label='Trans RE')
	ax.legend()

	plt.show()

if __name__ == '__main__':
	plotGraphic(sys.argv[1])