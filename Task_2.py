import numpy as np
import cv2 as cv

img = np.array(cv.imread('sad.png',0))  #reading image in numpy array

dim=np.shape(img)
newimg = np.zeros(dim(0)/2,dim(1)/2)

for i in range(dim(0)/2):
    for j in range(dim(1)/2):
        newimg(i,j) = img(i,j)

cv.imshow('New image',newimg);
        
        
