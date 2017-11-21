import sys,argparse
import numpy as np

def avgDatasets(filerrors):
    file = open(filerrors, 'r')

    data=[]
    avg=[0]*10 #range(10)
    first = True
    precrow = 'precrow'
    count=0
    allavg={}
    allstd={}

    for line in file:
        if first:
            first = False
        else:
            words = line.split(", ")
            # we now need to recognize different datasets
            if words[0] != precrow:
                if precrow == 'precrow':
                    # first run, initialize and nothing else
                    for i in range(0, len(words)-1):
                        data.append([])
                        data[i].append(float(words[i+1])) 
                else:
                    # we have changed dataset, hence we can compute the statistics for the old one
                    avg = [0]*(len(words)-1)
                    std = [0]*(len(words)-1)
                    print precrow
                    for i in range(0, len(words)-1):
                        arr = np.array(data[i])
                        avg[i] = arr.mean()
                        std[i] = arr.std()
                        data[i] = []
                        data[i].append(float(words[i+1])) 
                    allavg[precrow] = avg
                    allstd[precrow] = std
                precrow = words[0]
            else: # otherwise keep going
                for i in range(0, len(words)-1):
                    data[i].append(float(words[i+1])) 

    #for line in file:
    #    if first:
    #        first = False
    #    else:
    #        words = line.split(", ")
    #        if words[0] != precrow:
    #            if avg != [0]*10: #range(10):
    #                for c in range(1, len(words)):
    #                    avg[c]/=count
    #
    #            count=1
    #            allavg[precrow]=avg
    #            avg = range(10)
#
 #               precrow = words[0]
  #              for c in range(1,len(words)):
   #                 print words[c]
    #                avg[c]=0
     #               avg[c]+=float(words[c])
      #              print avg

       #     else:
        #        count+=1
         #       for c in range(1, len(words)):

          #          avg[c]+=float(words[c])

    out=open('avg.csv','w')
    out.write('DATASET, MEAN-T, STD-T, MIN-T, MAX-T, MEAN-R, STD-R, MIN-R, MAX-R, NUMMEASURES\n')
    for avg in allavg:
        out.write(avg+', ')
        for a in allavg[avg]:
            out.write(str(a) + ', ')
        out.write('\n')
    out.write('DATASET, MEAN-T, STD-T, MIN-T, MAX-T, MEAN-R, STD-R, MIN-R, MAX-R, NUMMEASURES\n')
    for std in allstd:
        out.write(std+', ')
        for s in allstd[std]:
            out.write(str(s) + ', ')
        out.write('\n')
    out.close()
    file.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='This tool aggregates the performance data of the individual runs for each of the datasets contained in the <errors.csv> (produced by writecsv.py) and writes a corresponding <avg.csv> file.')
    parser.add_argument('errorFile',help='the csv error summary file produced by writecsv.py')
    args = parser.parse_args()
    avgDatasets(args.errorFile)
