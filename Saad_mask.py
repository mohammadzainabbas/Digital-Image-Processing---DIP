#lab 5
#-Saad

import cv2
import numpy as np
def nopad():
    src=cv2.imread('hazard.jpg',0)
    [r,c]=np.shape(src)
    print('rows' + str(r))
    print('cols' + str(c));
    result=np.zeros((r,c));

    size=int(input('Mask Size: '));
    mask=np.ones((size,size));

    #without Padding
    val=0;
    offset=int((size-1)/2)
    for i in range(offset,r-offset-1):
        for j in range(offset,c-offset):
            for a in range(0,size-1):
                for b in range(0,size-1):
                    val=val+(mask[a,b]*src[(i-offset)+a,(j-offset)+a])
            
            val=val/(size*size);
            result[i,j]=val;

    cv2.imwrite('Masked_without_padding.jpg',result);

def pad():
    src=cv2.imread('hazard.jpg',0)
    [r,c]=np.shape(src)
    
    print('rows' + str(r))
    print('cols' + str(c));
    result=np.zeros((r,c));

    size=int(input('Mask Size: '));
    mask=np.ones((size,size));

   
    val=0;
    offset=int((size-1)/2)
    new=np.zeros((r+offset,c+offset));

    for i in range (offset,r):
        for j in range(offset,c):
            new[i,j]=src[i,j]

    cv2.imshow("New",new);
    
    for i in range(0,r-1):
        for j in range(0,c-1):
            for a in range(0,size-1):
                for b in range(0,size-1):
                    val=val+(mask[a,b]*new[(i-offset)+a,(j-offset)+a])
            
            val=val/(size*size);
            result[i,j]=val;

    cv2.imwrite('Masked_with_padding.jpg',result);

def gaus():
    src=cv2.imread('hazard.jpg',2)
    cv2.imshow("input",src);
    [r,c]=np.shape(src)
    array=[0.0625,0.125,0.0625,0.0125,0.25,0.125,0.0625,0.125,0.0625]
    mask=np.zeros((3,3));
    
    result=np.zeros((r,c));

    size=3;
    x=0;
    val=0;
    for i in range(0,3):
        for j in range(0,3):
            mask[i,j]=array[x]
            x=x+1;
    
    print(str(mask));
    for i in range(1,r-1):
        for j in range(1,c-1):
            for a in range(0,size-1):
                for b in range(0,size-1):
                    val=val+(mask[a,b]*src[(i-1)+a,(j-1)+a])
            
            val=val/(size*size);
            result[i,j]=val;

    cv2.imwrite('Masked_with_gausianBlur.jpg',result);
