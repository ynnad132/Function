import os
import pandas as pd

txt_path =r'C:\Users\EE803\Desktop\yolov7-main\runs\train\tooth_moco_smalldic_dualtemperature_all\results.txt'
csv_filename = r'C:\Users\EE803\Desktop\yolov7.csv'

precision = []
recall=[]
map05=[]
map05_095 = []


with open(txt_path) as f:
    all_data = f.readlines()
    for i in range(len(all_data)):
        tmp = []
        for element in all_data[i].strip().split():
            tmp.append(element)
            
        precision.append(tmp[8])
        recall.append(tmp[9])
        map05.append(tmp[10])
        map05_095.append(tmp[11])

         
submit = pd.DataFrame(data=precision, columns=['precision'],index=None)
submit.insert(1,column="recall",value=recall)
submit.insert(2,column="map05",value=map05)
submit.insert(3,column="map05_095",value=map05_095)
submit.to_csv(csv_filename,index=False)
