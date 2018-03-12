from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys,argparse
from os import listdir
from os.path import join, isdir, exists

def writeText(path):
    lastmap='1Map.png'
    for image in listdir(join(path,'Maps')):
        if image[-4:]=='.png' and image[-7:-4] == 'Map' and image[0:2]!='._':
            if int(image[:-7]) > int(lastmap[:-7]):
                lastmap=image
    if exists(join(path+'/Maps',lastmap)):
        pattern = Image.open(join(path+'/Maps',lastmap), "r").convert('RGBA')
        size = width, height = pattern.size
        draw = ImageDraw.Draw(pattern,'RGBA')
        font = ImageFont.truetype("OpenSans-Regular.ttf", 100)

        if exists(join(path,'Errors/Original/RE/T.errors')):
            tEr=open(join(path,'Errors/Original/RE/T.errors'),'r')
            first=True
            for line in tEr:
                if first:
                    first=False
                else:
                    words=line.split(', ')
                    textmeanT=words[0]
                    textstdT=words[1]
                    textmaxT=words[3]
                    textnumMes=words[4]

            rEr=open(join(path,'Errors/Original/RE/R.errors'),'r')
            first=True
            for line in rEr:
                if first:
                    first=False
                else:
                    words=line.split(', ')
                    textmeanR=words[0]
                    textstdR=words[1]
                    textmaxR=words[3]

            draw.text((1000,3700), 'MEAN-T ' + textmeanT+' STD-T '+textstdT+'\nMEAN-R ' + textmeanR+' STD-R '+textstdR, fill=(0, 0, 0, 255), font=font)
            pattern.save(path+'/errorMap.png')

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='This tool takes the last available map snapshot from the Maps folder within <individual_run_folder> and overlays it with the value of the mean translation error, as computed by the Freiburg Metric Evaluator on the randomly sampled relations. Under normal conditions, there is no need to manually execute this component, as it is automatically invoked by generateAll.py at the end of its computation. However, it can also be executed manually.')
    parser.add_argument('individual_run_folder',help='the folder containing the data (Errors, Maps, ...) of a single run')
    args = parser.parse_args()
    writeText(args.individual_run_folder)
