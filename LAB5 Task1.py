import numpy as np
import cv2 as cv

def filter (image,fsize):

    img = cv.imread(image,0)

    a = np.shape(img)

    print(np.shape(img))

    flter = np.ones((fsize,fsize))

    append = int(fsize/2)

    new_img = np.ones(((2*append)+a[0],(2*append)+a[1]))

    b = np.shape(new_img)

    print(np.shape(new_img))

    new_img[:append,:] = 0

    new_img[b[0]-append:,:] = 0

    new_img[:,:append] = 0

    new_img[:,b[1]-append:] = 0

    portion = np.zeros((fsize,fsize))

    for i in range(0,a[0]-1):
        for j in range(0,a[1]-1):
                new_img[i+append,j+append] = img[i,j]

    flter = flter/((fsize)**2)

    for i in range(append,b[0]-append):
        for j in range(append,b[1]-append):
            portion = new_img[i-append:i+append+1,j-append:j+append+1]
            flterportion = portion*flter
            new_img[i,j] = np.sum(flterportion)

    cv.imshow('New Image',new_img)
    cv.imwrite('New Image.png',new_img)
