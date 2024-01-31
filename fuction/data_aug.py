from functools import partial
from PIL import Image
from torch.utils.data import DataLoader
#import torchvision.models as models
from tqdm import tqdm
import argparse
import json
import math
import os
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import random
from torchvision import transforms

from torchvision.utils import save_image

train_transform = transforms.Compose([
    #transforms.Resize((96,72)),
    #transforms.RandomResizedCrop(32),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomApply([transforms.ColorJitter(0.4, 0.4, 0.4, 0.1)], p=0.8),
    transforms.RandomGrayscale(p=0.2),
    transforms.ToTensor(),
    transforms.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010])])

train_path=[]
root = r'C:\Users\EE803\Desktop\data_aug'
train_dataset_path = os.listdir(root)
for item in train_dataset_path:
 # Get all the file names
 train_path.append(str(root + '/' + item))
 

i=0
for img in train_path:
    
    image = Image.open(img)
    img_aug = train_transform(image) 
    save_image(img_aug,r'C:\Users\EE803\Desktop\image_8_7\data_augementatiom' + '/' + str(i) +'.png')
    i = i+1
    