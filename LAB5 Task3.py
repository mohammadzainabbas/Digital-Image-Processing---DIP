import numpy as np
import cv2 as cv

def guasian(image):

    img = cv.imread(image,0)

    cv.imwrite('Original Image.png',img)

    flter = [[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]]

    a = np.shape(img)

    for i in range(1,a[0]-1):
        for j in range(1,a[1]-1):
            portion = img[i-1:i+1+1,j-1:j+1+1]
            flterportion = portion*flter
            img[i,j] = np.sum(flterportion)

    cv.imshow('New Image',img)
    cv.imwrite('New Image.png',img)
