import subprocess
import argparse

def launch(file,dataset, errType):
	if errType=="T":
		trans="{1.0,1.0,1.0,0.0,0.0,0.0}"
		command='./metricEvaluator -s {0} -r /home/ros/catkin_ws/datasets/relations/{1}.relations -o /home/ros/catkin_ws/datasets/logs/{2}.log -w '.format(file,dataset,dataset)+trans+' -e {0}.errors -eu {1}.errors -em {2}.errors -e1 {3}.errors -e2 {4}.errors'.format(dataset+"//"+file[:-4],dataset+"//"+file[:-4]+"unsorted",dataset+"//"+file[:-4]+"magnitude",dataset+"//"+file[:-4]+"first",dataset+"//"+file[:-4]+"second")
		subprocess.call(command,shell=True)

	elif errType=="R":
		rot="{0.0,0.0,0.0,1.0,1.0,1.0}"
		command='./metricEvaluator -s {0} -r /home/ros/catkin_ws/datasets/relations/{1}.relations -o /home/ros/catkin_ws/datasets/logs/{2}.log -w '.format(file,dataset,dataset,)+rot+' -e {0}R.errors -eu {1}R.errors -em {2}R.errors -e1 {3}R.errors -e2 {4}R.errors'.format(dataset+"//"+file[:-4],dataset+"//"+file[:-4]+"unsorted",dataset+"//"+file[:-4]+"magnitude",dataset+"//"+file[:-4]+"first",dataset+"//"+file[:-4]+"second")
		subprocess.call(command,shell=True)

if __name__=='__main__':
	parser=argparse.ArgumentParser(description="Launch metric eval")
	parser.add_argument("--slam","-s",type=str,required=True,help="Slam log file")
	parser.add_argument("--dataset","-d",type=str,required=True,help="Dataset name")
	parser.add_argument("--err","-e",type=str,required=True,help="Translational(T) or Rotational(R) error")
	args=parser.parse_args()
	"""print "Enter slam file name:"
	file=raw_input()
	print "Enter dataset name:"
	dataset=raw_input()
	print "Translational(T) or Rotational(R) error?"
	errType=raw_input()"""
	launch(args.slam,args.dataset,args.err)
