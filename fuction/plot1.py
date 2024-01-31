import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
from PIL import Image
path_Mocov2_all  = r'C:\Users\EE803\Desktop\fasterrcnn_result\Mocov2\result\05084.jpg'
path_ours = r'C:\Users\EE803\Desktop\fasterrcnn_result\mocov2_65536_001\result\05084.jpg'
path_pretrain  = r'C:\Users\EE803\Desktop\fasterrcnn_result\resnet18_pretrain\result\05084.jpg'
path_no_prtrain = r'C:\Users\EE803\Desktop\fasterrcnn_result\resnet18_nopretrain\result\05084.jpg'




img_Mocov2_all = Image.open(path_Mocov2_all)
img_tooth_pretrain = Image.open(path_pretrain)
img_no_prtrain  = Image.open(path_no_prtrain)
img_ours = Image.open(path_ours)



#plot 1:
plt.figure(figsize=(24,22))
plt.subplot(2, 2, 1)
plt.imshow(img_tooth_pretrain)
plt.axis('off')
plt.title("Pre-train",{'fontsize':30})


plt.subplot(2, 2, 2)
plt.imshow(img_no_prtrain)
plt.axis('off')
plt.title("No Pre-train",{'fontsize':30})

#plot 3:

plt.subplot(2, 2, 3)
plt.imshow(img_Mocov2_all)
plt.axis('off')
plt.title("Mocov2_all",{'fontsize':30})


plt.subplot(2, 2, 4)
plt.imshow(img_ours)
plt.axis('off')
plt.title("Ours_all",{'fontsize':30})
plt.suptitle('Faster-RCNN Detect',fontsize = 35)    # 設定圖表主 title
plt.tight_layout()
plt.show()
