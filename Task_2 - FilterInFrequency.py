import numpy as np, cv2 as cv

def Normalize(img):
    img_1=np.array(img,dtype=np.uint8)
    r,c = np.shape(img)
    img_min = np.min(img)
    img_max = np.max(img)
    #To normalize image
    for i in range(r):
        for j in range(c):
            img_1[i,j] = 255*((img[i,j] - img_min)/(img_max-img_min))
    return img_1

def FourierTransform(img):
    
    #img = cv.resize(img, (128,128))
    
    img = 20*np.log(np.abs(np.fft.fftshift(np.fft.fft2(img))))

    return img

def InverseFourierTransform(img):

    img = 20*np.log(np.abs(np.fft.ifftshift(np.fft.ifft2(img))))

    return img


def FilterInFrequencyDomain(img):
    r,c=np.shape(img)
    distance_map = np.zeros((r,c))

    middle_pixel_x = np.floor(r/2)
    middle_pixel_y = np.floor(c/2)

    for i in range(r):
        for j in range(c):
            distance_map[i,j] = np.sqrt(pow((i - middle_pixel_x),2) + pow((j - middle_pixel_y),2))

    Threshold = 100

    distance_map [distance_map <= Threshold] = 1
    distance_map [distance_map > Threshold] = 0

    dot_product = np.dot(img, distance_map)

    DFT = FourierTransform(dot_product)

    return

img = np.array(cv.imread('Fig01.tif',0), dtype = np.double)
DFT = FourierTransform(img)
img_1 = InverseFourierTransform(DFT)

cv.imshow('DFT',DFT)
cv.imshow('Inverse DFT', img_1)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Inverse DFT.png',img_1)
cv.imwrite('DFT.png',DFT)