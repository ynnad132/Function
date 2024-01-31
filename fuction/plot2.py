import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as img
from PIL import Image
path_tooth_all  = r'C:\Users\EE803\Desktop\520201.jpg'

img = Image.open(path_tooth_all)



#plot 1:
plt.figure(figsize=(25,12))
plt.subplot(1, 5, 1)
img1 = img.rotate(-90)
plt.imshow(img1)
plt.axis('off')
plt.title("rotate -90 degree",{'fontsize':30})


plt.subplot(1, 5, 2)
img2 = img.rotate(-45)
plt.imshow(img2)
plt.axis('off')
plt.title("rotate -45 degree",{'fontsize':30})

#plot 3:


plt.subplot(1, 5, 3)
plt.imshow(img)
plt.axis('off')
plt.title("uncahange",{'fontsize':30})

plt.subplot(1, 5, 4)
img3 = img.rotate(45)
plt.imshow(img3)
plt.axis('off')
plt.title("rotate 45 degree",{'fontsize':30})


plt.subplot(1, 5, 5)
img4 = img.rotate(90)
plt.imshow(img4)
plt.axis('off')
plt.title("rotate 90 degree",{'fontsize':30})

plt.tight_layout()
plt.show()