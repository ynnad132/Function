import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
from PIL import Image
path_tooth_all  = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_all\05084.jpg'
path_tooth_100  = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_100\05084.jpg'
path_tooth_300  = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_300\05084.jpg'
path_tooth_moco_100 = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_moco_100\05084.jpg'
path_tooth_moco_300  = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_moco_300\05084.jpg'
path_tooth_moco_all = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_moco_all\05084.jpg'
path_tooth_moco_smalldic_dualtemperature_all  = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_moco_smalldic_dualtemperature_all\05084.jpg'
path_tooth_no_pretrain = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_no_pretrain\05084.jpg'
path_tooth_no_pretrain_100 = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_no_pretrain_100\05084.jpg'
path_tooth_no_pretrain_300 = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_no_pretrain_300\05084.jpg'
path_tooth_smalldic_dualtem_100 = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_smalldic_dualtem_100\05084.jpg'
path_tooth_smalldic_dualtem_300 = r'C:\Users\EE803\Desktop\yolov7-main\runs\detect\tooth_smalldic_dualtem_300\05084.jpg'



img_tooth_all = Image.open(path_tooth_all)
img_tooth_100 = Image.open(path_tooth_100)
img_tooth_300 = Image.open(path_tooth_300)
img_tooth_moco_100 = Image.open(path_tooth_moco_100)
img_tooth_moco_300  = Image.open(path_tooth_moco_300 )
img_tooth_moco_all = Image.open(path_tooth_moco_all)
img_tooth_moco_smalldic_dualtemperature_all = Image.open(path_tooth_moco_smalldic_dualtemperature_all)
img_tooth_smalldic_dualtem_100 = Image.open(path_tooth_smalldic_dualtem_100)
img_tooth_smalldic_dualtem_300 = Image.open(path_tooth_smalldic_dualtem_300)
img_tooth_no_pretrain = Image.open(path_tooth_no_pretrain)
img_tooth_no_pretrain_100 = Image.open(path_tooth_no_pretrain_100)
img_tooth_no_pretrain_300 = Image.open(path_tooth_no_pretrain_300)

#plot 1:
plt.figure(figsize=(17,23))
plt.subplot(3, 2, 1)
plt.imshow(img_tooth_all)
plt.axis('off')
plt.title("Pre-train_all",{'fontsize':25})


plt.subplot(3, 2, 2)
plt.imshow(img_tooth_no_pretrain)
plt.axis('off')
plt.title("No Pre-train_all",{'fontsize':25})

#plot 3:

plt.subplot(3, 2, 3)
plt.imshow(img_tooth_100)
plt.axis('off')
plt.title("Pre-train_100",{'fontsize':25})


plt.subplot(3, 2, 4)
plt.imshow(img_tooth_no_pretrain_100)
plt.axis('off')
plt.title("No Pre-train_100",{'fontsize':25})


plt.subplot(3, 2, 5)
plt.imshow(img_tooth_300)
plt.axis('off')
plt.title("Pre-train_300",{'fontsize':25})

plt.subplot(3, 2, 6)
plt.imshow(img_tooth_no_pretrain_300)
plt.axis('off')
plt.title("No Pre-train_300.",{'fontsize':25})
plt.suptitle('YOLOv7 Detect',fontsize = 35)    # 設定圖表主 title
plt.tight_layout()
plt.show()

#%%%%%%%%%%%%%%%%%%%%%
#plot 1:
plt.figure(figsize=(17,23))
plt.subplot(3, 2, 1)
plt.imshow(img_tooth_moco_all)
plt.axis('off')
plt.title("Moco_all",{'fontsize':25})


plt.subplot(3, 2, 2)
plt.imshow(img_tooth_moco_smalldic_dualtemperature_all)
plt.axis('off')
plt.title("Ours_all",{'fontsize':25})

#plot 3:

plt.subplot(3, 2, 3)
plt.imshow(img_tooth_moco_100)
plt.axis('off')
plt.title("Moco_100",{'fontsize':25})


plt.subplot(3, 2, 4)
plt.imshow(img_tooth_smalldic_dualtem_100)
plt.axis('off')
plt.title("Ours_100",{'fontsize':25})


plt.subplot(3, 2, 5)
plt.imshow(img_tooth_moco_300)
plt.axis('off')
plt.title("Moco_300",{'fontsize':25})

plt.subplot(3, 2, 6)
plt.imshow(img_tooth_smalldic_dualtem_300)
plt.axis('off')
plt.title("Ours_300.",{'fontsize':25})
plt.suptitle('YOLOv7 Detect',fontsize = 35)    # 設定圖表主 title
plt.tight_layout()
plt.show()
