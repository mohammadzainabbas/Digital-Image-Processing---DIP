import numpy as np
import cv2 as cv

def filterwopad (image,fsize):

    img = cv.imread(image,0)

    flter = np.ones((fsize,fsize))

    append = int(fsize/2)

    a = np.shape(img)

    portion = np.zeros((fsize,fsize))


    flter = flter/((fsize)**2)

    for i in range(append,a[0]-append):
        for j in range(append,a[1]-append):
            portion = img[i-append:i+append+1,j-append:j+append+1]
            flterportion = portion*flter
            img[i,j] = np.sum(flterportion)

    cv.imshow('New Image',img)
    cv.imwrite('New Image.png',img)
