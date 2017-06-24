import numpy as np, cv2 as cv, matplotlib.pyplot as plt

def Thresholding(img, Threshold):

    r,c = np.shape(img)

    for i in range(r):
        for j in range(c):
            if img[i,j] > Threshold:
                img[i,j] = 255
            else:
                img[i,j] = 0
                
    return img

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

def Convolution (img,filter):

    return cv.filter2D(img,cv.CV_32F,filter)

img = np.array(cv.imread('wire-bond.tif',0))

HorizontalSobel = np.array(((-1,-2,-1),
                            (0, 0, 0),
                            (1, 2, 1)))

VertialSobel = np.array(((-1, 0, 1),
                         (-2, 0, 2),
                         (-1, 0, 1)))

HS_img = Convolution(img, HorizontalSobel)
VS_img = Convolution(img, VertialSobel)

#Magnitude = np.abs(HS_img) + np.abs(VS_img)
Magnitude = np.sqrt(np.square(HS_img) + np.square(VS_img))
Phase = np.arctan2(HS_img,VS_img)

Magnitude = Normalize(Magnitude)
Phase = Normalize(Phase)

Threshold = 0.000001*np.max(Magnitude)

Edge_Image = Thresholding(Magnitude, Threshold)
Magnitude = np.uint8(Magnitude)
cv.imshow('Magnitude',Magnitude)
cv.imshow('Phase',Phase)
cv.imshow('Final edge image',Edge_Image)
cv.waitKey(10000)
cv.destroyAllWindows()
cv.imwrite('Magnitude.png',Magnitude)
cv.imwrite('Phase.png',Phase)
cv.imwrite('Edge Image.png',Edge_Image)

##magnitude_spectrum = 20*np.log(np.abs(np.fft.fftshift(np.fft.fft2(img))))
##plt.imshow(magnitude_spectrum)