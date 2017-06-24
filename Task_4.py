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
    print(box)
    cv.imshow('Shape_1',box)
    cv.waitKey(100000)
    cv.destroyAllWindows()
    cv.imwrite('Shape_1.png',box)
    return 

def EdgeBoxGenerator(w,b):
    r=w+b
    box = np.zeros((r,r),dtype=np.uint8)
    box[0:r,0:r]=255
    box[0:b,0:b]=0    
    box[0:b,w:r]=0
    box[w:r,0:b]=0    
    box[w:r,w:r]=0
    print(box)
    cv.imshow('Shape_2',box)
    cv.waitKey(100000)
    cv.destroyAllWindows()
    cv.imwrite('Shape_2.png',box)
    return

def LineBoxGenerator(r,w,b):
    div=int(r/(w+b))
    print(div)
    #i=[1:div]
    box = np.zeros((r,r),dtype=np.uint8)
    box[0:r,0:r]=255
##    box[0:r,w:w+b]=0
##    box[0:r,2*w+b:2*w+2*b]=0
##    box[0:r,3*w+2*b:3*w+3*b]=0
##    box[0:r,4*w+3*b:4*(w+b)]=0
##    box[w:w+b,0:r]=0
    for i in range(1,int(r/(w+b))+1):
        box[0:r,i*w+(i-1)*b:i*(w+b)]=0
        box[i*w+(i-1)*b:i*(w+b),0:r]=0
    #print(i)
    ##box[0:b,w:r]=0
    ##box[w:r,0:b]=0    
    ##box[w:r,w:r]=0
    print(box)
    cv.imshow('Shape_3',box)
    cv.waitKey(100000)
    cv.destroyAllWindows()
    cv.imwrite('Shape_3.png',box)
    return 

whiterows=int(input('Enter white box size: '))
blackrows=int(input('Enter black line size: '))
size=int(input('Enter image size: '))

#BoxGenerator(whiterows,blackrows);
#EdgeBoxGenerator(whiterows,blackrows);
LineBoxGenerator(size,whiterows,blackrows);




