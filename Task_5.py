import cv2 as cv, numpy as np

def DownSample():
    
    img = np.array(cv.imread('sad.png',0))      #reading image and storing in numpy array
    img = cv.resize(img,(512,512))              #Resizing image to 512x512 

    dim = np.shape(img)
    
    new_img = np.zeros((int(dim[0]/4),int(dim[1]/4)),dtype=np.uint8)
##    for i in range(int(dim[0]/4)):
##        for j in range(int(dim[1]/4)):
##            if i%4==0 or j%4==0:
##                new_img[i:j] = img[i*4,j*4]
##

    
    di = np.shape(new_img)
    new_img = img[0:dim[0]-1:4,0:dim[1]-1:4]

    print(img)
    print(new_img)
    print(dim)
    print(di)
    
    cv.imshow('Resized Image',img)
    cv.imshow('Down Sampled by 4', new_img)
    cv.waitKey(10000)
    cv.destroyAllWindows()

    return

DownSample()