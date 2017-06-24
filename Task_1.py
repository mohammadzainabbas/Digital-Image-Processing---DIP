import matplotlib as lib, cv2 as cv, numpy as np

def Thresholding():

    img = np.array(cv.imread('fig01.tif',0))

    mean_value = np.mean(img)

    r,c = np.shape(img)

    for i in range(r):
        for j in range(c):
            if img[i,j] > mean_value:
                img[i,j] = 255
            else:
                img[i,j] = 0

    cv.imshow('Binary Image', img)
    cv.imwrite('Binary Image.png',img)
    cv.waitKey(10000)
    cv.destroyAllWindows()

    return

def Negative():

    img = np.array(cv.imread('Binary Image.png',0))
 
    mean_value = np.mean(img)

    r,c = np.shape(img)

    for i in range(r):
        for j in range(c):
            img[i,j] = 255 - img [i,j]

    cv.imshow('Negative Image', img)
    cv.imwrite('Negative Image.png',img)
    cv.waitKey(10000)
    cv.destroyAllWindows()

    return

Thresholding()
Negative()
