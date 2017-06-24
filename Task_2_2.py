import numpy as np
import cv2 as cv

img = np.array(cv.imread('sad.png',0))  #reading image in numpy array

dim=np.shape(img)

r=int(dim[0])
c=int(dim[1])

flipped = np.zeros((r,c),dtype=np.uint8)

for i in range(r):
    for j in range(c):
        flipped[i,j]=img[r-i-1,j]

cv.imshow('Flipped',flipped)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Flipped Image.png',flipped)

        
        

