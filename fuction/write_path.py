
# -*- coding:utf-8 -*-
import glob
 
imageList = glob.glob(r"C:\Users\EE803\Desktop\yolov7-main\datasets\paper_s_one_label\images\val\*.jpg")  # 图片所在文件夹的路径
f = open(r'C:\Users\EE803\Desktop\yolov7-main\datasets\paper_s_one_label\images\val_list.txt', 'a')  # 创建标签文件存放图片文件名
i = 0
for item in imageList:
    #print()   # D:\0_me_python\目标检测\SSD-pytorch-main\SSD-pytorch-main\coco\val2017\000000000139.jpg
    img_name = item.split('\\')  # 图片文件名018.jpg
    # img_name = item.split('\\')[-1]  # 图片文件名018.jpg
    f.write(str(img_name[5])+'/'+str(img_name[6]) + '/' +str(img_name[7])+ '/'+str(img_name[8])+'/'+str(img_name[9]) +  '\n')  # 将图片文件名逐行写入txt
   

f.close()
print('OK')
