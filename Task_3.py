import numpy as np
import cv2 as cv

def BoxGenerator(w,b):
    r=w+b
    box = np.zeros((r,r),dtype=np.uint8)
    box[0:r,0:r]=255
    box[0:r,0:b]=0
    box[0:b,0:r]=0
    box[w:r,0:r]=0
    box[0:r,w:r]=0
    cv.imshow('Box',box)
    cv.waitKey(100000)
    cv.destroyAllWindows()
    cv.imwrite('Box.png',box)
    return 

##
##for i in range(r):
##    for j in range(c):
##        flipped[i,j]=img[r-i-1,j]
##
##cv.imshow('Flipped',flipped)
##cv.waitKey(10000)
##cv.destroyAllWindows()
##cv.imwrite('Flipped Image.png',flipped)

whiterows=int(input('Enter white rows size: '))
blackrows=int(input('Enter black rows size: '))
BoxGenerator(whiterows,blackrows);
        


