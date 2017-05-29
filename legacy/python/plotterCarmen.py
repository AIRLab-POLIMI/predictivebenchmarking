import matplotlib.pyplot as plt
import sys
import math

if __name__=='__main__':

	file=open(sys.argv[1],'r')

	xCarmen=[]
	yCarmen=[]

	for line in file:
		words = line.split(" ")
		if words[0]=='ODOM':
			xCarmen.append(float(words[1]))
			yCarmen.append(float(words[2]))

	file.close()

	file2=open(sys.argv[2],'r')

	x=[]
	y=[]

	for line in file2:
		words = line.split(" ")
		x.append(float(words[5]))
		y.append(float(words[6]))

	file2.close()

	plt.plot(xCarmen,yCarmen,'c',x,y,'g')
	plt.show()