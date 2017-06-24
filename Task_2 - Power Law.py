import matplotlib as lib, cv2 as cv, numpy as np

def PowerLaw(img, gamma):

    r,c = np.shape(img)

    power_img = np.power(img, gamma)

    power_img = NormalizeImage(power_img)

    return power_img

def LogTransformation(img):

    img = np.log10(img)

    return img

##def LogTransformation(img):
##
##    r,c = np.shape(img)
##
##    for i in range(r):
##        for j in range(c):
##            img[i,j] = np.log10(1 + img[i,j])
##
##    return img


def Display():
    
    img1 = np.array(cv.imread('fig01.tif',0))
    img2 = np.array(cv.imread('fig02.tif',0))

    gamma1 = .9
    gamma2 = .6
    gamma3 = 1.3
    gamma4 = 1.8

    power_img1_1 = PowerLaw(img1, gamma1)
    power_img2_1 = PowerLaw(img2, gamma1)

    power_img1_2 = PowerLaw(img1, gamma2)
    power_img2_2 = PowerLaw(img2, gamma2)

    power_img1_3 = PowerLaw(img1, gamma3)
    power_img2_3 = PowerLaw(img2, gamma3)

    power_img1_4 = PowerLaw(img1, gamma4)
    power_img2_4 = PowerLaw(img2, gamma4)

##    power_img1_1 = LogTransformation(power_img1_1)
##    power_img2_1 = LogTransformation(power_img2_1)
##
##    power_img1_2 = LogTransformation(power_img1_2)
##    power_img2_2 = LogTransformation(power_img2_2)
##
##    power_img1_3 = LogTransformation(power_img1_3)
##    power_img2_3 = LogTransformation(power_img2_3)
##
##    power_img1_4 = LogTransformation(power_img1_4)
##    power_img2_4 = LogTransformation(power_img2_4)

    cv.imshow('Power Image 1 - 0.9',power_img1_1)
    cv.imshow('Power Image 2 - 0.9',power_img2_1)

    cv.imshow('Power Image 1 - 0.6',power_img1_2)
    cv.imshow('Power Image 2 - 0.6',power_img2_2)

    cv.imshow('Power Image 1 - 1.3',power_img1_3)
    cv.imshow('Power Image 2 - 1.3',power_img2_3)

    cv.imshow('Power Image 1 - 1.8',power_img1_4)
    cv.imshow('Power Image 2 - 1.8',power_img2_4)
    
    cv.imwrite('Power Image 1 - 0.9.png',power_img1_1)
    cv.imwrite('Power Image 2 - 0.9.png',power_img2_1)

    cv.imwrite('Power Image 1 - 0.6.png',power_img1_2)
    cv.imwrite('Power Image 2 - 0.6.png',power_img2_2)

    cv.imwrite('Power Image 1 - 1.3.png',power_img1_3)
    cv.imwrite('Power Image 2 - 1.3.png',power_img2_3)

    cv.imwrite('Power Image 1 - 1.8.png',power_img1_4)
    cv.imwrite('Power Image 2 - 1.8.png',power_img2_4)
    cv.waitKey(10000)
    cv.destroyAllWindows()

    return

Display()

