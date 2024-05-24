import math
import os
import glob



txtList = glob.glob(r'C:\Users\EE803\Desktop\研究_別刪\Data\Cavity Data\valid\labels\*.txt')  #所有txt檔案
imageList = glob.glob(r'C:\Users\EE803\Desktop\研究_別刪\Data\Cavity Data\valid\images\*.jpg')  #所有jpg檔案

txtlist = []
imagelist = []

for txt in txtList:
    txt = txt.split('\\')
    txtlist.append(txt[-1][:-4])
        



for image in imageList:
    image = image.split('\\')
    imagelist.append(image[-1][:-4])
    

for img in imagelist:
    if img not in txtlist:
        print(img)


        



'''


for file in txtList:
    with open(file,'r') as f:
        lines = f.readlines()
        i = len(lines)
        with open(file, 'w') as ff:
            for line in lines:
                line = line.replace(line[0], '1',1)
                ff.write(line)
            
'''
    


       

                


