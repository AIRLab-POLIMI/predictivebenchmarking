import sys
import bisect

def sortRelations(file):
	file=open(file,'r')
	firstTime=[]
	for line in file:
		bisect.insort(firstTime, line)
	print firstTime

if __name__=='__main__':
	
	sortRelations(sys.argv[1])
