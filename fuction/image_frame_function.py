import cv2
import numpy as np
import os


video_name1 = r'C:\Users\EE803\Desktop\tooth_video\video\decay\1.mp4'
path = r'C:\Users\EE803\Desktop\tooth_video\image'
#video_name2 = r'C:\Users\EE803\Desktop\tooth_video\video\2.mp4'
#video_name=[video_name1,video_name2]
video_name=video_name1
#%%

time_F = 2#time_F越小，取樣張數越多


c = 0

def get_images_from_video(video_name, time_F,c):
    
    vc = cv2.VideoCapture(video_name)
    

    if vc.isOpened(): #判斷是否開啟影片
        rval, video_frame = vc.read()
    else:
        rval = False

    while rval:   #擷取視頻至結束
        rval, video_frame = vc.read()
        
        if(c % time_F == 0): #每隔幾幀進行擷取
            image_outpath = os.path.join(f'C:/Users/EE803/Desktop/tooth_video/image/{c:05d}.jpg')
            cv2.imwrite(image_outpath, video_frame)     
        c = c + 1
    vc.release()
    
    return c


c = get_images_from_video(video_name,time_F,c)

#%%

def batch_rename(path):
    count = 5188
    for fname in os.listdir(path):
        new_fname = f'{count:05d}.jpg'
        #print os.path.join(path, fname)
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        count = count + 1 

batch_rename(path)

























    
